# ADR 0003 — Single host and cold backup

- Date: 2026-09-30
- Status: proposed for pilot
- Owner: service owner and platform operator

## Context

A small internal platform can tolerate a scheduled maintenance window if stakeholders explicitly agree. Simultaneous database/files changes complicate consistency.

## Decision

Use a single Compose project with named volumes. For the reference backup, stop writers and then all stateful services cleanly; archive their volumes while stopped. Back up secrets separately. Recovery starts on an isolated empty host with the same image versions and compatible architecture.

## Alternatives and consequences

Logical database dumps plus synchronized file snapshots can reduce downtime but need coordination and version-specific testing. HA costs more and does not replace backups. Cold physical PostgreSQL backups require the same major version and compatible environment. Never restore them into a different major version as an upgrade method.

## Acceptance

Measure actual interruption and restore duration with realistic data. Fictional targets are RPO 24 hours and RTO 4 hours, not achieved results. Reject this design if the maintenance window or measured recovery is unacceptable. Revisit at capacity growth, recovery failure or changed business objectives.
