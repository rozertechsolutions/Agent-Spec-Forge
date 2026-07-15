# Cursor Cybersecurity Governance, Risk, Compliance & Assurance

This package defines a Cursor-native Cybersecurity GRC & Assurance workspace using nested instructions, project rules, subagents, and Agent Skills.

## Native Components

- `AGENTS.md`: area-level coordinator instructions.
- `.cursor/rules/grc-governance.mdc`: always-applied project rule for scope, safety, and evidence discipline.
- `.cursor/agents/*.md`: specialist subagents with deterministic ownership.
- `.cursor/skills/*/SKILL.md`: reusable GRC workflows packaged as Agent Skills.
- `reference/NATIVE_SOURCES.md`: official Cursor sources and native/omitted component decisions.

No hooks, MCP servers, commands, plugins, scripts, or live integrations are included.

## Use

Ask Cursor Agent to work inside this directory and select the relevant Skill or subagent by task:

- Governance, policy, control mapping, compliance gaps: `governance-policy-frameworks`.
- Risk statements, risk register, treatments, exceptions, remediation governance: `risk-exceptions-remediation`.
- Evidence, assurance readiness, findings, third-party risk, maturity, executive reporting: `assurance-third-party-reporting`.
- Independent quality review: `independent-assurance-review`.

All outputs require explicit evidence provenance, assumptions, limitations, residual risk, and human approval state.

