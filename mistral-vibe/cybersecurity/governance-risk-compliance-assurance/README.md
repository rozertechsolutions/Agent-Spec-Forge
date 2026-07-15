# Mistral Vibe Cybersecurity GRC Assurance

This package configures Mistral Vibe Code for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance.

## Native Entry Points

- `AGENTS.md`
- `.vibe/config.toml`
- `.vibe/agents/*.toml`
- `.vibe/prompts/*.md`
- `.vibe/skills/*/SKILL.md`
- `reference/NATIVE_SOURCES.md`

## Safe Defaults

- No model, provider, endpoint, credential, MCP server, connector, telemetry override, hook, script, or external integration is configured.
- The default coordinator can read, search, use Skills, maintain todo state, ask questions, and request read-only subagent delegation.
- Subagents are read-only and cannot ask the user questions, edit files, run shell commands, connect tools, accept risk, certify compliance, or approve their own work.
- Formal policy approval, risk acceptance, audit sign-off, external reporting, vendor decisions, and compliance claims require a human accountable owner.
