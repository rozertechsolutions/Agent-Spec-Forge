# Kiro Cybersecurity GRC Assurance Specialization

This directory contains only the Kiro package for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance. Work here must stay scoped to cybersecurity governance, policy frameworks, cyber risk, exceptions, control assurance, audit evidence, third-party risk, maturity reporting, and remediation oversight.

## Native Surface

- Target surface: current Kiro IDE and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md`.
- Steering guidance is provided through `.kiro/steering/governance-risk-compliance-assurance.md`.
- Custom agents are Kiro CLI JSON agents in `.kiro/agents/`.
- Reusable GRC processes are Kiro Agent Skills in `.kiro/skills/`.
- Hooks, MCP servers, Specs, Powers, executable scripts, and live integrations are intentionally not configured for this static package.

## Scope Rules

- Modify only files under `kiro/cybersecurity/governance-risk-compliance-assurance/`.
- Do not create shared cross-platform adapters, runtime abstractions, or common directories for this specialization.
- Do not activate external integrations, authenticate services, import credentials, start servers, publish, deploy, submit filings, approve risk, certify compliance, spend money, or run destructive operations.
- Do not hardcode model versions. Agents inherit the active model unless a future user explicitly requests a supported override.
- Treat genuine secrets, customer data, employee data, audit evidence, contracts, vulnerability data, and regulator communications as protected material.
- Review agents are read-only and must not implement or approve their own recommendations.

## Responsibilities

Use the five project custom agents exactly as defined in `.kiro/agents/`:

- `governance-policy-frameworks-agent`
- `cyber-risk-exceptions-agent`
- `assurance-evidence-remediation-agent`
- `third-party-maturity-reporting-agent`
- `independent-assurance-reviewer`

Implementation roles may prepare drafts, mappings, registers, remediation plans, and reporting packs. `independent-assurance-reviewer` performs final independent review and never reviews implementation it authored.

## Workflow Selection

Use these project Skills for repeatable work:

- `governance-policy-frameworks`
- `risk-exceptions-remediation`
- `assurance-third-party-reporting`
- `independent-assurance-review`

Do not duplicate these workflows as hooks, Specs, Powers, MCP servers, or executable commands. If a later user requests another Kiro-native surface, migrate only after preserving one authoritative workflow owner.

## Validation Standard

Every completed task must report actual evidence, assumptions, source gaps, human approval needs, and unavailable context. Do not claim compliance, certification, control effectiveness, risk acceptance, or audit readiness without explicit evidence and human approval.
