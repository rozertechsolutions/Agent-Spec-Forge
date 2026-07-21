# Native Sources

Documentation review date: 2026-07-21.

Product surface: Kilo Code 1.0+ VS Code extension and CLI, using project `kilo.jsonc`, `AGENTS.md`, `.kilo/agents`, `.kilo/commands`, `.kilo/skills`, `.kilo/rules`, `.kilocodeignore`, permissions, and MCP configuration.

## Official source checks

### Check 1 - Current reference documentation

- Kilo Code CLI: `https://kilo.ai/docs/code-with-ai/platforms/cli`
- Custom Modes: `https://kilo.ai/docs/customize/custom-modes`
- Custom Subagents: `https://kilo.ai/docs/customize/custom-subagents`
- Agent Permissions: `https://kilo.ai/docs/customize/agent-permissions`
- Custom Rules: `https://kilo.ai/docs/customize/custom-rules`
- Custom Instructions: `https://kilo.ai/docs/customize/custom-instructions`
- AGENTS.md: `https://kilo.ai/docs/customize/agents-md`
- Workflows: `https://kilo.ai/docs/customize/workflows`
- Skills: `https://kilo.ai/docs/customize/skills`
- `.kilocodeignore`: `https://kilo.ai/docs/customize/context/kilocodeignore`
- MCP: `https://kilo.ai/docs/automate/mcp/using-in-kilo-code`

### Check 2 - Official release or product status source

- Current Kilo Code documentation states the all-new extension is rebuilt on Kilo CLI and the CLI page applies to Kilo version 1.0 and later.
- Current workflow documentation states workflows are slash commands stored in `.kilo/commands/`; legacy workflow layouts are migrated.
- Current custom-modes documentation states legacy `.kilocodemodes` and `custom_modes.yaml` are legacy migration surfaces.

### Check 3 - Official package, repository, or schema evidence

- Kilo source and issue repository referenced from official docs: `https://github.com/Kilo-Org/kilocode`
- Official configuration documentation records project config locations as `./kilo.json[c]`, legacy `./opencode.json[c]`, or `./.kilo/` config.
- Official docs define current custom agent frontmatter and config fields, permissions, task delegation controls, Skills discovery, commands, MCP config, and `.kilocodeignore` behavior.
- No Kilo CLI package was installed or executed for this remediation.

## Current native facts

- Project path: open one area as the workspace/project root, for example `kilo-code/cybersecurity/security-architecture-engineering/`.
- Configuration: project `kilo.jsonc` is valid JSONC and includes `$schema`, `instructions`, `permission`, and empty `mcp`.
- Instructions: Kilo auto-discovers `AGENTS.md` and also loads files listed in `kilo.jsonc` `instructions`.
- Agents: project custom agents are Markdown files under `.kilo/agents/*.md`; supported frontmatter includes `description`, `mode`, `model`, `permission`, `hidden`, `steps`, `temperature`, `top_p`, `color`, and `disable`.
- Modes: retained Cybersecurity agents use `mode: subagent`.
- Permissions: retained subagents allow read/search and deny edit, write, bash, and task delegation. Area `kilo.jsonc` files deny destructive Git/remove commands and ask before project writes.
- Commands/workflows: current slash-command workflow files live under `.kilo/commands/*.md` and may include optional YAML frontmatter with `description`.
- Skills: project Skills live under `.kilo/skills/<skill>/SKILL.md`.
- MCP: current MCP servers would be declared under top-level `mcp`, but the retained config uses an empty object and no server entries.
- `.kilocodeignore`: still supported; Kilo migrates patterns into permission deny behavior for read/edit.

## Removed or deprecated field handling

- Removed `.kilo/workflows/` directories by moving retained workflow prompt files to current `.kilo/commands/` locations.
- Removed exact duplicate `.kilo/rules/<area>.md` files that repeated the area `AGENTS.md`; Kilo already discovers `AGENTS.md`.
- Removed unreferenced legacy appsec Skills `independent-appsec-assurance`, `sdlc-requirements-threat-modeling`, `supply-chain-ci-release-assurance`, and `testing-findings-psirt-coordination`; retained Skills cover the current appsec workflows.
- No legacy `.kilocodemodes`, `custom_modes.yaml`, `.kilocode/rules`, or metadata-only `kilo.jsonc` files remain in this Cybersecurity package.

## Validation method

- Inventoried all eight `kilo-code/cybersecurity/<area>/` directories.
- Parsed every `kilo.jsonc` as JSONC.
- Parsed Markdown/YAML frontmatter for agents, commands, and Skills.
- Verified all 41 agents use `mode: subagent` and current permission keys.
- Verified every command is under `.kilo/commands/`, not `.kilo/workflows/`.
- Verified retained `.kilo/rules` entries are referenced from `kilo.jsonc`.
- Verified no MCP server entries, hooks, provider credentials, cloud connectors, scanner integrations, or live-action workflows are present.

## Reasons for omitted mechanisms

- No MCP servers are included because this package must not connect external systems by default.
- No provider, proxy, model, or BYOK configuration is included because those values are user/organization-dependent and may contain secrets.
- No legacy mode files are included because current Kilo uses Markdown agents and `kilo.jsonc`.
- No CI, Cloud Agent, Kilo Connect, or remote automation configuration is included because this repository package is local/static and must not create production or hosted automation.
