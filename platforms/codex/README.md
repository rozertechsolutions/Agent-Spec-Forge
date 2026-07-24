# Codex

Surfaces:
- IDE extension
- CLI

Shared repository configuration is stored once under `common/`.

Native mechanisms demonstrated:
- Project instructions: `AGENTS.md`
- Project custom agents: `.codex/agents/*.toml`
- Project Skills: `.agents/skills/<skill>/SKILL.md`
- Project command rules: `.codex/rules/*.rules`
- Project configuration: `.codex/config.toml`

Hooks and MCP are supported through Codex configuration but are omitted because this minimal
example does not require them.

Official documentation:
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/subagents
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/config-reference
- https://learn.chatgpt.com/codex/agent-configuration/rules
- https://learn.chatgpt.com/codex/hooks
