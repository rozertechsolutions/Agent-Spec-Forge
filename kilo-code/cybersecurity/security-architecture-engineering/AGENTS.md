# Kilo Code Cybersecurity Security Architecture Engineering Specialization

This directory contains only the Kilo Code package for Cybersecurity Area 02: Security Architecture Engineering. Work here must stay scoped to secure architecture design, review, documentation, reusable security engineering patterns, architecture governance, IAM/PAM, cloud, network, endpoint, data protection, cryptography, container, Kubernetes, IaC, automation boundaries, and independent architecture assurance.

## Native Surface

- Target surface: current Kilo Code VS Code extension and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md` and `kilo.jsonc`.
- Project rules are native Markdown instructions referenced from the `instructions` array in `kilo.jsonc`.
- Custom subagents are native project Markdown agents in `.kilo/agents/`.
- Reusable architecture processes are native Agent Skills in `.kilo/skills/`.
- `.kilocodeignore` is used only as a static file-access guard for sensitive local material.
- MCP servers, plugins, shell workflows, and slash commands are intentionally not configured for this static package.

## Scope Rules

- Modify only files under `kilo-code/cybersecurity/security-architecture-engineering/`.
- Do not create shared cross-platform adapters, generic runtime abstractions, or common directories for this specialization.
- Do not activate external integrations, authenticate services, import credentials, start servers, publish, deploy, approve risk, approve exceptions, operate controls, or run destructive operations.
- Do not hardcode model versions. Agents inherit the active model unless a future user explicitly requests a supported override.
- Treat genuine restricted material, personal data, private endpoints, certificates, architecture diagrams, and supplier confidential data as protected material.
- Review agents are read-only and must not implement or approve their own recommendations.

## Responsibilities

Use the five project subagents exactly as defined in `.kilo/agents/`:

- `architecture-governance-agent`
- `enterprise-solution-architecture-agent`
- `identity-cloud-network-agent`
- `data-container-automation-agent`
- `independent-architecture-reviewer`

Implementation roles may prepare designs, reviews, ADRs, patterns, findings, and remediation validation packages. `independent-architecture-reviewer` performs final independent review and never reviews implementation it authored.

## Workflow Selection

Use these project Skills for repeatable work:

- `security-architecture-review`
- `reference-and-control-patterns`
- `identity-cloud-network-data-design`
- `container-iac-automation-review`
- `independent-architecture-assurance`

Do not duplicate these workflows as slash commands. If a user explicitly asks for slash-command versions later, migrate only after removing the equivalent Skill to keep one authority.

## Validation Standard

Every completed task must report actual evidence, assumptions, source gaps, human approval needs, and unavailable context. Do not claim architecture approval, risk acceptance, exception approval, production readiness, or control effectiveness without explicit evidence and human approval.
