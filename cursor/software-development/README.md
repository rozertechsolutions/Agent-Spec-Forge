# Cursor - Software Development

This directory configures Cursor for the Software Development specialization.

## Native Surfaces

- `AGENTS.md` makes the primary Cursor Agent the Software Development Lead.
- `.cursor/rules/` contains Cursor project rules.
- `.cursor/skills/` contains static reusable Skills.
- `docs/workflows/` contains auxiliary workflow references, not a guaranteed native workflow engine.

## Subagent Omission

This package intentionally omits Cursor project subagents because the exact stable project subagent path and frontmatter cannot be established from the current target files. Do not simulate them, create legacy `.cursorrules`, or add background-agent automation.

## Safety Defaults

No hooks, MCP configuration, shell helpers, automatic approvals, background-agent configuration, credentials, endpoints, deployment automation, publication automation, signing automation, release automation, or automatic authentication are included. Human approval is required for sensitive actions, edits, command execution, external access, Git mutation, deployment, publication, signing, submission, and release.
