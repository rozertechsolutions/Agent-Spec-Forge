# Native Source Verification

Official sources checked on 2026-07-15:

- Cline config: `https://docs.cline.bot/getting-started/config`
- Cline rules: `https://docs.cline.bot/customization/cline-rules`
- Cline Skills: `https://docs.cline.bot/customization/skills`
- Cline subagents: `https://docs.cline.bot/features/subagents`

## Decisions

- Workspace rule instructions are represented with a Cline rule file.
- Project Skills are represented under `.cline/skills/<skill-name>/SKILL.md`.
- Hooks, MCP, plugins, cron, connectors, command permissions, and executable artifacts are omitted because this static package must not run code or connect tools.
