# Contributing

Keep lifecycle guidance vendor neutral and implementation assumptions explicit. Use synthetic content and reserved domains. Never commit customer exports, private inventory, `.env`, backup archives or real evidence screenshots. Templates intentionally contain bracketed fields; implementation files should not contain unexplained placeholders.

For a change: state the requirement, update affected ADRs/runbooks, explain risks and verify local links and Compose behavior. Product feature claims need current primary sources and version/edition context. Runtime claims need actual evidence.

```sh
python3 scripts/check_repository.py
python3 scripts/check_compose.py
```

The second command needs Docker Compose but no daemon. It uses temporary synthetic credentials only for parsing, verifies loopback/default and TLS port boundaries, and confirms missing secrets fail. It never starts containers.

For operational acceptance additionally follow [handover checks](handover/acceptance-checklist.md) in an isolated environment. Submit a focused pull request with checks performed and limitations. Keep external link checks manual to avoid confusing temporary network failures with content errors.
