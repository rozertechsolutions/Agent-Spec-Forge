# Gemini CLI - Software Development

This directory configures Gemini CLI for the Software Development specialization.

## Native Surfaces

- `GEMINI.md` makes the main Gemini CLI agent the Software Development Lead.
- `.gemini/settings.json` sets default approval mode and enables Plan mode without providers, endpoints, models, credentials, MCP, hooks, extensions, sandbox builders, or environment values.
- `.gemini/agents/` contains seven specialist agents; there is intentionally no Lead agent.
- `.gemini/commands/software-development/*.toml` contains prompt-only workflow commands.
- `.gemini/skills/` contains static reusable Skills.

## Policy Removal

`.gemini/policies/software-development.toml` was intentionally removed because repository workspace policies are not currently an effective policy tier for this package. Safety relies on default approval mode, Plan mode, explicit tool allowlists, and instructions.

## Safety Model

Read-only specialists use read/search/list tools only. The implementation specialist uses read/search/list plus `write_file` and `replace`. No specialist is granted `run_shell_command`, web, MCP, browser, Git mutation, deployment, publication, signing, or release tools. Runtime loading and command execution have not been performed from this repository package.
