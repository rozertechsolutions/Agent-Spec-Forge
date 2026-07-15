# Native Source Verification

Reviewed before creating this Kiro package on July 15, 2026.

## Official Kiro Documentation

- `https://kiro.dev/docs/` confirmed Kiro documentation areas for Specs, Hooks, Chat, Steering, MCP, privacy, IDE, and CLI.
- `https://kiro.dev/docs/steering/` confirmed workspace steering in `.kiro/steering/`, `AGENTS.md` support, and inclusion modes including `auto`.
- `https://kiro.dev/docs/skills/` confirmed Agent Skills in `.kiro/skills/<skill>/SKILL.md` with required `name` and `description` frontmatter.
- `https://kiro.dev/docs/cli/custom-agents/` confirmed custom agents as configurable Kiro CLI agents that control tools, permissions, and context.
- `https://kiro.dev/docs/cli/custom-agents/creating/` confirmed JSON custom-agent files, workspace directory `.kiro/agents/`, `tools`, `allowedTools`, `resources`, and `prompt` fields.
- `https://kiro.dev/docs/specs/` was considered; Specs are omitted because this package is a static reusable guidance and workflow package, not an executable feature plan.
- `https://kiro.dev/docs/hooks/` was considered; hooks are omitted because they can trigger commands or agent actions.
- `https://kiro.dev/docs/mcp/` was considered; MCP is omitted because this static package must not activate external connectors.

## Package Decisions

- Included native artifacts: `AGENTS.md`, `.kiro/steering/`, `.kiro/agents/`, and `.kiro/skills/`.
- Omitted native artifacts: `.kiro/hooks/`, `.kiro/specs/`, MCP configuration, executable scripts, Powers, and live integrations.
- Verification is static only: file presence, empty-file scan, secret-marker scan, JSON parse, and git diff review.
