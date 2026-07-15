# OpenCode Governance, Risk, Compliance, and Assurance

This package defines a native OpenCode workspace for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance.

## Native Components

- `AGENTS.md`: operating instructions, routing, controls, and completion criteria.
- `opencode.jsonc`: OpenCode project configuration with least-privilege permissions and inactive external integrations.
- `.opencode/agents/*.md`: five specialist subagents for the area.
- `.opencode/skills/*/SKILL.md`: reusable governance, risk, assurance, and independent review workflows.
- `reference/NATIVE_SOURCES.md`: official OpenCode documentation checked during creation.

## Operating Model

The primary OpenCode agent coordinates work and delegates to one specialist owner at a time. Review agents remain read-only and cannot approve their own work. External systems, MCP servers, plugins, scheduled actions, and executable hooks are intentionally omitted from this static package.

## Delivery Rules

Use this package for policy framework alignment, cyber risk registers, exception governance, control evidence, remediation tracking, third-party assurance, maturity reporting, and independent review. Keep outputs evidence-based, cite source artifacts, preserve user changes, and require human approval for any action that could change live systems, governance records, access rights, contractual commitments, or external communications.
