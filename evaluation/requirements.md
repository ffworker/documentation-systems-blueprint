# Requirements discovery

Record an accountable approver, evidence and a decision date for every requirement. The values below are fictional starting assumptions, not defaults to impose on a customer.

| ID | Requirement | Priority | Verification | Example target |
| --- | --- | --- | --- | --- |
| R01 | Nontechnical authors can publish a reviewed runbook | Must | Five representative users complete an authoring task | 4/5 finish without admin help |
| R02 | Readers cannot change content; restricted material stays restricted | Must | Positive and negative access tests incl. search/export/attachments | Zero unauthorized access |
| R03 | Content and attachments can be recovered | Must | Isolated restore of representative dataset | RPO ≤24h, RTO ≤4h |
| R04 | Content can leave the platform | Must | Export and open externally; inventory reconciliation | All critical pages/files usable |
| R05 | Service meets residency and licensing constraints | Must | Contract/edition and hosting review | Customer-approved location and terms |
| R06 | Search finds common operational answers | Should | Ten benchmark questions | 9/10 found within two minutes |
| R07 | Concurrent authors retain edits | Should | Two-user editing and reconnect exercise | No lost accepted edits |
| R08 | Ownership and overdue reviews are visible | Must | Content register audit | Every critical page has an owner |
| R09 | Provisioning/offboarding fits identity policy | Must | Joiner/mover/leaver exercise | Access removed within approved deadline |
| R10 | Cost fits the support model | Must | Three-year TCO with staff time and restore exercises | Budget approved before purchase |

Discovery questions: audiences and languages; present content volume/quality; high-risk knowledge held by one person; attachments and diagrams; retention/deletion rules; identity and MFA; internet access; accessibility; integrations; outage tolerance; maintenance windows; staffing and escalation.

Deliver a signed scope, exclusions, risk register and inventory. Unresolved mandatory requirements block selection. For the fictional pilot local accounts are allowed; do not generalize that exception to a customer.
