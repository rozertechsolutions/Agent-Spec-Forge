# Native Source Verification

Official sources checked on 2026-07-15:

- Gemini CLI README: `https://github.com/google-gemini/gemini-cli`
- Configuration: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/configuration.md`
- Context files: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md`
- Subagents: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/subagents.md`
- Skills: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md`

## Decisions

- `GEMINI.md` is used for project context.
- `.gemini/agents/*.md` is used for project subagents.
- `.gemini/skills/*/SKILL.md` is used for reusable Skills.
- MCP, tool discovery commands, shell wrappers, and executable automation are omitted because this static package must not execute or connect anything.

