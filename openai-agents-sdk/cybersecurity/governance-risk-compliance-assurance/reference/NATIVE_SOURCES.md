# Native Source Verification

Reviewed before creating this OpenAI Agents SDK package on July 15, 2026.

## Official OpenAI Agents SDK Documentation

- `https://openai.github.io/openai-agents-python/` confirmed SDK primitives: agents, agents as tools, handoffs, guardrails, sessions, human-in-the-loop, and tracing.
- `https://openai.github.io/openai-agents-python/agents/` confirmed agent configuration, instructions, tools, multi-agent patterns, handoffs, hooks, guardrails, and structured outputs.
- `https://openai.github.io/openai-agents-python/tools/` confirmed function tools and agents-as-tools.
- `https://openai.github.io/openai-agents-python/handoffs/` confirmed ownership-transfer patterns; this package keeps coordinator ownership by default.
- `https://openai.github.io/openai-agents-python/guardrails/` confirmed guardrail concepts used here as static validators.
- `https://openai.github.io/openai-agents-python/tracing/` confirmed tracing exists; tracing is disabled by default unless runtime configuration changes it.

## Package Decisions

- Included native artifacts: Python package, role definitions, coordinator and specialist agent builders, workflow registry, guardrail-style validators, README, and source reference.
- Omitted native artifacts: MCP servers, hosted tools, sessions, sandbox agents, realtime/voice agents, active connectors, daemon/server processes, executable setup scripts, and live API calls.
- Verification is static only: file presence, empty-file scan, secret-marker scan, and git diff review.
