#!/usr/bin/env python3
"""Parse Compose without a daemon; assert isolation and missing-secret rejection."""
import json
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
deploy = root / 'deployment'
base = ['docker', 'compose', '--project-directory', str(deploy)]
# Keep the parse deterministic; never inherit deployment secrets or image overrides.
env = {k: v for k, v in os.environ.items()
       if not k.startswith(('COMPOSE_', 'DOCKER_', 'SMTP_', 'MAIL_'))
       and k not in {'APP_SECRET', 'POSTGRES_PASSWORD', 'APP_URL', 'DOCS_DOMAIN',
                    'DOCMOST_IMAGE', 'POSTGRES_IMAGE', 'REDIS_IMAGE', 'CADDY_IMAGE'}}

def render(envfile, tls=False):
    cmd = base + ['--env-file', str(envfile), '-f', str(deploy / 'compose.yaml')]
    if tls:
        cmd += ['-f', str(deploy / 'compose.tls.yaml')]
    return subprocess.run(cmd + ['config', '--format', 'json'], env=env,
                          capture_output=True, text=True)

with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / 'parse.env'
    raw = (deploy / '.env.example').read_text()
    # Deliberately synthetic values, used only by config parsing.
    valid = raw.replace('APP_SECRET=\n', 'APP_SECRET=' + 'a' * 64 + '\n')
    valid = valid.replace('POSTGRES_PASSWORD=\n', 'POSTGRES_PASSWORD=' + 'b' * 64 + '\n')
    path.write_text(valid)
    for tls in (False, True):
        result = render(path, tls)
        if result.returncode:
            raise SystemExit('Compose parse failed: ' + result.stderr)
        model = json.loads(result.stdout)
        services = model['services']
        assert not services['db'].get('ports'), 'Database port published'
        assert not services['redis'].get('ports'), 'Redis port published'
        assert model['networks']['data']['internal'] is True
        ports = services['docmost'].get('ports', [])
        if tls:
            assert not ports, 'TLS mode leaves an application host port'
            assert {str(p['published']) for p in services['proxy']['ports']} == {'80', '443'}
        else:
            assert len(ports) == 1 and ports[0]['host_ip'] == '127.0.0.1'
    for key, synthetic in [('APP_SECRET', 'a' * 64), ('POSTGRES_PASSWORD', 'b' * 64)]:
        path.write_text(valid.replace(key + '=' + synthetic, key + '='))
        for tls in (False, True):
            assert render(path, tls).returncode != 0, f'Missing {key} accepted'
print('PASS: base/TLS Compose, network/port boundaries and missing-secret rejection')
