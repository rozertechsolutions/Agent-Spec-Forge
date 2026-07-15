# Warp Cybersecurity Security Architecture Engineering Rules

## Scope

These project rules apply only inside `warp/cybersecurity/security-architecture-engineering/` unless the user explicitly identifies external artifacts for review. Support security architecture governance, enterprise and solution architecture, identity and privileged access architecture, cloud and platform architecture, network and communications architecture, endpoint and workspace architecture, data protection, cryptography, key handling, restricted material architecture, container, Kubernetes, IaC, security tooling, automation design, and independent review.

Use Warp-native project rules and skills only:

- Native: `AGENTS.md` project rules.
- Native: `.warp/skills/<workflow>/SKILL.md` reusable workflow Skills.
- Conditionally native: `.warp/.mcp.json` project MCP config, only for a separately approved server that is necessary, contains no sensitive values, and remains subject to explicit Warp startup approval.
- Unsupported in this specialization: generic `agents/`, `subagents/`, `hooks/`, `mcp/`, `skills/`, `workflows/`, cloud schedules, cloud environments, integration triggers, Skills-as-Agents, agent profile files, live integrations, ticket creation, evidence upload, notification delivery, publication, deployment, and external autonomous execution.

Do not create `WARP.md`. Warp recognizes `AGENTS.md` as the default project rules file; `WARP.md` is backward compatibility and would take priority if both existed.

## Native Surface Verification

Verified against official Warp documentation on 2026-07-15: project rules, Skills, project MCP context, profiles and permissions, scheduled agents, and integrations.

## Responsibility Matrix

| Component | Native form | Exclusive scope | Write permission | Final review allowed |
| --- | --- | --- | --- | --- |
| `architecture-governance-agent` | Rule-defined Warp role | Governance model, reference architecture, standards mapping, decision records, review gates | Advisory by default | No |
| `enterprise-solution-architecture-agent` | Rule-defined Warp role | Enterprise, solution, platform, endpoint, and workspace design patterns | Advisory by default | No |
| `identity-cloud-network-agent` | Rule-defined Warp role | Identity, privileged access, cloud, platform, network, communications, and segmentation architecture | Advisory by default | No |
| `data-container-automation-agent` | Rule-defined Warp role | Data protection, cryptography, key handling, restricted material, container, Kubernetes, IaC, security tooling, and automation design | Advisory by default | No |
| `independent-architecture-reviewer` | Rule-defined Warp role | Evidence sufficiency, traceability, independence, unresolved limitations, residual risk, and final quality challenge | Read-only | Yes |

## Skill Routing

- Governance model, reference architecture, standards mapping, or decision record: `security-architecture-governance`.
- Enterprise, solution, platform, endpoint, or workspace pattern review: `enterprise-solution-patterns`.
- Identity, privileged access, cloud, platform, network, communications, data protection, or cryptography design: `identity-cloud-network-data-design`.
- Container, Kubernetes, IaC, security tooling, or automation review: `container-iac-automation-review`.
- Final challenge or readiness review: `independent-architecture-assurance`.

## Security And Human Control

Protect actual credential material, private keys, certificates, private URLs, production personal data, confidential third-party data, local environment files, and authoritative system records.

Never add real endpoints, sensitive values, private URLs, production data, or authenticated session material. Never activate, trust, approve, authenticate, start, or connect MCP servers or external integrations by default.

Require human approval before architecture approval, risk acceptance, access control change, production configuration, external write, notification, deployment, publication, or financial action.

## Completion Report

Every completed workflow must report official Warp documentation consulted; files created, modified, and omitted; native capabilities used and unsupported capabilities omitted; primary owner, reviewers, responsibility boundaries, and Skills used; security controls and MCP decision; static validation evidence; remaining limitations; and confirmation that no sensitive value, active integration, publication, external write, production change, destructive action, or out-of-scope modification occurred.

