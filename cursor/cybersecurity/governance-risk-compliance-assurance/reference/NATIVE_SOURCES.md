# Native Source Summary

Official Cursor documentation checked on 2026-07-15:

- Cursor Customize documentation: describes extension components including rules, skills, subagents, commands, MCP servers, and hooks.
- Cursor Rules documentation: documents project rules in `.cursor/rules/*.mdc`, rule frontmatter such as `description`, `globs`, and `alwaysApply`, plus nested `AGENTS.md` support.
- Cursor Subagents documentation: documents `.cursor/agents/*.md` subagents with frontmatter such as `name`, `description`, `model`, and `readonly`.
- Cursor Agent Skills documentation: documents Agent Skills as portable specialized capabilities using `SKILL.md` under `.cursor/skills`.
- Cursor Hooks and MCP documentation were reviewed only to classify them as omitted for this static package.

## Native Components Used

- `AGENTS.md` for scoped durable instructions.
- `.cursor/rules/grc-governance.mdc` for an always-applied area rule.
- `.cursor/agents/*.md` for specialist subagents.
- `.cursor/skills/*/SKILL.md` for reusable GRC workflows.

## Components Omitted

- Hooks are omitted because this area must not execute lifecycle scripts or enforce runtime behavior.
- MCP is omitted because this area must not connect to external tools, APIs, evidence stores, ticketing systems, cloud systems, or repositories.
- Commands, plugins, installers, and scripts are omitted because they are unnecessary for the static GRC package and would duplicate the Skills.

