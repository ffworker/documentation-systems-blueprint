# Access model

Classify content as public-approved, internal, restricted or highly sensitive. Highly sensitive credentials and keys belong in a secret manager, never a wiki page. Public publishing is a separate, explicitly approved action; an internal page is not safe merely because its URL is hard to guess.

For every space identify audience, owner, approver, administrator, retention and export rules. Use the smallest maintainable set of groups. Avoid complex page-level exceptions unless the chosen product demonstrably enforces them for search, files, exports and links.

Local accounts are a fictional pilot assumption. Evaluate MFA, SSO, audit and automated deprovisioning against the chosen edition and identity policy. No identity feature is assumed free or available merely because another product has it.

Joiner: owner approves group and expiry. Mover: remove old groups before adding unnecessary access. Leaver: revoke sessions/tokens and shares where supported, disable access, transfer content ownership and test the result. Review privileged access monthly and all groups quarterly. Record exceptions with expiration and approver.

Infrastructure administrators can read volumes/backups and modify application behavior. Treat Docker access and backup decryption as privileged access, with separate accountable roles where staffing allows.
