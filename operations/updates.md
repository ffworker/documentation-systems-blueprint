# Controlled updates

Owner: platform operator; approver: service owner. Review application, database, Redis and proxy advisories at least monthly and when critical notices arrive. Classify urgency with exposure and compensating controls.

1. Record current digests, configuration, schema expectations and release notes. Check edition/license changes and supported upgrade path.
2. Restore a recent backup into isolated staging. Upgrade one component at a time; major PostgreSQL upgrades require a separate tested logical migration or supported upgrade procedure.
3. Run login, mail, upload/download, search, permissions, collaborative editing and export checks. Repeat recovery validation if the data format changes.
4. Agree a maintenance window. Freeze writes, take and verify a coordinated backup, then update approved image references and recreate services with the correct Compose files.
5. Verify health and user tasks, compare error rate/latency to baseline, record exact deployed digests and reopen writes.

Rollback is not automatically an old image tag. Schema migrations may prevent older code from reading upgraded data. If incompatible, restore the complete pre-change database/files/Redis/config set into an isolated environment and reconcile any post-upgrade writes before promotion. Define this rollback boundary before updating.

Never run unattended `latest` image upgrades for this reference. Minor/patch updates also need compatibility review; major tags in the example must be pinned for a real release.
