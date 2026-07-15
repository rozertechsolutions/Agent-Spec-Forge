# Native Kilo Code Sources

Official Kilo Code documentation checked on 2026-07-15:

- Documentation index: `https://kilocode.ai/docs/llms.txt`
- AGENTS.md customization: `https://kilocode.ai/docs/customize/agents-md`
- Custom rules: `https://kilocode.ai/docs/customize/custom-rules`
- Custom subagents: `https://kilocode.ai/docs/customize/custom-subagents`
- Agent Skills: `https://kilocode.ai/docs/customize/skills`
- Workflows: `https://kilocode.ai/docs/customize/workflows`
- Ignore file: `https://kilocode.ai/docs/customize/context/kilocodeignore`

Implementation decision: use `AGENTS.md`, `kilo.jsonc`, `.kilocodeignore`, `.kilo/rules/*.md`, `.kilo/agents/*.md`, and `.kilo/skills/*/SKILL.md`. Omit MCP servers, plugins, workflows, slash commands, shell automation, external integrations, authentication, scans, deployment, publication, and live-system actions because this package is static guidance only.
