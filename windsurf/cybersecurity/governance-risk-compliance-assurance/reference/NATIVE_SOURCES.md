# Native Configuration Sources

These official sources define the native Windsurf Cascade mechanisms used by this package. Review them again before installation because product behavior can change.

- `https://docs.windsurf.com/windsurf/cascade/agents-md`
- `https://docs.windsurf.com/windsurf/cascade/skills`
- `https://docs.windsurf.com/windsurf/cascade/workflows`

## Decisions

- `AGENTS.md` is used because Cascade discovers directory-scoped `AGENTS.md` instructions.
- `.windsurf/skills/*/SKILL.md` is used because Cascade Skills are workspace-scoped under `.windsurf/skills/`.
- `.windsurf/workflows/*.md` is used for a manual final decision package workflow.
- Hooks are omitted because this package must be static and must not run generated scripts.
- MCP and integrations are omitted because no live external system is approved or required.
- Repository custom agent and subagent files are omitted because they are not a documented Windsurf repository-native surface for this specialization.
