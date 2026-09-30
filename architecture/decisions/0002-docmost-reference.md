# ADR 0002 — Docmost reference implementation

- Date: 2026-09-30
- Status: accepted for this example; not a customer selection result
- Owner: blueprint maintainer

## Context and alternatives

The fictional scenario values browser-based contribution and concurrent editing. Alternatives include repairing the existing BookStack, another collaborative wiki, a managed knowledge platform, and a Git-based documentation site. Keeping the existing system may have the lowest migration risk.

## Decision

Use Docmost to demonstrate an application/database/queue/storage stack. Start with local accounts in an isolated pilot. No LDAP/SSO requirement is assumed for that pilot. Enterprise identity, audit and lifecycle requirements must be reassessed against current edition terms before adoption.

## Consequences

Migration loses some source semantics unless explicitly rebuilt. Collaborative editing creates a WebSocket dependency. Operating PostgreSQL, Redis and file storage requires coordinated recovery. A modern interface alone does not justify migration.

## Evidence and review trigger

See the [source register](../sources.md) and [evaluation method](../../evaluation/decision-matrix.md). Revisit if required controls are unavailable or paid features change total cost, export fidelity fails, or user trials show no benefit over improving the incumbent.
