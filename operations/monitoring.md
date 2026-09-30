# Monitoring and service objectives

Example objectives require owner approval: monthly user-facing availability 99.5%, backup recovery point no older than 24h, quarterly restore within 4h. Define whether agreed maintenance counts in the availability denominator. Measure from a client perspective, not just container process state.

| Signal | Example trigger | Action / owner |
| --- | --- | --- |
| HTTPS and login path | Three consecutive failed one-minute probes | Operator checks proxy, app and dependencies |
| Synthetic author workflow | Cannot create/read/delete a marked test page | Operator investigates application/API behavior |
| TLS validity | Less than 21 days remaining | Operator investigates renewal |
| Disk usage | 75% warning, 85% urgent; growth predicts exhaustion | Operator adds capacity or safely applies retention |
| Backup | Job failure immediately, age >26h | Backup operator reruns or declares RPO breach |
| Recovery exercise | Last successful drill >90 days | Service owner schedules exercise |
| Database/Redis | Restarts, unhealthy status, persistent errors | Operator inspects logs and memory/storage pressure |
| Content quality | Critical page review overdue | Content owner reviews; steward escalates |

Synthetic tests need a least-privilege account and cleanup, and must not include sensitive content. Decide probe behavior for SSO or restricted networks. Page on actionable failure, deduplicate alerts and document acknowledgement/escalation deadlines. Do not log credentials or private page bodies. Choose log retention/access according to customer policy.

These are implementation requirements; the repository does not deploy a monitoring stack. Acceptance needs a triggered test alert, named recipient, response evidence and a link to the runbook.
