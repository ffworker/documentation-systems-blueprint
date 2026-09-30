# Future roadmap

## First: validate the manual documentation standard

Apply the [space structure](governance/docmost-structure.md), two core templates and operational change rules. Prioritize useful navigation, clear ownership, verified recovery procedures and a second operator's ability to use the documentation. Capture gaps and actual validation results privately before automating authoring.

## Later: standalone local-LLM documentation intake

Status: future idea only; not implemented or required by this blueprint. A separate project could provide a local documentation interview agent with an interactive CLI. It could combine approved repository material, deliberately supplied sanitized host evidence and operator answers, ask for missing facts, distinguish observation from assumption, and suggest whether content belongs in a system page or runbook.

A possible flow is: operator interview → structured draft facts with sources and unknowns → Docmost-compatible Markdown → human review → manual publication. The aim is better intake and verification, not simply more generated prose. Evaluate against the manual templates and sanitized reference cases before choosing a model or integration.

Keep it standalone and Community-edition compatible. Do not depend on Docmost's paid AI or API-key features, assume direct publication is available, or build an integration now. Any later implementation must define consent for input collection, secret filtering, local data retention, evidence handling and human approval before publication. This roadmap adds no CLI, model runtime, host collector or automated publishing behavior.
