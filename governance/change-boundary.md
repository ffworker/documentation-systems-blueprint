# GitHub implementation and Docmost operations

GitHub is authoritative for implementation: source code, tests, refactors, build details, commits, developer documentation and release history. Docmost is authoritative for the deployed service's operational contract and knowledge transfer: ownership, access, architecture, dependencies, configuration references and procedures.

Link between the system page and its repository. Record the deployed version or release when relevant. Repository defaults are evidence of intended behavior, not proof of live configuration; verify runtime facts privately. Do not mirror whole READMEs or maintain competing copies of runbooks. If a versioned operational procedure already has its canonical home in GitHub, link it explicitly from Docmost and identify its applicable release.

## When to update Docmost

| Change | Documentation action |
| --- | --- |
| Ports, URLs, APIs or integrations change | Update access/dependency descriptions and affected checks |
| Authentication, roles or ownership change | Update access guidance and responsibility records |
| Data paths, persistence or dependencies change | Update system facts, backup scope and recovery guidance |
| Start mechanism, deployment, backup, restore or monitoring change | Update affected runbooks and verify them |
| A material user or operator workflow changes | Update that workflow, even if the implementation change is entirely in the UI |
| Cosmetic UI changes, component rewrites or internal refactors with unchanged behavior | Keep implementation history in GitHub; no Docmost update needed |
| An incident reveals a missing or incorrect operating step | Correct the relevant procedure and record verification |

The test is operational impact, not frontend versus backend. Moving buttons or changing colors does not create a documentation obligation; changing how someone creates a domain, generates output or restores service can. At release review, identify affected pages or record that there is no operational impact. Avoid copying every commit into the wiki.

Update the [system overview](../templates/system-overview.md) when its summary fields change. Keep service lifecycle status separate from document review status. A review date means an actual check happened, not merely that a file was edited.
