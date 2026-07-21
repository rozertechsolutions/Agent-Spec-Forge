# Native Sources

Documentation review date: 2026-07-21.

Product surface: Windsurf/Devin Desktop Cascade plus Devin Local/CLI. This package uses `AGENTS.md`, Windsurf workspace Skills, and Devin project configuration only.

## Official sources checked

- Windsurf/Devin Desktop AGENTS.md documentation: `https://docs.windsurf.com/windsurf/cascade/agents-md`
- Windsurf/Devin Desktop Memories and Rules documentation: `https://docs.windsurf.com/windsurf/cascade/memories`
- Windsurf/Devin Desktop Skills documentation: `https://docs.windsurf.com/windsurf/cascade/skills`
- Windsurf/Devin Desktop Hooks documentation: `https://docs.windsurf.com/windsurf/cascade/hooks`
- Windsurf/Devin Desktop MCP documentation: `https://docs.windsurf.com/windsurf/cascade/mcp`
- Devin CLI extensibility overview: `https://docs.devin.ai/cli/extensibility`
- Devin CLI configuration file reference: `https://docs.devin.ai/cli/reference/configuration/config-file`
- Devin CLI configuration precedence: `https://docs.devin.ai/cli/reference/configuration/global-vs-local`
- Devin CLI configuration import reference: `https://docs.devin.ai/cli/reference/configuration/read-config-from`
- Devin CLI permissions reference: `https://docs.devin.ai/cli/reference/permissions`
- Devin CLI commands and flags: `https://docs.devin.ai/cli/reference/commands`
- Devin CLI stable changelog: `https://docs.devin.ai/cli/changelog/stable`
- Devin Local Agent documentation: `https://docs.devin.ai/desktop/devin-local`

## Current native facts

- Cascade automatically discovers `AGENTS.md` or `agents.md` in the workspace and scopes it by location.
- Cascade Rules use `.devin/rules/*.md` as the preferred workspace path and `.windsurf/rules/*.md` as a fallback. The legacy root `.windsurfrules` file is still read.
- Cascade workspace Skills live at `.windsurf/skills/<skill-name>/SKILL.md` and require `name` and `description` frontmatter.
- Cascade hooks are JSON files at system, user, or workspace levels. Workspace hooks use `.windsurf/hooks.json`. This package intentionally ships no hooks.
- Cascade MCP is configured outside this package and requires user or administrator action. No MCP servers are included.
- Devin CLI project configuration lives at `.devin/config.json`; `.devin/config.local.json` is a local, uncommitted override.
- Devin CLI project config supports `permissions`, `mcpServers`, `read_config_from`, and hooks. User-only options are not used in this project config.
- Devin CLI permission syntax supports scope matchers such as `Read(**)`, `Write(**)`, `Exec(prefix)`, `Fetch(pattern)`, tool names such as `read`, `edit`, `grep`, `glob`, `exec`, and MCP tool patterns such as `mcp__*`.
- Devin CLI merges permissions with deny before ask before allow; organization and session permissions can take precedence over project config.
- Devin CLI can import Windsurf rules and Skills through `read_config_from.windsurf`; Windsurf workflows are not imported as Skills.
- Devin Local is a preview local agent surface in Devin Desktop and shares the Devin CLI harness.

## Retained project paths

- `windsurf/cybersecurity/.devin/config.json`
- `windsurf/cybersecurity/<area>/AGENTS.md`
- `windsurf/cybersecurity/<area>/.windsurf/skills/<skill-name>/SKILL.md`
- `windsurf/cybersecurity/README.md`
- `windsurf/cybersecurity/NATIVE_SOURCES.md`

## Configuration and permission behavior

The retained `.devin/config.json` uses documented project fields only:

- `permissions.allow`: static read/search/glob permissions.
- `permissions.ask`: writes and edits require explicit approval.
- `permissions.deny`: shell execution, fetch, MCP tools, environment-file writes, and parent-directory writes are denied.
- `mcpServers`: empty project MCP map.
- `read_config_from`: Windsurf import enabled; Cursor and Claude imports disabled to avoid unintended cross-platform imports.

Cascade still remains subject to the user's workspace trust, account plan, product settings, and organization controls. This repository does not override product-level approvals or administrator policies.

## Removed, omitted, or deprecated mechanisms

- No repository-defined Windsurf custom-agent files are included because the current documented repository mechanisms for this package are `AGENTS.md`, Rules, Skills, hooks, MCP, and Devin Local/CLI extensibility.
- No `.devin/agents/*/AGENT.md` files are included. Devin custom subagent profiles are currently experimental and were not required for this static cybersecurity baseline.
- No `.windsurf/hooks.json` is included because hooks execute shell commands and this package does not need executable hooks.
- No MCP servers, credentials, connectors, scanners, cloud-agent schedules, app deploys, or live integrations are included.
- No `.windsurfrules` file is included because `AGENTS.md` provides the retained directory-scoped instruction channel without a duplicate legacy rule file.

## Validation method

- Inventory of all eight `windsurf/cybersecurity/<area>/` packages.
- JSON parsing for `.devin/config.json`.
- Markdown frontmatter validation for all retained `SKILL.md` files.
- Native path review for `AGENTS.md`, `.windsurf/skills/`, and `.devin/config.json`.
- Duplicate and reachability review for retained Markdown files.
- Repository hygiene checks for temporary environments, caches, empty files, empty directories, and committed credentials.

No generated agent, model call, Devin session, Cascade session, hook, MCP connection, scanner, live target, or production action was executed during validation.
