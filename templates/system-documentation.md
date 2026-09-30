# System / Dienst

> Template — replace all bracketed fields before approval.

| Metadata | Value |
| --- | --- |
| Document ID | [stable ID] |
| Owner / deputy | [roles or approved contacts] |
| Classification | [public-approved / internal / restricted] |
| Status | [draft / reviewed / published / archived] |
| Last verified / next review | [dates] |
| Related service / change | [references] |

Target: `20 Systeme & Dienste` for a service, or `10 Infrastructure` for infrastructure. Keep one canonical page; link procedures from `30 Workflow & Abläufe`. Remove irrelevant fields and record unknown facts with an owner and follow-up. Public copies must use placeholders, not actual inventory.

## Purpose and criticality
[Purpose, users, impact of outage and service objectives. Service status: Produktiv / Pilot / Test / Außer Betrieb, distinct from document status.]

## Responsibility and access
[Technical owner, operations role, business owner and support contact; URL/entry point, authentication and role model. Secret-vault references only.]

## Source and deployment
[Repository link, deployed release, host/IP and OS/platform references in private inventory, deployment/configuration location and verified start mechanism. GitHub owns implementation; this page describes the deployed service.]

## Architecture and dependencies
[Diagram, trust boundaries, components, data flows, storage, identity, DNS/TLS, upstream/downstream services.]

## Inventory and configuration
[Components and responsibilities, ports/interfaces, data/configuration/log paths, private configuration sources, approved versions/edition and capacity assumptions; no embedded secrets. Separate verified runtime facts from assumptions.]

## Operations and recovery
[Health checks, logs, monitoring coverage/gaps, maintenance, backup scope/frequency/retention and owner, RPO/RTO, last restore evidence or explicit “not tested”. Link task procedures for restart, update, troubleshooting, backup and restore instead of duplicating them here.]

## Access and lifecycle
[Access approver, role model, patch owner, retirement criteria, retention.]

## Verification and known risks
[Evidence, reviewer, unresolved risks with owner and deadline.]
