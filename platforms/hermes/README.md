# Hermes Agent

Surfaces:
- Desktop
- CLI/TUI

Hermes Desktop and CLI use the same agent core and `~/.hermes/` configuration, so the reusable
agent example is stored under `common/`.

Native mechanisms demonstrated:
- Agent identity: `~/.hermes/SOUL.md`
- Non-secret settings: `~/.hermes/config.yaml`
- Skills: `~/.hermes/skills/`

Secrets belong in `~/.hermes/.env` or managed authentication files and are deliberately NOT
included.

Official documentation:
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration/
- https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
