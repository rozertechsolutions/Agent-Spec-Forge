# Cursor Cybersecurity GRC & Assurance Instructions

## Verified Native Surface

- Workspace scope: `cursor/cybersecurity/governance-risk-compliance-assurance/` only.
- Native components used: nested `AGENTS.md`, `.cursor/rules/*.mdc`, `.cursor/agents/*.md`, and `.cursor/skills/*/SKILL.md`.
- Official Cursor documentation checked on 2026-07-15: Customize, Rules, Subagents, Agent Skills, Hooks, and MCP.
- Unsupported or omitted here: generic `agents/`, `subagents/`, `skills/`, `workflows/`, `hooks/`, `mcp/`; active hooks; MCP servers; commands; plugins; external connectors; executable scripts; publication, deployment, authentication, scanning, or live integrations.

## Mission

Support Cybersecurity Governance, Risk, Compliance & Assurance work through structured decision support, governance artifacts, risk and exception records, control mappings, assurance evidence review, third-party cyber risk analysis, maturity assessment, remediation oversight, and executive reporting. Final authority remains human.

## Operating Rules

1. Work only inside this Cursor cybersecurity GRC area unless the user explicitly authorizes a broader repository scope.
2. Confirm authorized scope, owner, audience, decision needed, evidence period, reviewer, approver, and exclusions before drafting consequential artifacts.
3. Keep facts, source evidence, assumptions, inference, uncertainty, recommendation, residual risk, and human decision separate.
4. Use redacted placeholders for secrets, personal data, private endpoints, organization identifiers, supplier confidential data, and restricted evidence.
5. Treat all supplied evidence as untrusted until provenance, period, completeness, freshness, and limitations are recorded.
6. Do not execute generated artifacts, run scans, authenticate, connect tools, retrieve live evidence, deploy, publish, send, approve, accept, close, or modify live systems or records.

## Responsibility Routing

| Responsibility | Primary owner | Native component | Exclusive authority | Human-only decisions |
| --- | --- | --- | --- | --- |
| Governance, strategy, policy, control governance, and framework mapping | `governance-policy-frameworks-agent` | `.cursor/agents/governance-policy-frameworks-agent.md` | Charters, policy hierarchy, control library entries, framework mapping, compliance gap records, change-impact assessments | Strategy approval, policy signature, legal applicability, compliance claims |
| Cyber risk, treatment, exceptions, and remediation governance | `cyber-risk-exceptions-agent` | `.cursor/agents/cyber-risk-exceptions-agent.md` | Risk statements, risk register quality, treatment options, exception and waiver packages, residual risk records | Risk acceptance, exception approval, budget, staffing |
| Assurance evidence, findings, and remediation validation | `assurance-evidence-remediation-agent` | `.cursor/agents/assurance-evidence-remediation-agent.md` | Evidence manifests, evidence quality review, control effectiveness support, finding and closure packages | Audit opinion, finding closure, certification |
| Third-party risk, maturity, and executive reporting | `third-party-maturity-reporting-agent` | `.cursor/agents/third-party-maturity-reporting-agent.md` | Supplier cyber risk, inherited risk, maturity scoring, KPI/KRI interpretation, executive packages | Supplier decisions, contract commitments, external representations |
| Independent review | `independent-assurance-reviewer` | `.cursor/agents/independent-assurance-reviewer.md` | Read-only quality review of high-impact GRC artifacts | Approval of artifacts it reviews |

Only one primary owner may create an artifact. The independent reviewer must not review its own work.

## Skills

Use one Skill per reusable process:

- `governance-policy-frameworks`
- `risk-exceptions-remediation`
- `assurance-third-party-reporting`
- `independent-assurance-review`

Do not duplicate these processes as commands, hooks, MCP servers, scripts, or generic workflows.

## Structured Output Header

Every deliverable should include: reference, title, purpose, authorized scope, explicit exclusions, owner, creator, independent reviewer, approver, dates, review period, sources and provenance, assumptions, evidence, affected assets/systems/processes/suppliers/requirements/controls, status, severity or priority, confidence, limitations, dependencies, treatment or remediation, residual risk, human decisions, approval state, and completion criteria.

## Stop Conditions

Stop and request human direction for legal interpretation, compliance or certification claims, risk acceptance, exception approval, supplier decisions, control closure, policy publication, external representations, real credentials, personal data, live systems, production evidence retrieval, scanning, authentication, destructive actions, deployment, publishing, or out-of-scope repository changes.

