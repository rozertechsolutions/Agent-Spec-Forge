# Native Sources

Documentation review date: 2026-07-21.

Product surface: Qwen Code CLI project context, `QWEN.md`, `AGENTS.md`, project settings in `.qwen/settings.json`, custom subagents, Agent Skills, custom commands, approval modes, hooks settings, MCP settings, and folder trust.

Official source evidence checked or retained for this platform:

- Qwen Code repository: https://github.com/QwenLM/qwen-code
- Qwen Code configuration settings: https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/
- Qwen Code custom subagents: https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- Qwen Code Agent Skills: https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- Qwen Code approval modes: https://qwenlm.github.io/qwen-code-docs/en/users/features/approval-mode/
- Qwen Code file-system tools: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/file-system/
- Qwen Code tools overview and confirmations: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction/
- Qwen Code hooks: https://qwenlm.github.io/qwen-code-docs/en/users/features/hooks/
- Qwen Code commands: https://qwenlm.github.io/qwen-code-docs/en/users/features/commands/
- Qwen Code MCP: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/

Validation method:

- Inventory of `qwen-code/cybersecurity/` files and native support directories.
- Static syntax parsing for JSON and Markdown/YAML frontmatter.
- Reference resolution for retained commands, Skills, agents, instructions, and settings files.
- Native field review against current Qwen Code docs for custom agents, settings, approval modes, tools, hooks, MCP, and Skills.
- Removal of redundant area-level source copies after this platform-wide source file replaced them.

Current native facts recorded:

- Project paths: `qwen-code/cybersecurity/<area>/` for all eight Cybersecurity areas.
- Discovery: launch Qwen Code from `qwen-code/cybersecurity/<area>/` so the area's `QWEN.md`, `AGENTS.md`, `.qwen/settings.json`, `.qwen/agents/*.md`, `.qwen/skills/<name>/SKILL.md`, and `.qwen/commands/*.md` are the active project package.
- Custom agent fields used: `name`, `description`, `model`, `approvalMode`, `tools`, and `disallowedTools`.
- Approval modes: `approvalMode: plan` is used on cybersecurity custom agents for analyze-only behavior. Project settings keep `tools.approvalMode` at `default`, requiring approval for sensitive operations outside custom plan-mode agents.
- Native read-only agent tools used: `read_file`, `grep_search`, `glob`, and `list_directory`.
- Native dangerous tools denied in custom agents: `write_file`, `edit`, `notebook_edit`, `run_shell_command`, and `web_fetch`.
- Skills: area Skills are retained under `.qwen/skills/<skill-name>/SKILL.md`; they are not declared through custom-agent `skills` frontmatter.
- Settings: retained `.qwen/settings.json` files use documented structured settings such as `general`, `privacy`, `model`, `memory`, `tools`, `permissions`, `slashCommands`, `mcp`, `security.folderTrust`, `telemetry`, `experimental`, and `disableAllHooks`.
- Hooks: hooks are not provided by this package, and retained settings set `disableAllHooks` to `true`.
- MCP: no MCP server configuration is provided; retained settings use empty `mcp.allowed` and wildcard `mcp.excluded` lists.
- Trust: repository-local configuration is effective only when Qwen Code trusts the project and the session is launched or imported according to current documentation.
- Precedence: documented Qwen Code precedence allows user settings, environment variables, and command-line arguments to override project defaults. The user must confirm `/status` and approval mode before use.
- Omitted mechanisms: fake MCP servers, generated live hooks, external endpoints, credentials, cloud actions, scanners, hosted tools, and deployment automation are intentionally omitted.

Removed or deprecated field handling:

- Removed descriptive-only settings fields that have no documented Qwen Code permission effect: `staticOnly`, `externalIntegrationsEnabled`, `liveSecurityActionsEnabled`, `activeTestingEnabled`, and `productionActionsEnabled`.
- Replaced copied non-native agent tool labels `Read`, `Grep`, and `Glob` with documented Qwen Code tool identifiers.
- Did not add unsupported `readonly` or agent-level `skills` fields.
- Removed orphaned duplicate app-security Skill directories that were not referenced by commands, agents, README, or native discovery requirements after the retained Skills preserved the professional workflow coverage.
