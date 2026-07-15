# Kilo Code Cybersecurity GRC Assurance Specialization

This directory contains only the Kilo Code package for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance. Work here must stay scoped to policy governance, cyber risk, control assurance, audit evidence, third-party risk, maturity reporting, and remediation oversight.

## Native Surface

- Target surface: current Kilo Code VS Code extension and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md` and `kilo.jsonc`.
- Project rules are native Markdown instructions referenced from the `instructions` array in `kilo.jsonc`.
- Custom subagents are native project Markdown agents in `.kilo/agents/`.
- Reusable GRC processes are native Agent Skills in `.kilo/skills/`.
- `.kilocodeignore` is used only as a static file-access guard for sensitive local material.
- MCP servers, plugins, shell workflows, and slash commands are intentionally not configured for this static package.

## Scope Rules

- Modify only files under `kilo-code/cybersecurity/governance-risk-compliance-assurance/`.
- Do not create shared cross-platform adapters, generic runtime abstractions, or common directories for this specialization.
- Do not activate external integrations, authenticate services, import credentials, start servers, publish, deploy, submit filings, approve risk, certify compliance, spend money, or run destructive operations.
- Do not hardcode model versions. Agents inherit the active model unless a future user explicitly requests a supported override.
- Treat genuine secrets, customer data, employee data, audit evidence, contracts, vulnerability data, and regulator communications as protected material.
- Review agents are read-only and must not implement or approve their own recommendations.

## Responsibilities

Use the five project subagents exactly as defined in `.kilo/agents/`:

- `governance-policy-frameworks-agent`
- `cyber-risk-exceptions-agent`
- `assurance-evidence-remediation-agent`
- `third-party-maturity-reporting-agent`
- `independent-assurance-reviewer`

Implementation roles may prepare drafts, mappings, registers, and remediation plans. `independent-assurance-reviewer` performs final independent review and never reviews implementation it authored.

## Workflow Selection

Use these project Skills for repeatable work:

- `governance-policy-frameworks`
- `risk-exceptions-remediation`
- `assurance-third-party-reporting`
- `independent-assurance-review`

Do not duplicate these workflows as slash commands. If a user explicitly asks for slash-command versions later, migrate only after removing the equivalent Skill to keep one authority.

## Validation Standard

Every completed task must report actual evidence, assumptions, source gaps, human approval needs, and unavailable context. Do not claim compliance, certification, control effectiveness, risk acceptance, or audit readiness without explicit evidence and human approval.
