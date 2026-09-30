# Evidence-led platform evaluation

First apply mandatory requirements as pass/fail gates. A high weighted score cannot compensate for failed access controls, unlawful hosting, missing export or unaffordable required licenses. Unknown is not a pass.

Shortlist at least: improve the incumbent (e.g. BookStack), a collaborative platform (e.g. Docmost), a docs-as-code approach, and a managed service if procurement allows it. Evaluate the exact version and edition; avoid product popularity as a scoring criterion.

| Criterion | Weight | Evidence |
| --- | ---: | --- |
| Author usability and adoption | 25 | Timed pilot with representative authors |
| Operations and recoverability | 20 | Second administrator performs restore |
| Identity, access and audit fit | 20 | Role tests; current edition/license review |
| Migration and exit fidelity | 15 | Representative round-trip content sample |
| Three-year total cost | 10 | License, hosting, maintenance, migration, training |
| Search and information architecture | 10 | Benchmark questions and navigation tasks |

Score 0–5: 0 absent, 1 major gaps, 2 significant workaround, 3 meets requirement, 4 exceeds it with evidence, 5 materially better and proven. Weighted result = sum(weight × score / 5), on a 0–100 scale. Document uncertainty and sensitivity to changed weights.

## Arithmetic example — fictional alternatives, not product ratings

| Candidate | Usability | Operations | Access | Portability | Cost | Search | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Candidate A | 4 | 3 | 3 | 4 | 4 | 3 | 70 |
| Candidate B | 3 | 4 | 4 | 3 | 3 | 4 | 70 |

A tie should trigger closer evidence review, not arbitrary precision. Candidate A would lead if author usability mattered more; Candidate B if access and operations did. These invented values select neither Docmost nor another product.

## Selection record to complete

Candidate/version/edition; requirement gate results; scores with evidence links; three-year cost assumptions; residual risks; rejected alternatives; approver; review date. Write an ADR. If no candidate passes, revise scope or budget explicitly rather than weakening a mandatory control silently.
