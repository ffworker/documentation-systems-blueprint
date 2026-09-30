# Logical RBAC contract

These are blueprint roles, not claims about exact vendor role names. Map each to the selected version/edition and test effective permissions.

| Logical role | Read | Edit | Approve/publish | Manage space members | Platform administration |
| --- | --- | --- | --- | --- | --- |
| Reader | Assigned content | No | No | No | No |
| Contributor | Assigned content | Assigned drafts/content | Workflow-dependent | No | No |
| Content owner | Owned domain | Owned domain | Yes, by agreed review process | If explicitly delegated | No |
| Platform administrator | Operationally privileged | As assigned | Not a substitute for content approval | Yes | Yes |

Where the product cannot enforce draft/approval separation, use restricted staging spaces and a documented second-person review. Record that this is a procedural control; do not present it as built-in RBAC.

Test reader edit denial, unrelated-space denial, direct attachment denial, search results, exports, shared links, token access and offboarding. Check both UI and direct URL/API behavior where supported. Store test evidence privately; publish only synthetic examples. A failed mandatory negative test blocks acceptance.
