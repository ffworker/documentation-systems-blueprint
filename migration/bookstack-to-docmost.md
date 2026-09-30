# Worked migration route: BookStack → Docmost

This is a procedure to validate, not a promise of lossless or automated conversion. Record source BookStack version and target Docmost version/edition first. Upstream formats and import behavior may change.

| Source concept | Candidate target | Required review |
| --- | --- | --- |
| Shelf | Navigation/grouping convention | Books can belong to multiple shelves; prevent duplicates |
| Book | Space or root page | Choose according to access boundary and ownership |
| Chapter | Parent page | Check nesting and ordering |
| Page | Page | Formatting, code, tables and anchors |
| Images/attachments | Files associated with target pages | Transfer bytes, permissions, links and download behavior |
| Roles/page overrides | Rebuilt target permissions | No assumed one-to-one equivalence |

1. Back up the source application using its own recovery procedure. Export representative books/chapters/pages as Markdown or HTML using an authorized account. BookStack's portable ZIP is a BookStack format; do not assume it is Docmost's ZIP format.
2. Import `.md` or `.html` files into a closed Docmost staging space using its import dialog. Trial each complex content type. Embedded HTML images and separate attachments need explicit verification; export an independent attachment inventory and fetch missing files through authorized source access.
3. Record old and new page identifiers in a mapping ledger. Rebuild hierarchy, page links, image/file links and permissions. Do not assume histories, authorship, comments, shelf relationships or access rules survive format conversion. Preserve required historical evidence in a restricted archive.
4. Review rendered content and exercise search, navigation, attachment downloads and unauthorized-user access. Resolve or accept every exception with its owner.
5. Follow the generic write freeze, delta migration, cutover and rollback plan in [migration strategy](legacy-to-new-platform.md).

A successful import message proves that the importer accepted files, not that the migration is complete. See the [validation checklist](validation-checklist.md) and [fictional mapping](../examples/fictional-system/migration-ledger.md).

Sources: [BookStack export/import](https://www.bookstackapp.com/docs/user/export-import/), [Docmost import/export](https://docmost.com/docs/user-guide/import-export).
