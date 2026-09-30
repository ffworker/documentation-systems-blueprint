# Secrets and configuration

`.env.example` contains blank secret fields. Generate independent high-entropy values and store actual `.env` files outside Git with mode 600 and protected parent directories. Docker environment values can be inspected by privileged users: this reference is not a secret vault. Use an approved secret delivery mechanism for a real deployment and verify the application's supported interface before assuming `_FILE` variables exist.

Back up the application key and database credentials in an encrypted, independently accessible vault. Losing a key can prevent valid sessions or application functions; rotation requires version-specific testing. Rotate database role credentials and application connection settings together; modifying `.env` alone does not change an initialized role password.

If a secret enters Git: revoke/rotate first, assess exposure including forks/actions/artifacts, then remove it from current files and coordinate history cleanup. Deleting one commit does not make an exposed secret safe. Never put secrets in issue bodies, screenshots, URLs or troubleshooting logs.
