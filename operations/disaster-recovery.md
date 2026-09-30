# Disaster recovery coordination

## Declare and contain

The incident commander records impact, incident start, last known good point and decision log. Stop harmful writes and preserve forensic evidence if compromise is suspected. Use an independent contact/runbook copy when the documentation service itself is unavailable.

## Choose the recovery route

- Application fault with intact data: investigate and restore service without overwriting storage.
- Host/storage loss: restore the coordinated backup to an isolated replacement host.
- Data corruption or compromise: choose a clean point with owners, restore in isolation, investigate credentials and integrations before exposing it.

The service owner authorizes accepted data loss and recovery-point selection. The operator performs [restore](restore.md); a second person verifies permissions and content. Compare measured RPO/RTO with the approved contract and communicate any breach.

## Promote and close

Fence the former primary, verify TLS/DNS and restrict writers until acceptance. Reconcile surviving edits when possible. Restore integrations deliberately and monitor errors. Record timeline, loss window, evidence, decisions and unresolved risks. Within five working days, review the incident without blame, assign corrective actions and update tests/runbooks.

Escalation roster, vendor contacts and backup unlock procedures belong in a protected offline-accessible private record. Test access to that record without the failed platform.
