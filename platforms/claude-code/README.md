# Claude Code

Surfaces:
- IDE integrations
- CLI

Claude Code uses the same core agent and project customizations across local surfaces, so shared
configuration is stored once under `common/`.

Native mechanisms demonstrated:
- Project memory/instructions: `CLAUDE.md`
- Project rules: `.claude/rules/*.md`
- Project subagents: `.claude/agents/*.md`
- Project skills: `.claude/skills/<skill>/SKILL.md`

Settings, hooks and `.mcp.json` are supported but are not required by this minimal example.

Official documentation:
- https://code.claude.com/docs/en/ide-integrations
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
