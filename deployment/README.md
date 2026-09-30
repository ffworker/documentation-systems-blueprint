# Deploy the reference

## Prerequisites and boundaries

Use a dedicated Linux host with Docker Engine, Compose ≥2.24.4 and a supported CPU architecture. The executing account needs Docker access (effectively host-level privilege). Choose disk/RAM/CPU from a pilot, not an unsupported sizing promise. This guide assumes GNU/Linux and local named volumes, not external S3 storage.

Reference application: Docmost 0.96.0. PostgreSQL 18 and Redis 8 match the upstream release's Compose layout. Caddy 2 is optional. Major tags receive changes; before production replace all image references with reviewed digest-pinned references and preserve the resolved manifest. Do not introduce database major upgrades by changing an environment variable.

## Local pilot

1. Copy `.env.example` to `.env`; set file mode 600. Set `APP_SECRET` and `POSTGRES_PASSWORD` to independent `openssl rand -hex 32` outputs. Use a hex database password here so interpolation into the connection URI is safe; arbitrary passwords need URI encoding.
2. Review `APP_URL` and optional SMTP. Empty SMTP fields deliberately provide no working mail service; onboarding/password-reset acceptance cannot pass until mail is configured and tested.
3. Run `docker compose config --quiet` (avoid printing resolved secrets), then `docker compose pull` and `docker compose up -d`.
4. Open `http://localhost:3000` on the host, or use an approved SSH tunnel for a remote host. Complete owner/workspace setup before any wider exposure.
5. Check `docker compose ps`, inspect redacted logs, and exercise create/edit/search/upload/download with two test users. Healthy database/Redis status alone does not establish application readiness.
6. Record exact image digests, host architecture, versions and evidence in the private release record. Complete the [acceptance checklist](../handover/acceptance-checklist.md).

## Network service

Follow [reverse proxy setup](reverse-proxy/README.md). Firewall policy, DNS, certificates and SMTP belong to the actual deployment. This repository installs none of them on the host automatically. In TLS mode use `docker compose -f compose.yaml -f compose.tls.yaml` consistently, including stopping/restarting services.

## Persistence and change safety

Named volumes hold database, attachments and Redis state. `docker compose down` preserves them; `down --volumes` destroys them and is never a routine maintenance step. Keep a stable project name because it determines volume names. Changing database passwords in `.env` does not change an initialized database role: rotate the role and connection configuration as a coordinated operation.

For backups use [the maintenance procedure](../operations/backup.md). For version changes use [updates](../operations/updates.md). No runtime test is implied by successful Compose parsing. See [validation status](../handover/validation-record.md).
