# Kiro IDE - Software Development

This directory configures Kiro IDE for the Software Development specialization.

## Native Surfaces

- `.kiro/steering/` is authoritative for the primary Kiro agent, which acts as Software Development Lead.
- `.kiro/agents/` contains seven Kiro IDE custom agents in Markdown frontmatter format; there is intentionally no Lead custom agent.
- `.kiro/skills/` contains static reusable Skills.
- `docs/workflows/` contains auxiliary workflow references, not a Kiro spec or executable workflow engine.

## Safety Model

Specialists report to the primary Kiro agent, cannot recursively delegate, cannot expand scope, and cannot claim final completion. Reviewers and planners are read-only through `tools: ["read"]`. The implementation specialist uses `tools: ["read", "write"]` for approval-gated workspace editing and has no shell, web, MCP, hook, deployment, publication, signing, release, credentials, or Git mutation authority.

`.kiro/specs/`, Kiro CLI JSON agents, hooks, and MCP are intentionally absent. Runtime loading and command execution have not been performed from this repository package.
