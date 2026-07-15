# Native Configuration Sources

Reviewed before creating this local package on July 15, 2026.

## Official Sources

- `https://modelcontextprotocol.io/docs/getting-started/intro` confirmed MCP is a standard for connecting AI applications to external systems. MCP is omitted here because this package must not activate external connectors.
- `https://agentskills.io/specification` confirmed Agent Skills use a directory with `SKILL.md` and optional executable `scripts/`, `references/`, and `assets/`. This local package uses YAML skill manifests instead of runnable Skill directories, and records the external spec only as a reference for skill-style decomposition.

## Package Decisions

- Included native artifacts: `README.md`, `SPECIFICATION.md`, `local.yaml`, `agents/`, `subagents/`, `skills/`, `workflows/`, `policies/`, `tools/`, `schemas/`, and `reference/`.
- Omitted native artifacts: provider examples, MCP server examples, executable hooks, scripts, daemons, commands, active integrations, and runtime configuration.
- Verification is static only: file presence, empty-file scan, secret-marker scan, and git diff review.
