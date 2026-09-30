# SYS-ATLAS-001 — Atlas Knowledge Service

| Metadata | Fictional value |
| --- | --- |
| Owner / deputy | Knowledge steward / operations lead |
| Classification | Internal in scenario; public synthetic example here |
| Status | Draft, not accepted |
| Last verified | Not yet tested |
| Next review | Before pilot acceptance |

Purpose: provide operational runbooks and project knowledge to a fictional operations team. Loss of service delays routine work; emergency procedures have protected offline copies.

Architecture: Docmost behind a TLS proxy, PostgreSQL, Redis and attachment storage on one host. Candidate address: `https://docs.example.com`, reserved and nonoperational. Dependencies: host storage, DNS, certificates, identity policy, mail and independent backup storage.

Fictional objectives: RPO 24h, RTO 4h; no availability achievement claimed. Scope excludes credential storage and formal records retention. The single host is a known outage risk; the service owner must approve it after a measured restore exercise.

Operations: daily coordinated backup in an approved window; alert on stale backup or low disk; monthly update review; quarterly restore drill and privileged-access review. Recovery follows the repository's [restore runbook](../../operations/restore.md).
