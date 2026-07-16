# Web Development — OpenAI Agents SDK (Python)

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Python package defining agents, handoffs, contracts and approval policy
- No-tools-by-default orchestration
- Static policy tests

## Intentionally omitted or disabled
- No server, UI, deployment, installer, environment file, API key or MCP server
- No model is pinned
- No executable shell or computer-use tool

## Platform notes
The code is a reference SDK configuration. Agents have instructions and handoffs but no tools, so importing the package cannot modify a computer or external system. A downstream application must add tools explicitly and enforce the included approval policy.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
