# Kiro

Surfaces:
- IDE
- CLI

Kiro shares Steering, Skills and MCP workspace configuration, but IDE and CLI custom agents use
different native formats. Therefore agent examples are surface-specific rather than duplicated in
`common/`.

Native mechanisms demonstrated:
- Shared Steering: `.kiro/steering/*.md`
- Shared Skills: `.kiro/skills/<skill>/SKILL.md`
- Shared MCP: `.kiro/settings/mcp.json`
- IDE custom agents: `.kiro/agents/*.md`
- CLI custom agents: `.kiro/agents/*.json`
- CLI user settings: `~/.kiro/settings/cli.json`

Official documentation:
- https://kiro.dev/docs/steering/
- https://kiro.dev/docs/skills/
- https://kiro.dev/docs/custom-agents/
- https://kiro.dev/docs/cli/custom-agents/
- https://kiro.dev/docs/cli/custom-agents/configuration-reference/
- https://kiro.dev/docs/cli/reference/settings/
