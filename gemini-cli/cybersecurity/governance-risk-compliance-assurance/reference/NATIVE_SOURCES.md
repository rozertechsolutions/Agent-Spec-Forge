# Native Source Summary

Official Gemini CLI documentation checked on 2026-07-15:

- Gemini CLI `README.md`: describes Gemini CLI as an open-source terminal AI agent with custom context files, MCP support, and built-in tools.
- `docs/cli/gemini-md.md`: documents `GEMINI.md` context files, hierarchical loading, just-in-time context, imports, and configurable context file names.
- `docs/core/subagents.md`: documents subagents as specialized agents with focused context, specialized tools, independent context windows, and delegation.
- `docs/cli/skills.md` and `docs/cli/using-agent-skills.md`: document Agent Skills, workspace discovery under `.gemini/skills/`, `SKILL.md`, activation consent, and precedence.
- `docs/hooks/index.md` and `docs/cli/settings.md`: reviewed to classify hooks and active settings as omitted because hooks execute commands in the agent loop.

## Native Components Used

- `GEMINI.md` for durable workspace context.
- `.gemini/agents/*.md` for local specialist subagents.
- `.gemini/skills/*/SKILL.md` for workspace Agent Skills.

## Components Omitted

- Hooks and hook settings are omitted because this static repository package must not execute scripts.
- MCP servers are omitted because this area must not connect to external tools or evidence sources.
- Custom commands and extensions are omitted because they would duplicate the Skills and are not required.

