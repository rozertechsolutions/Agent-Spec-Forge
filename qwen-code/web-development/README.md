# Web Development — Qwen Code

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- QWEN.md project context
- Project subagents in `.qwen/agents/`
- Project Agent Skills
- Empty MCP settings and single-level subagent depth

## Intentionally omitted or disabled
- Experimental agent teams are not enabled
- No hooks, extensions or providers
- No model is pinned
- No auto-edit or yolo approval mode

## Platform notes
Subagents use `approvalMode: plan` for independent reviewers and `default` for implementation roles. Maximum subagent depth is one to prevent recursive delegation.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
- https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/
