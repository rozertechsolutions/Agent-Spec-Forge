# Mistral Vibe Cybersecurity GRC Assurance Instructions

These instructions apply only inside `mistral-vibe/cybersecurity/governance-risk-compliance-assurance/` and cybersecurity GRC artifacts intentionally placed below it. Keep work scoped to governance, policy frameworks, cyber risk, exceptions, assurance evidence, audit readiness support, third-party risk, maturity reporting, and remediation oversight.

Start Vibe with this directory as the working directory so project `.vibe/` configuration, agents, prompts, and Skills are discovered. Do not start from a descendant and assume ancestor configuration is loaded.

## Native Surface

- Vibe Code project configuration: `.vibe/config.toml`.
- User-facing coordinator: `.vibe/agents/grc-coordinator.toml` with `.vibe/prompts/grc-coordinator.md`.
- Delegation-only subagents: `.vibe/agents/*-agent.toml` and `.vibe/agents/independent-assurance-reviewer.toml`.
- Reusable procedures: `.vibe/skills/*/SKILL.md`.
- Official docs checked on July 15, 2026: Vibe mode selection, Work Skills, Code CLI agents, Code CLI configuration, and Code CLI Skills.

## Scope and Boundaries

- Do not configure providers, models, connectors, MCP servers, hooks, scripts, remote sessions, automation schedules, or external tools.
- Do not read, copy, log, expose, or embed secrets, credentials, private audit evidence, customer data, employee data, vendor contracts, vulnerability details, or regulator communications unless the user explicitly supplies and authorizes the material for the task.
- Do not approve policy, accept risk, waive controls, certify compliance, close audit findings, approve vendors, publish, deploy, submit filings, spend money, or perform destructive operations.
- Treat unsupported evidence as unavailable. Never turn missing evidence into a pass.

## Delegation

Use only these project subagents:

- `governance-policy-frameworks-agent`
- `cyber-risk-exceptions-agent`
- `assurance-evidence-remediation-agent`
- `third-party-maturity-reporting-agent`
- `independent-assurance-reviewer`

Assign exactly one primary owner per deliverable. Implementation and drafting roles do not perform their own independent final review.

## Completion Standard

Every result must list sources inspected, assumptions, evidence state, approval needs, unavailable context, and whether independent review was completed or remains required. Formal claims require human approval.
