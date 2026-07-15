# Native Configuration Sources

Reviewed before creating this Mistral Vibe package on July 15, 2026.

- `https://docs.mistral.ai/vibe/choose-chat-work-code` confirmed Vibe Work, Chat, and Code modes; Code is the mode for codebase, terminal, IDE, and coding-session work.
- `https://docs.mistral.ai/vibe/work/skills` confirmed Skills as reusable instructions and resources that load progressively in Vibe Work.
- `https://docs.mistral.ai/vibe/code/cli/agents` confirmed custom project agents in `./.vibe/agents/*.toml`, `agent_type = "agent"`, `agent_type = "subagent"`, `system_prompt_id`, subagent delegation, and `AGENTS.md` support.
- `https://docs.mistral.ai/vibe/code/cli/configuration` confirmed project `.vibe/config.toml`, default agent, skills, tool filters, MCP server configuration, and configuration precedence.
- `https://docs.mistral.ai/vibe/code/cli/skills` confirmed project Skills in `./.vibe/skills/`, `SKILL.md` frontmatter, `user-invocable`, `allowed-tools`, and Skill filtering.

Included native artifacts: `AGENTS.md`, `.vibe/config.toml`, `.vibe/agents/`, `.vibe/prompts/`, `.vibe/skills/`, and `reference/`.

Omitted native artifacts: MCP servers, connectors, hooks, custom tools, executable scripts, provider/model configuration, telemetry overrides, remote sessions, and scheduled tasks.
