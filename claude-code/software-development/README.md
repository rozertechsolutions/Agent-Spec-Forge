# Claude Code - Software Development

This directory configures Claude Code for the Software Development specialization.

## Native Surfaces

- `CLAUDE.md` makes the primary Claude Code session the Software Development Lead.
- `.claude/agents/` contains seven specialist subagents; there is intentionally no Lead subagent.
- `.claude/settings.json` denies destructive, Git-mutating, publication, deployment, signing, package publication, secret-read, sensitive-key, and external-authentication actions.
- `.claude/skills/` contains static reusable procedures.
- `docs/workflows/` contains auxiliary workflow references, not auto-executed commands.

## Safety Model

The primary session plans, routes, requests approvals, aggregates evidence, and reports completion. Specialists return bounded evidence to the primary session, cannot recursively delegate, cannot expand scope, and cannot claim final completion. Review specialists are read-only. The implementation specialist is limited to read/search plus approved workspace edits and has no Bash, network, MCP, Git, deployment, publication, signing, or release authority.

Runtime loading and command execution have not been performed from this repository package.
