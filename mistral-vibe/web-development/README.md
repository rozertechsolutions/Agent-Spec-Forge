# Web Development — Mistral Vibe

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- AGENTS.md project instructions
- Project Skills in `.vibe/skills/`

## Intentionally omitted or disabled
- Custom agent TOML files are omitted to avoid model- or user-prompt binding
- MCP and executable hooks are not configured
- No provider or model is pinned

## Platform notes
Vibe receives the department through AGENTS.md and on-demand project Skills. This keeps the package project-scoped and provider-neutral while avoiding user-home prompt dependencies.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.mistral.ai/mistral-vibe/introduction/agents
- https://docs.mistral.ai/mistral-vibe/introduction/skills
- https://docs.mistral.ai/mistral-vibe/introduction/agents-md
