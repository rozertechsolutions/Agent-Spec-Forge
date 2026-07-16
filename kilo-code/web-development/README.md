# Web Development — Kilo Code

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md
- Kilo project config
- Project rules
- Custom agents/subagents
- Agent Skills
- Slash-command workflows
- Empty MCP map and approval-oriented permissions

## Intentionally omitted or disabled
- No legacy `.kilocodemodes` or `.kilocode/` formats
- No hooks or plugins
- No model is pinned

## Platform notes
This package targets the current VS Code/CLI surface and uses `.kilo/` rather than legacy configuration. Reviewer agents deny edit and bash.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://kilo.ai/docs/customize/agents-md
- https://kilo.ai/docs/customize/custom-modes
- https://kilo.ai/docs/customize/custom-subagents
- https://kilo.ai/docs/customize/skills
- https://kilo.ai/docs/customize/workflows
- https://kilo.ai/docs/configure/mcp-servers
