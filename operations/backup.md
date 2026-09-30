# Backup runbook — maintenance-window reference

## Recovery contract

Fictional target: RPO 24h and RTO 4h. Agree real values with the service owner and measure them. Schedule daily backups only if the resulting outage is acceptable. Backups must include PostgreSQL, attachments and Redis state from the same quiescent interval, plus an independently escrowed configuration/secret set and exact image manifest.

Use a restricted backup location outside this repository. Encrypt before copying to independent storage; use separate deletion credentials and a retention policy (example: 14 daily and 8 weekly generations). Monitor job failure, age, size anomalies and offsite-copy completion. A backup left only on the service host is not disaster recovery.

## Procedure

Commands below run from `deployment/` with Bash. In TLS mode set `dc=(docker compose -f compose.yaml -f compose.tls.yaml)` instead. The reference assumes GNU tar in the official PostgreSQL image, compatible local Docker named volumes, and an isolated maintenance window.

1. Notify users, block new access, and stop writers cleanly. Stop proxy first if present, then Docmost. Wait for termination before stopping dependencies. Do not let automation restart them during the copy.
2. Stop database and Redis with sufficient grace. Inspect exit status and logs: PostgreSQL must report a clean shutdown. If Docker kills the database at timeout, abort this procedure and investigate rather than declaring a clean backup.
3. Archive stopped volumes with a read-only helper; do not start application images against them.

```bash
set -euo pipefail
dc=(docker compose)
# TLS mode: use both files in dc, then "${dc[@]}" stop proxy
umask 077
backup_dir="$(mktemp -d /tmp/docs-backup.XXXXXXXX)"
"${dc[@]}" stop -t 120 docmost
"${dc[@]}" stop -t 120 db redis
"${dc[@]}" ps -a
# Verify clean shutdown in logs before continuing.
helper_image="$("${dc[@]}" config --format json | python3 -c 'import json,sys; print(json.load(sys.stdin)["services"]["db"]["image"])')"
for service in docmost db redis; do
  container_id="$("${dc[@]}" ps -a -q "$service")"
  test -n "$container_id" || exit 1
  case "$service" in
    docmost) volume_path=/app/data/storage ;;
    db) volume_path=/var/lib/postgresql ;;
    redis) volume_path=/data ;;
  esac
  docker run --rm --network none --read-only --user 0:0     --volumes-from "$container_id:ro" --entrypoint tar "$helper_image"     -C "$volume_path" -czpf - . > "$backup_dir/$service.tgz" || exit 1
done
"${dc[@]}" config --images > "$backup_dir/images.txt"
for service in docmost db redis; do
  docker inspect --format '{{.Name}} {{.Image}}' "$("${dc[@]}" ps -a -q "$service")"
done > "$backup_dir/image-ids.txt"
(cd "$backup_dir" && sha256sum *.tgz > SHA256SUMS)
```

4. On any error, do not label this backup successful. Keep the services stopped until the operator chooses safe recovery or restart. Inspect archive contents with `tar -tzf`, record the backup timestamp/host architecture and retain the immutable release digests with the archives. Image IDs alone cannot be pulled from a registry.
5. Escrow `.env`, Compose files, private overrides and proxy config in an encrypted restricted backup set. Never put resolved Compose configuration into public CI logs. For TLS, separately preserve Caddy volumes with the same stopped-volume method, or record an approved certificate reissuance plan.
6. Restart with `"${dc[@]}" up -d`. Verify login, search, editing and attachments, then reopen access. Encrypt and transfer the backup with the organization's approved tool; record independent-copy verification. Remove the local staging copy only after verification and according to retention policy.

Test [restore](restore.md) quarterly and after material version/storage changes. Record measured duration, data loss window, recovered attachment hashes and operator identity. Do not mark the RPO/RTO achieved until the exercise proves it.
