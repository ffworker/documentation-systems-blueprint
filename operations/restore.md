# Restore runbook — isolated empty environment

## Preconditions

Incident commander or service owner approves the recovery point. Use a new isolated host/project, no production DNS and no outbound user mail. Match the recorded application, PostgreSQL, Redis and helper image versions/digests and host architecture. This is a cold physical PostgreSQL restore, not cross-major migration. Do not extract archives over existing data.

Obtain the matching three archives, checksum manifest and encrypted configuration/secret set. Verify provenance and decrypt only in restricted storage. Preserve `APP_SECRET` and database credentials. Change `APP_URL` and mail settings to isolated recovery values before starting the application. Archives contain sensitive data and must not be trusted from unknown sources.

## Procedure

Run from the recovered `deployment/` directory with Bash. Set `backup_dir` to the absolute verified backup location, and use a distinct `COMPOSE_PROJECT_NAME` in the recovery `.env`.

```bash
set -euo pipefail
dc=(docker compose)
# Set backup_dir before continuing, for example an approved recovery mount.
: "${backup_dir:?Set the verified backup directory}"
(cd "$backup_dir" && sha256sum -c SHA256SUMS)
"${dc[@]}" config --quiet
"${dc[@]}" create
helper_image="$("${dc[@]}" config --format json | python3 -c 'import json,sys; print(json.load(sys.stdin)["services"]["db"]["image"])')"
```

Check that containers are stopped and all three target named volumes are newly created and empty. If any contain data, stop and choose a new project; do not delete data as part of this runbook. Inspect each archive's paths before extracting. Restore ownership/numeric IDs as recorded by tar:

```bash
set -euo pipefail
for service in docmost db redis; do
  container_id="$("${dc[@]}" ps -a -q "$service")"
  test -n "$container_id" || exit 1
  case "$service" in
    docmost) volume_path=/app/data/storage ;;
    db) volume_path=/var/lib/postgresql ;;
    redis) volume_path=/data ;;
  esac
  docker run --rm -i --network none --read-only --user 0:0     --volumes-from "$container_id:rw" --entrypoint tar "$helper_image"     --numeric-owner -C "$volume_path" -xzpf - < "$backup_dir/$service.tgz" || exit 1
done
"${dc[@]}" up -d db redis
"${dc[@]}" ps
# Wait for both dependencies to be healthy; inspect logs if not.
"${dc[@]}" up -d docmost
```

Verify representative pages, search, attachments, role restrictions, login and two-user editing. Queued Redis jobs may be replayed; keep outbound mail/integrations blocked until reviewed. Record checksums, recovered timestamp, recovery duration and defects. A rendered login page alone is not recovery proof.

For production promotion: service owner accepts results, fence the old instance to prevent split writes, restore/validate proxy TLS state, change DNS/ingress under change control, then enable mail and integrations deliberately. Verify from a client and monitor. Keep the original environment isolated until retention approval. Record any irrecoverable edits since the backup; do not silently call them migrated.
