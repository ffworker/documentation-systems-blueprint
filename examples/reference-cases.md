# Reference cases: Docmost, Signaturee and Bistro Connect

These names identify the reference cases used to refine the blueprint. The descriptions below capture reusable documentation patterns, not a live inventory or deployment validation. No actual hosts, IPs, company names, accounts, configuration values or operational evidence are included. Suggested page splits and runbooks still need local verification.

| Case | Generic purpose and architecture | Lesson |
| --- | --- | --- |
| Docmost | Self-hosted collaborative documentation with application, database, cache and attachments | Document the knowledge platform itself, including ownership, backup scope and independently accessible recovery guidance |
| Signaturee | Signature generation combining a web interface, application backend and script-based processing | Explain component boundaries, data inputs and the verified start mechanism; distinguish implementation changes from operational changes |
| Bistro Connect | RSS-based display content served by a web application and shown by Anthias display players | Separate central application health from player/network/display health; identify both sides of the dependency chain |

## Docmost

The system page explains purpose, edition, dependencies, content storage, access responsibilities and backup/recovery objectives. Link procedures for backup, restore, updates and access administration under `30 Workflow & Abläufe → Docmost`. Keep a recovery copy accessible outside the platform it restores. A normal system overview table avoids a paid feature dependency.

## Signaturee

The main page connects the input data, generator, backend and user interface. Detailed configuration or architecture can become subpages when useful. Link `Dienst prüfen & neu starten`, update, import and recovery runbooks as needed. Do not copy real directory data or generated signatures into this public blueprint.

A visual UI redesign or internal refactor stays in GitHub unless behavior relevant to users or operators changes. A new authentication method, input format, data location or generation workflow requires updating the affected Docmost page. Runtime startup details must be verified in the deployment, not inferred from a repository README.

## Bistro Connect

The system page explains the central feed/web service and the Anthias player role without confusing a working server with a working display. Suggested detail pages cover architecture and component configuration. `Störung analysieren` should distinguish feed availability, web service health, connectivity and player state before remediation. Update, rollback, feed-management and player-configuration procedures belong under the system's workflow group when needed.

## Applying the examples

Use [System / Dienst](../templates/system-documentation.md) for the canonical description and [Workflow / Runbook](../templates/runbook.md) for tasks. Keep unknowns explicit and validate with another operator. The separate [fictional worked example](fictional-system/README.md) demonstrates filled records; neither example set proves production readiness.
