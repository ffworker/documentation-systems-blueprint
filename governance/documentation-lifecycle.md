# Documentation lifecycle

States: draft → review → published → review-due → revised or archived → deleted under retention policy. Each transition has an owner; a review date is not proof that a review occurred.

Minimum metadata: title, stable identifier, owner and deputy, classification, service/domain, status, last verification date, next review date and related records. Use templates consistently without forcing every document to repeat irrelevant fields.

Suggested cadence: critical recovery and access runbooks every 90 days; ordinary service documentation every 180 days; review immediately after material system change or incident. These are starting assumptions requiring agreement. Archive superseded pages with a link to their replacement; delete only after retention review.

Use a predictable hierarchy by domain/service/task, descriptive titles and a controlled small tag vocabulary. Separate task procedures from background explanations. Document prerequisites, expected outcomes, verification and rollback for every operational procedure.

Secrets remain in a vault. Screenshots must be sanitized and should not replace searchable steps. A runbook is accepted when another qualified person can use it successfully, not when its author marks it complete.

For the Docmost reference, apply the [five-space content structure](docmost-structure.md) and [GitHub/Docmost change boundary](change-boundary.md). Material operational changes trigger review; cosmetic UI changes and behavior-preserving refactors do not.
