# Web Development — Local Provider-Independent Package

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Neutral department specification
- Role instructions
- Agent Skills
- Workflow specifications
- JSON Schemas
- Disabled provider/tool/MCP examples

## Intentionally omitted or disabled
- No runtime, model, provider, endpoint or executable is selected
- No automatic discovery, installation or authentication

## Platform notes
This is a provider-independent configuration package, not an executable runtime. A user or downstream open-source runtime must map the neutral files to its own supported schema after review.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://agentskills.io/specification
- https://modelcontextprotocol.io/specification/latest
