# Legacy-to-new-platform migration

## 1. Discover and preserve

Inventory pages, hierarchy, attachments, diagrams, owners, classification, timestamps, links, permissions, users and integrations. Separate active, stale, duplicate, restricted and retention-bound material. Take a restorable source-system backup before export. Export is not backup.

Assign each source item a stable migration ID. Record source reference, target reference, batch, owner, format, attachment count/checksum, transformation and validation result. Keep this inventory private if it contains real URLs or titles.

## 2. Pilot before choosing the final route

Test at least one item of each actual content type: nested pages, complex tables, embedded drawings, code blocks, large files, cross-links and restricted content. Import into a closed staging space. Measure fidelity, manual repair effort and time per batch. Rebuild permissions before granting broad access; text formats rarely carry authorization semantics.

## 3. Reconcile and prepare cutover

Define counts and hashes where formats stay identical; use content review where conversion changes bytes. Validate all critical pages, all restricted paths and every attachment. Sample remaining rendered pages using a documented risk-based sample; any systematic defect expands validation to the affected batch. Log omissions with owner-approved disposition. Reject unexplained count differences.

## 4. Freeze, transfer and accept

Announce a source write freeze, enforce it for all writers including API accounts, take a final backup/export and migrate the delta. Re-run reconciliation. Link replacement must account for page fragments and attachments. Record freeze timestamp and target opening time so edits can be attributed unambiguously.

Go/no-go: no open critical defect, all must-have requirements pass, recovery exercise accepted, owners approve content and access. Keep the legacy system read-only and access-restricted during an agreed retention period; do not expose an unpatched legacy service indefinitely.

## 5. Roll back or retire

Before target writes begin, rollback can reopen the frozen source. After target writes begin, stop target writes and reconcile new/changed/deleted items back to the source or an approved holding area before reopening it. Never silently discard post-cutover edits. Record the accountable decision maker and point of no simple return.

Retire only after acceptance, dependency checks, retention approval and recovery evidence. Revoke service accounts and integrations, remove DNS/routes, retain required encrypted archives with an expiry date, and document deletion. Exit planning for the new platform repeats the same discipline.
