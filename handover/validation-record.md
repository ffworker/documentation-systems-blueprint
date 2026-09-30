# Validation record

Initial preparation date: 2026-09-30.

| Check | Status | Meaning |
| --- | --- | --- |
| Repository structure and local Markdown links | Passed locally, 2026-09-30 | Automated structural check |
| Base Compose parsing | Passed locally, 2026-09-30 | Syntax/interpolation only |
| TLS overlay removes application host port | Passed locally, 2026-09-30 | Resolved configuration assertion |
| Missing secrets block configuration | Passed locally, 2026-09-30 | Fail-closed interpolation |
| Docmost runtime startup and user tasks | Not run | Local Docker daemon access unavailable |
| TLS issuance and email | Not run | Requires actual infrastructure |
| Source migration and access acceptance | Not run | Requires pilot data and users |
| Backup/restore and timed recovery | Not run | Requires running containers and representative data |

The CI workflow validates structure and configuration only. Use a private copy of this table to record the exact release, date, operator, evidence and result of runtime acceptance. Do not promote pending or unrun checks to passed based on static validation.
