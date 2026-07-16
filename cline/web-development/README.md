# Web Development — Cline

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Workspace rules in `.clinerules/`
- Project Skills in `.cline/skills/`

## Intentionally omitted or disabled
- Hooks, plugins, cron and executable workflows are omitted
- MCP is not configured because current IDE MCP settings are not project-portable
- Agent definitions are omitted to avoid mixing IDE and CLI schemas

## Platform notes
The package targets Cline workspace rules and Skills, which are current repository-scoped mechanisms shared safely with a team. It does not install a provider, plugin or model.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/getting-started/config
