# Web Development — GitHub Copilot

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Repository custom instructions
- Path-specific web instructions
- Custom agent profiles
- Agent Skills
- Reusable prompt files

## Intentionally omitted or disabled
- No MCP servers are embedded
- No GitHub Actions, workflows, hooks or automatic PR behavior
- No model is pinned

## Platform notes
The files target repository-scoped Copilot Chat, IDE and coding-agent customization. Reviewer profiles expose only read/search tools. Prompt files never instruct Copilot to push, merge or deploy.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents
- https://docs.github.com/en/copilot/reference/custom-agents-configuration
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
