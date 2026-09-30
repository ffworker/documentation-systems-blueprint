# Migration validation checklist

Record tester, date, source/target versions, batch and evidence for each result. Unchecked means pending.

- [ ] Source full backup restored successfully outside production.
- [ ] Inventory covers all containers, pages, files and access exceptions.
- [ ] Target counts reconcile to migrated + deliberately excluded source items.
- [ ] Attachment hashes match where bytes are unchanged; converted assets reviewed.
- [ ] Every critical runbook exercised by someone other than its author.
- [ ] Tables, code, diagrams, links and anchors render and behave correctly.
- [ ] Restricted content cannot be discovered through search, direct URLs, files or exports by an unauthorized user.
- [ ] Histories/authorship/comments retained or loss explicitly accepted.
- [ ] Final source freeze enforced; delta changes reconciled.
- [ ] Rollback owner, deadline and target-edit reconciliation method agreed.
- [ ] Content owners signed off; retirement and archive expiry approved.

Exception record: ID, affected items, severity, business impact, workaround, owner, resolution deadline, acceptance authority and evidence. Critical defects block cutover; only the accountable owner may accept a lower-severity residual risk.
