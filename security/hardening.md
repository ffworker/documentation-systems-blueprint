# Hardening and threat review

| Risk | Control | Verification |
| --- | --- | --- |
| First visitor claims initial owner | Bootstrap on loopback/restricted network | Owner established before wider ingress |
| Unauthorized content exposure | Group boundaries, share review, negative tests | Search/file/export access tests |
| Host or Docker compromise | Patched dedicated host, restricted admin access | Host baseline and access review |
| Database/Redis exposure | No published ports; private data network | Review rendered Compose ports and network reachability |
| Backup theft or deletion | Encryption, independent storage, separate credentials | Restore and retention/deletion test |
| Malicious or compromised dependency | Approved digests, advisory review, update process | Release evidence and vulnerability triage |
| Forgotten legacy instance | Restricted read-only period with removal date | Retirement checklist signed |

Use HTTPS for network access, restrict ingress to intended audiences, test mail security and bound log growth. Backups and exports retain the classification of the source content. Assess attachment scanning, resource limits, abuse protection and outbound integration restrictions according to exposure.

Do not blindly set read-only filesystems, arbitrary users or capability rules on third-party containers without testing required write paths and startup behavior. Document any exception to the host/container baseline with a reason and review date. The reference network layout is one control, not a complete hardened operating system.
