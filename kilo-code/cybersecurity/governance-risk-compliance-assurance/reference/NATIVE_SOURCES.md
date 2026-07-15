# Native Source Verification

Reviewed before creating this Kilo Code package on July 15, 2026.

## Official Kilo Code Documentation

- `https://kilocode.ai/docs/llms.txt` confirmed the current documentation index and raw page list.
- `https://kilocode.ai/docs/customize/agents-md` confirmed `AGENTS.md` support and loading behavior.
- `https://kilocode.ai/docs/customize/custom-rules` confirmed `kilo.jsonc` `instructions` entries and `.kilo/rules/` Markdown rule files.
- `https://kilocode.ai/docs/customize/custom-subagents` confirmed project subagents in `.kilo/agents/*.md`, frontmatter fields, modes, permissions, and task delegation.
- `https://kilocode.ai/docs/customize/skills` confirmed Agent Skills in `.kilo/skills/<skill>/SKILL.md` with `name` and `description` frontmatter.
- `https://kilocode.ai/docs/customize/workflows` confirmed slash commands in `.kilo/commands/`; commands are omitted here to avoid duplicating the Skill workflows.
- `https://kilocode.ai/docs/customize/context/kilocodeignore` confirmed `.kilocodeignore` and permission-based file access controls.
- `https://kilocode.ai/docs/automate/mcp/overview` was considered; MCP is omitted because this static package must not activate external connectors.
- `https://kilocode.ai/docs/automate/extending/plugins` was considered; plugins are omitted because JavaScript plugins would introduce executable behavior.

## Package Decisions

- Included native artifacts: `AGENTS.md`, `kilo.jsonc`, `.kilocodeignore`, `.kilo/rules/`, `.kilo/agents/`, and `.kilo/skills/`.
- Omitted native artifacts: `.kilo/commands/`, `.kilo/plugins/`, MCP server configuration, executable scripts, and live integrations.
- Verification is static only: file presence, empty-file scan, secret-marker scan, and git diff review.
