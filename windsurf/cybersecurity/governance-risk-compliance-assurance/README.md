# Windsurf Governance, Risk, Compliance, and Assurance

This package defines a native Windsurf Cascade workspace for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance.

## Native Components

- `AGENTS.md`: directory-scoped Cascade instructions, role routing, controls, and completion criteria.
- `.windsurf/skills/*/SKILL.md`: reusable Cascade Skills for multi-step GRC work.
- `.windsurf/workflows/grc-decision-package.md`: manual workflow for final human decision preparation.
- `reference/NATIVE_SOURCES.md`: official Windsurf documentation checked during creation.

## Operating Model

Cascade uses `AGENTS.md` for directory-scoped behavior, Skills for model-selected procedures, and Workflows for manual slash-command runbooks. Repository custom agent files, subagent files, active MCP servers, hook scripts, external integrations, deployments, uploads, notifications, and live GRC writes are intentionally omitted.
