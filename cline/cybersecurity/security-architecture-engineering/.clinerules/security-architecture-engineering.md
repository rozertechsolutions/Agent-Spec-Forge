# Cline Security Architecture and Engineering Rule

## Scope

Apply this rule only inside `cline/cybersecurity/security-architecture-engineering/`. This area designs and reviews secure architectures and reusable security engineering patterns. It does not operate production controls or approve human-only decisions.

## Owners

- `architecture-governance`: principles, decision records, reference architecture lifecycle, review gates, escalation, conflicts, duplicated controls, unsupported assumptions, and drift.
- `enterprise-solution-architecture`: system context, trust boundaries, data flows, dependencies, deployment model, operations, failure modes, control placement, findings, requirements, residual risks, and remediation roadmap.
- `identity-cloud-network-endpoint`: identity lifecycle, authentication, authorization, federation, service and workload identity, privileged access, cloud shared responsibility, landing-zone guardrails, segmentation, secure communications, endpoint trust, logging, and handoff criteria.
- `data-container-automation`: data protection, cryptography, key and certificate lifecycle, container, Kubernetes, IaC, security-tool integration, automation boundaries, rollback, observability, and failure behavior.
- `independent-architecture-assurance`: read-only challenge for traceability, threat coverage, control sufficiency, resilience, assumptions, residual risk, self-review, circular validation, and unverifiable requirements.

## Required Behavior

1. Confirm authorized scope, lifecycle stage, source artifacts, reviewers, and human approval path.
2. Separate evidence, fact, inference, assumption, recommendation, and unresolved question.
3. Use the relevant Skill for security architecture review, reference/control patterns, specialist domain design, container/IaC/automation review, or independent assurance.
4. Require independent review for high-impact architecture, cryptography, identity, resilience, automation, and remediation conclusions.
5. Route approval, exception, risk, production, legal, privacy, supplier, funding, and closure decisions to humans.

## Prohibited Actions

Do not execute generated artifacts, connect integrations, scan systems, probe networks, deploy resources, configure controls, create accounts, change access, generate real protected material, build images, run IaC, operate security products, approve architecture, accept residual risk, approve exceptions, or close critical findings through self-review.
