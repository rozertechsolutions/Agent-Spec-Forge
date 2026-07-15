# Native Source Verification

Verified on 2026-07-15 against official OpenCode documentation:

- Rules documentation: `https://opencode.ai/docs/rules/`
- Agents documentation: `https://opencode.ai/docs/agents/`
- Configuration documentation: `https://opencode.ai/docs/config/`
- Plugins documentation: `https://opencode.ai/docs/plugins/`
- MCP servers documentation: `https://opencode.ai/docs/mcp-servers/`

## Decisions

- `AGENTS.md` is used for project instructions because OpenCode documents project-level rule files and instruction loading.
- `opencode.jsonc` is used because OpenCode documents project configuration and JSONC support.
- `.opencode/agents/*.md` is used because OpenCode documents Markdown agent files with frontmatter and `mode: subagent`.
- `.opencode/skills/*/SKILL.md` is used because the official configuration documentation identifies `.opencode/skills` as a native configuration directory, and this repository already uses that native pattern for OpenCode packages.
- Active plugins and MCP servers are omitted because this package is static and must not enable external integrations.

## Limitation

The direct Agent Skills page URL checked during creation returned 404. Skill files therefore follow the existing repository OpenCode convention and only use simple frontmatter plus Markdown process instructions.
