# Antigravity

Surfaces:
- IDE
- CLI

`common/` contains workspace customizations shared by Antigravity IDE and CLI.
`CLI/` additionally shows the CLI-only user settings file.

Native mechanisms demonstrated:
- Workspace Rules: `.agents/rules/`
- Agent Skills: `.agents/skills/<skill>/SKILL.md`
- Workspace MCP configuration: `.agents/mcp_config.json`
- CLI settings: `~/.gemini/antigravity-cli/settings.json`

Hooks and plugins are supported but are intentionally omitted from this minimal example because
the example does not require lifecycle automation or packaging.

Official documentation:
- https://antigravity.google/docs/ide/rules
- https://antigravity.google/docs/skills
- https://antigravity.google/docs/mcp
- https://antigravity.google/docs/hooks
- https://antigravity.google/docs/cli/settings
