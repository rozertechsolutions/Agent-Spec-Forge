# Native Cursor Sources

Official Cursor documentation checked on 2026-07-15:

- Cursor Docs: `https://docs.cursor.com/`
- Customize Cursor: `https://cursor.com/docs/customize-cursor`
- Rules: `https://docs.cursor.com/context/rules`
- Skills: `https://docs.cursor.com/context/skills`
- Agents: `https://docs.cursor.com/agent/custom-agents`
- MCP: `https://docs.cursor.com/context/mcp`

Implementation decision: use Cursor-native nested `AGENTS.md`, `.cursor/rules/*.mdc`, `.cursor/agents/*.md`, and `.cursor/skills/*/SKILL.md`. Omit active hooks, MCP servers, plugins, external connectors, commands, executable scripts, and live integrations because this package is static guidance only.
