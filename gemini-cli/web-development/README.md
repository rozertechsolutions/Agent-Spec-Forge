# Web Development — Gemini CLI

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- GEMINI.md hierarchical project context
- Project custom commands in `.gemini/commands/`
- Empty workspace MCP settings

## Intentionally omitted or disabled
- No shell interpolation is used in commands
- No extensions, hooks or external tools
- No custom agents are created because a stable project-agent surface was not used for this package

## Platform notes
Every command is prompt-only TOML. There are no shell-interpolation blocks or automatic file injections. Users remain responsible for folder trust and approvals.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- https://google-gemini.github.io/gemini-cli/docs/cli/custom-commands.html
- https://google-gemini.github.io/gemini-cli/docs/cli/trusted-folders.html
- https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html
