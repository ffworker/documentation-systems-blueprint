# Docmost content structure

This is the current reference content model distilled from the setup, not an export or audit of a live workspace. The five spaces below are the baseline. Create additional pages only when useful; suggested child pages are not a claim that they already exist.

| Space | Reader's question | Content |
| --- | --- | --- |
| `00 Documentation` | How do we document? | Standards, authoring guidance and templates |
| `10 Infrastructure` | What does our IT run on? | Physical/virtual infrastructure, storage and networks |
| `20 Systeme & Dienste` | What is the system and how is it built? | System overview and canonical service descriptions |
| `30 Workflow & Abläufe` | What do I need to do? | Operational tasks, troubleshooting and recovery procedures |
| `99 Archive` | What has been retired or superseded? | Retired content with replacement links and retention decisions |

## Authoring entry points

In `00 Documentation`, provide:

- `40 - Neues System dokumentieren`: choose the primary space, search for existing content, use System / Dienst, verify runtime facts, link procedures and update the overview.
- `50 - Workflow / Runbook dokumentieren`: define a task and trigger, use Workflow / Runbook, include prerequisites, expected results, stop conditions and recovery, then ask a second operator to validate it.
- `90 - Vorlagen` with child pages `System / Dienst` and `Workflow / Runbook`, copied from the [core templates](../templates/README.md).

The 40 and 50 pages explain the process; they are not additional templates. A system has one primary documentation home. Link from infrastructure, workflows and the overview instead of copying its configuration into several pages.

## System overview

Create `00 - Systemübersicht` as a normal page in `20 Systeme & Dienste` using the [Markdown table](../templates/system-overview.md). Link each system name to its canonical page. Maintain status, owner, host, IP, platform, backup, monitoring and last review when adding, changing or retiring a system. Keep actual inventory in private Docmost only.

Use the Community/Open Source edition first. Ordinary pages, links and Markdown tables are sufficient for this baseline. [Bases are a commercial feature](https://docmost.com/docs/user-guide/bases), unavailable in the free edition (checked 2026-09-30); the overview must not depend on them. Do not require paid API keys, AI, granular page permissions or approval features for this workflow. Re-evaluate editions only for a documented need, and verify availability against the selected release. Use space access and a manual review record where appropriate; see the [review process](review-process.md).

## Main pages and subpages

Start with a useful system page, not an empty tree. Keep its purpose, owner, service status, access entry point, key dependencies and links visible. Split architecture, configuration or component details into subpages once size or a distinct reader task justifies it. Parent pages then become concise navigation and orientation pages.

Backup scope and recovery objectives belong on the system page (or a descriptive recovery subpage). The executable backup, restore, update, rollback and troubleshooting procedures belong in `30 Workflow & Abläufe`, grouped under the system name and linked in both directions. Begin with a single troubleshooting page containing common symptoms; split out an incident pattern when it needs its own substantial procedure. Do not create a separate page for every error message.

Example navigation (child topics are suggestions, not completed deployment evidence):

```text
20 Systeme & Dienste
├── 00 - Systemübersicht
├── Docmost
├── Signaturee
│   ├── Architektur
│   └── Betrieb & Konfiguration
└── Bistro Connect
    ├── Architektur
    └── Komponenten
30 Workflow & Abläufe
├── Docmost
│   └── Backup & Restore
├── Signaturee
│   └── Dienst prüfen & neu starten
└── Bistro Connect
    └── Störung analysieren
```

See the [sanitized reference cases](../examples/reference-cases.md) for why these systems exercise different documentation needs.

## Is the documentation useful?

Ask another operator to find the owner, explain the system's dependencies, locate a recovery procedure and complete a safe task without author coaching. Record gaps and unknown facts with owners rather than inventing values or treating a filled template as proof. Prefer improving navigation and verified procedures over adding more prose. Archive retired systems and update the overview without breaking replacement links.
