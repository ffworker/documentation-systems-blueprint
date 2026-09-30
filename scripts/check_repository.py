#!/usr/bin/env python3
"""Check required blueprint coverage and relative Markdown targets; no network."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = [
    'README.md', 'LICENSE', 'architecture/overview.md',
    'evaluation/requirements.md', 'evaluation/decision-matrix.md',
    'deployment/compose.yaml', 'deployment/compose.tls.yaml', 'deployment/.env.example',
    'migration/legacy-to-new-platform.md', 'migration/bookstack-to-docmost.md',
    'operations/backup.md', 'operations/restore.md', 'operations/updates.md',
    'operations/monitoring.md', 'operations/disaster-recovery.md',
    'security/rbac.md', 'security/access-model.md', 'security/secrets.md',
    'security/hardening.md', 'governance/ownership.md',
    'governance/documentation-lifecycle.md', 'governance/review-process.md',
    'handover/acceptance-checklist.md', 'handover/admin-handover.md',
    'handover/user-onboarding.md', 'examples/fictional-system/README.md',
]
errors = [f'Missing or empty: {p}' for p in required
          if not (root / p).is_file() or not (root / p).stat().st_size]
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            continue
        relative = target.split('#', 1)[0]
        if not (path.parent / relative).exists():
            errors.append(f'{path.relative_to(root)}: broken link {target}')
for p in root.glob('deployment/.env*'):
    if p.name != '.env.example':
        errors.append(f'Local secret file inside delivery tree: {p.name}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(required)} required artifacts and relative Markdown file targets')
