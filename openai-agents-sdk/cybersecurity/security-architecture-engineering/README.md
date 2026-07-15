# OpenAI Agents SDK Security Architecture Engineering

This specialization implements a native Python package for the OpenAI Agents SDK. It coordinates Cybersecurity Area 02: Security Architecture and Engineering while keeping production changes, control operation, formal approval, and risk acceptance under human authority.

## Verified Surface

- Platform: OpenAI Agents SDK for Python.
- Native capabilities used: `Agent`, `Runner`, agents-as-tools, handoff-ready role boundaries, guardrail-style validators, typed workflow routing, and tracing controls.
- Unsupported or intentionally omitted: active MCP connections, hosted web/file/code-interpreter tools, daemon/UI/server processes, external connectors, provider setup, credential import, risk acceptance, architecture approval, compliance certification, deployment, live configuration, production operation, and destructive actions.

## Responsibility Model

The coordinator owns routing and synthesis. The five specialists preserve exclusive responsibility boundaries:

1. `architecture-governance-agent`
2. `enterprise-solution-architecture-agent`
3. `identity-cloud-network-agent`
4. `data-container-automation-agent`
5. `independent-architecture-reviewer`

Review roles are read-only by default. Drafting roles do not perform their own independent final review. `independent-architecture-reviewer` is the final independent reviewer and never reviews its own work.

## Workflows

- `security-architecture-governance`
- `enterprise-solution-patterns`
- `identity-cloud-network-data-design`
- `container-iac-automation-review`
- `independent-architecture-assurance`

Each workflow declares triggers, ordered steps, validation gates, stop conditions, evidence requirements, outputs, acceptance criteria, human approvals, and prohibited actions.

## Runtime Notes

The package declares the SDK dependency but does not install dependencies or run OpenAI API calls during import. Use `OPENAI_AGENTS_MODEL` to select a model at runtime. No model is hardcoded.

Official documentation consulted:

- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/tracing/

