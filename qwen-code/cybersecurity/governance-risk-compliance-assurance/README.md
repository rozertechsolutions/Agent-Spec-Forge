# Qwen Code Governance, Risk, Compliance, and Assurance

This package defines a native Qwen Code workspace for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance.

## Native Components

- `QWEN.md`: project context, routing, controls, and completion contract.
- `.qwen/settings.json`: project settings that keep automation conservative.
- `.qwen/agents/*.md`: five focused Qwen Code subagents.
- `.qwen/skills/*/SKILL.md`: four reusable Qwen Code Skills.
- `reference/NATIVE_SOURCES.md`: official Qwen Code documentation checked during creation.

## Operating Model

The main Qwen Code session acts as coordinator. It applies the relevant Skill, assigns exactly one primary specialist per work unit, and invokes independent review before presenting governance, risk, assurance, third-party, maturity, or committee material as complete.

Hooks, MCP servers, extensions, scheduled tasks, daemon mode, SDK code, live integrations, uploads, notifications, and external writes are intentionally omitted from this static package.
