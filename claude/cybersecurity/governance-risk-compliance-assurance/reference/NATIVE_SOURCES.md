# Native Configuration Sources

Official sources checked on 2026-07-15:

- Claude Help Center: What are projects?, `https://support.claude.com/en/articles/9517075-what-are-projects`.
- Claude Help Center: Get started with custom connectors using remote MCP, `https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp`.
- Claude Developer Documentation index, `https://docs.claude.com/llms.txt`.

## Current native surface

Claude Projects provide self-contained workspaces with chat histories, project knowledge bases, document uploads, and project instructions. Team and Enterprise project sharing can provide `Can use` and `Can edit` permission levels. Custom connectors using remote MCP are available in Claude but require adding a reachable remote MCP server, optional OAuth details, user connection, and per-conversation enablement.

## Implementation decision

This package uses Claude Project instructions and project knowledge files only. It omits custom connectors because they would require external services, authentication, and live tool access. It omits Claude Code files because this platform is `claude/`, not `claude-code/`. It omits Claude Skills because a current official Help Center or developer-docs page establishing the upload format and scope could not be verified safely during this run.

