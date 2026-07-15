# Cybersecurity Governance, Risk, Compliance & Assurance for Claude

This package defines a Claude-native project knowledge package for Cybersecurity Governance, Risk, Compliance & Assurance. It is intended for manual setup in a Claude Project by copying `PROJECT_INSTRUCTIONS.md` into project instructions and uploading the `knowledge/`, `templates/`, `workflows/`, and `reference/` files as project knowledge.

## Native mechanisms used

- Claude Project instructions.
- Claude Project knowledge files.
- Manual use of Claude chats inside the project.

## Unsupported or omitted mechanisms

This package does not create Claude Code files, local agents, subagents, hooks, MCP connector definitions, executable tools, or unverified Claude Skill bundles. Custom connectors using remote MCP require externally hosted services, authentication, and user/organization configuration, so they are documented as omitted and disabled by default.

## Safety baseline

Claude supports governance and assurance analysis only. It must not approve strategy, publish policy, accept risk, grant exceptions, approve suppliers, make legal determinations, claim compliance or certification, close critical findings by self-review, contact external parties, connect to security tools, scan systems, retrieve secrets, or execute active security operations.

