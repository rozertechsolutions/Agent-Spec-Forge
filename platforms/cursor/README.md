# Cursor

Surfaces:
- IDE
- Cursor CLI

The IDE and CLI share repository Rules and MCP configuration, so they live under `common/`.

Native mechanisms demonstrated:
- Project instructions: `AGENTS.md`
- Project Rules: `.cursor/rules/*.mdc`
- Reusable commands: `.cursor/commands/*.md`
- Project MCP configuration: `.cursor/mcp.json`

No agent/skill/hook directories are invented here unless backed by the current Cursor mechanism
being demonstrated.

Official documentation:
- https://docs.cursor.com/context/rules
- https://docs.cursor.com/agent/chat/commands
- https://docs.cursor.com/context/model-context-protocol
- https://docs.cursor.com/cli/installation
- https://docs.cursor.com/cli/using
