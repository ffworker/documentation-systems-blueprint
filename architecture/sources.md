# Source register

Reviewed 2026-09-30. Upstream documentation evolves; check again when selecting a release. Statements about editions are not contractual license advice.

| Source | What it supports |
| --- | --- |
| [Docmost installation](https://docmost.com/docs/installation) | Docker setup, initial workspace owner, WebSocket requirement |
| [Release v0.96.0](https://github.com/docmost/docmost/releases/tag/v0.96.0) | Reference application release selection |
| [Compose at v0.96.0](https://github.com/docmost/docmost/blob/v0.96.0/docker-compose.yml) | PostgreSQL 18 mount layout, Redis 8, storage path |
| [Environment variables](https://docmost.com/docs/self-hosting/environment-variables) | Application URL, secrets, storage and SMTP |
| [Docmost import/export](https://docmost.com/docs/user-guide/import-export) | Markdown/HTML transfer; validate fidelity in pilot |
| [Docmost self-hosting](https://docmost.com/docs/category/self-hosting) | Navigation to current license and edition information |
| [BookStack export/import](https://www.bookstackapp.com/docs/user/export-import/) | Export formats; exports are not application backups |
| [Caddy reverse proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy) | HTTP and WebSocket proxy behavior |
| [Compose services](https://docs.docker.com/reference/compose-file/services/) | Health dependencies, ports and volume configuration |
| [PostgreSQL file-system backup](https://www.postgresql.org/docs/18/backup-file.html) | Consistent physical backup requires shutdown or valid snapshot procedures |

The operating model, acceptance thresholds and evaluation example are blueprint design choices, not upstream claims or measured customer results.
