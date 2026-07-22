# Native Sources

Documentation review date: 2026-07-22.

Product surface: Cline IDE extension, TUI, CLI, workspace `.clinerules/` Rules, project `.cline/skills/` Skills, hooks when separately configured, Cline-managed read-only subagents, Agent Teams on supported SDK/CLI/Kanban surfaces, MCP configuration when separately approved, and approval controls.

Official source evidence checked or retained for this platform:

- https://docs.cline.bot/cline-overview
- https://docs.cline.bot/getting-started/config
- https://docs.cline.bot/features/subagents
- https://docs.cline.bot/cli/agent-teams
- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/core-workflows/using-commands
- https://github.com/cline/cline/blob/main/CHANGELOG.md
- https://docs.cline.bot/customization/hooks
- https://docs.cline.bot/mcp/mcp-overview
- https://docs.cline.bot/tools-reference/all-cline-tools
- https://docs.cline.bot/usage/cli-overview

Validation method:

- Inventory of `cline/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON, TOML, YAML where applicable.
- Reference resolution for retained repository-local Rules, Skills, and config files where applicable.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.
- Documentation comparison across Cline configuration, subagent, Agent Teams, Rules, Skills, commands, hooks, MCP, tools, CLI, changelog, and overview pages.

Current native facts recorded:

- Project paths: `cline/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: Cline documents `.clinerules/` as the primary workspace Rule format and documents project `.cline/skills/` Skills. The general configuration directory page also lists `.cline/rules/`, but the current Rules page and public repository README identify `.clinerules/` as the primary project Rule surface. This package therefore retains `.clinerules/<area>.md` as the single canonical always-on baseline for each area.
- Skills: project Skills are retained at `.cline/skills/<skill>/SKILL.md`. Enabled Skills can be triggered directly from chat as slash commands such as `/governance-policy-frameworks`, and Cline loads the matching `SKILL.md` instructions when triggered.
- Subagents: Cline-managed `use_subagents` workers are experimental, read-only research workers. They can read, list, search, run restricted read-only commands, and use Skills. They cannot write, use browser/web search, access MCP, or spawn nested subagents.
- Agent Teams: available for Cline SDK, CLI, and Kanban; not applicable to VS Code or JetBrains extensions according to the current Agent Teams page.
- Permissions: read-only/static by default; shell, network, MCP, connector, hosted tool, scanner, deployment, and production actions absent or denied unless a human explicitly configures them outside this baseline. Cline approval settings and auto-approval remain user/platform controls.
- Trust: repository-local configuration is effective only when the platform trusts or imports the project according to its current documentation.
- Precedence: the selected area workspace's `.clinerules/` baseline governs the selected work; platform-level README and this file provide package-wide evidence.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Unsupported descriptive-only metadata is not treated as a permission control.
- `.cline/workflows/*.md` files were removed. Current documentation exposes reusable procedures through native Skills and direct Skill slash-command invocation, while the configuration page only identifies workflows under global data locations.
- Duplicate area `AGENTS.md` and `.cline/rules/<area>.md` files were removed after migrating the complete baseline into `.clinerules/<area>.md`.
- `.cline/agents/*.md` files are omitted. The current official documentation checked for this remediation does not establish that path as a repository-native declarative custom-agent format for project-defined named subagents.
- Platform-specific frontmatter and config fields must be verified against current vendor documentation before use.
- For SDK packages, runtime API compatibility must be validated in an isolated environment without model calls before production use.
