# Web Development — OpenCode

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md instructions
- Project configuration with disabled sharing and empty MCP
- Custom agents
- Agent Skills
- Custom commands

## Intentionally omitted or disabled
- No plugins or custom tools
- No model is pinned
- Bash and editing require approval by default

## Platform notes
OpenCode permissions are set to ask before bash, edit and web fetch. Reviewer agents deny edits and bash. Automatic sharing is disabled.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://opencode.ai/docs/rules/
- https://opencode.ai/docs/agents/
- https://opencode.ai/docs/skills/
- https://opencode.ai/docs/commands/
- https://opencode.ai/docs/permissions/
- https://opencode.ai/docs/config/
