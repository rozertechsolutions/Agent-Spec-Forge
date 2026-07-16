# Web Development — Cursor

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md instructions
- Cursor Project Rules
- Project subagents in `.cursor/agents/`
- Project Skills in `.cursor/skills/`
- Empty project MCP configuration

## Intentionally omitted or disabled
- Hooks are omitted
- No model is pinned
- No cloud agent publication or GitHub integration is configured

## Platform notes
Rules and subagents are scoped to the repository. Read-only reviewer subagents use Cursor's native `readonly` field. MCP remains empty.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://cursor.com/docs/rules
- https://cursor.com/docs/subagents
- https://cursor.com/docs/context/skills
- https://cursor.com/docs/context/mcp
