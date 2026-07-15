# Native Source Verification

Verified on 2026-07-15 against official Qwen Code documentation:

- Repository README: `https://github.com/QwenLM/qwen-code`
- Qwen Code docs overview: `https://qwenlm.github.io/qwen-code-docs/en/users/overview/`
- Memory and `QWEN.md`: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/memory.md`
- Subagents: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/sub-agents.md`
- Skills: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/skills.md`
- Hooks: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/hooks.md`
- MCP: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/features/mcp.md`
- Settings: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/settings.md`
- Trusted folders: `https://raw.githubusercontent.com/QwenLM/qwen-code/main/docs/users/configuration/trusted-folders.md`

## Decisions

- `QWEN.md` is used for shared project instructions because the official memory documentation identifies it as Qwen Code project context.
- `.qwen/settings.json` is used because official settings documentation identifies project settings at that path.
- `.qwen/agents/*.md` is used because official subagent documentation identifies project-level agents at `.qwen/agents/` with YAML frontmatter.
- `.qwen/skills/*/SKILL.md` is used because official Skills documentation identifies project Skills at `.qwen/skills/<skill-name>/SKILL.md`.
- Hooks, MCP, extensions, scheduled tasks, daemon mode, and SDK code are omitted because this package is static and must not enable external execution or integrations.
