# Web Development — Claude Code

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- CLAUDE.md project instructions
- Project subagents in `.claude/agents/`
- Project Skills in `.claude/skills/`
- Project settings that disable hooks
- Empty project MCP configuration

## Intentionally omitted or disabled
- Executable hooks are disabled
- No plugins or external MCP servers
- No model is pinned

## Platform notes
Copy the contents of this directory to the target repository root. Subagents inherit the parent model unless the user chooses otherwise. Reviewer agents are restricted to read/search tools.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/mcp
