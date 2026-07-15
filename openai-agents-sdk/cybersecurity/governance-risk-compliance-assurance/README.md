# OpenAI Agents SDK Cybersecurity GRC Assurance

This specialization implements a native Python package for the OpenAI Agents SDK. It coordinates Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance while keeping formal approvals and sensitive evidence under human control.

## Verified Surface

- Platform: OpenAI Agents SDK for Python.
- Native capabilities used: `Agent`, `Runner`, agents-as-tools, handoff-ready role boundaries, guardrail-style validators, typed workflow routing, and tracing controls.
- Unsupported or intentionally omitted: active MCP connections, hosted web/file/code-interpreter tools, daemon/UI/server processes, external connectors, provider setup, credential import, regulator submission, risk acceptance, compliance certification, audit sign-off, vendor approval, deployment, and destructive actions.

## Responsibility Model

The coordinator owns routing and synthesis. The five specialists preserve exclusive responsibility boundaries:

1. `governance-policy-frameworks-agent`
2. `cyber-risk-exceptions-agent`
3. `assurance-evidence-remediation-agent`
4. `third-party-maturity-reporting-agent`
5. `independent-assurance-reviewer`

Review roles are read-only by default. Drafting roles do not perform their own independent final review. `independent-assurance-reviewer` is the final independent reviewer and never reviews its own work.

## Workflows

- `governance-policy-frameworks`
- `risk-exceptions-remediation`
- `assurance-third-party-reporting`
- `independent-assurance-review`

Each workflow declares triggers, preconditions, ordered steps, validation gates, stop conditions, evidence requirements, outputs, acceptance criteria, human approvals, and prohibited actions.

## Runtime Notes

The package declares the SDK dependency but does not install dependencies or run OpenAI API calls during import. Use `OPENAI_AGENTS_MODEL` to select a model at runtime. No model is hardcoded.

Official documentation consulted:

- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/agents/
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/handoffs/
- https://openai.github.io/openai-agents-python/guardrails/
- https://openai.github.io/openai-agents-python/tracing/
