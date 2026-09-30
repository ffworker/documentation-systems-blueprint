# RB-ATLAS-002 — Investigate “pages load, editing disconnects”

Owner: operations lead. Status: illustrative draft, not executed. Scope: fictional Atlas service. Required access: read-only monitoring/log access; changes require operator authorization.

1. Ask whether one user or multiple users are affected and note the start time. Do not collect page contents or session tokens.
2. Check recent proxy/app changes and sanitized browser connection errors. Compare the approved HTTPS origin with `APP_URL`.
3. Check application and Redis state and proxy errors. A healthy database does not establish a working collaborative channel.
4. Test with two synthetic users on a disposable page. Confirm WebSocket connection and reconnect behavior. If only proxy access fails while an approved isolated application test works, investigate the proxy path and middleboxes.
5. Apply the verified configuration correction through the normal change process. Do not restart the database or delete Redis data as a speculative fix.

Success: both users see each other's edits and retain them after reconnect. If the change fails, revert the reviewed proxy configuration and escalate with sanitized timestamps/errors. Record cause, uncertainty and follow-up testing.
