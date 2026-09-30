# TLS reverse proxy

Caddy forwards HTTP and WebSocket traffic on the private Docker edge network. Automatic public certificate issuance needs an owned, resolvable DNS name and the appropriate inbound ACME reachability. `docs.example.com` is reserved and cannot be deployed as your domain. Internal-only installations require an explicitly designed internal CA or DNS challenge solution; this file does not implement those.

Before exposing the service, create the initial workspace owner through the loopback-only lab mode (or an SSH tunnel to it). Restrict ingress to the intended users, then apply the TLS overlay. Set `APP_URL=https://<owned-domain>` and `DOCS_DOMAIN=<owned-domain>` together.

```sh
docker compose -f compose.yaml -f compose.tls.yaml config --quiet
docker compose -f compose.yaml -f compose.tls.yaml up -d
```

The `!reset` override removes the application's loopback publication, leaving only proxy ports. Always use both files for subsequent commands on this deployment. Test login, upload, email links, simultaneous editing and reconnect after proxy restart. Add HSTS only after HTTPS and recovery access are established; it can make certificate mistakes harder to recover from.

Preserve Caddy data/config volumes securely in TLS deployments, or document certificate reissuance and rate-limit implications during recovery. The application backup procedure covers three application volumes, not the proxy's certificate state.
