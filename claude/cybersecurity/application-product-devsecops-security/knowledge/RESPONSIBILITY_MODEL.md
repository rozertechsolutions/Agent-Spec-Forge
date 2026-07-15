# Responsibility Model

## Primary Owners

- `product-security-governance`: secure-SDLC activities, criticality tailoring, lifecycle matrix, evidence model, escalation, and developer enablement.
- `requirements-threat-modeling`: application-security requirements, threat models, abuse cases, mitigations, and validation traceability.
- `secure-design-code-review`: design review, static secure-code review, confirmed code evidence, remediation guidance, and static validation criteria.
- `supply-chain-ci-release`: dependency, SBOM, provenance, build, CI/CD, configuration, artifact, and release-readiness review.
- `testing-findings-psirt`: testing strategy, finding triage, remediation guidance, vulnerability intake, PSIRT coordination, and remediation validation.
- `independent-appsec-assurance`: read-only final challenge and assurance review.

## Human Decisions

Release approval, deployment, exception approval, active testing authorization, disclosure, public communication, legal position, finding closure, and risk acceptance remain human-only.

## Evidence Rules

Do not fabricate evidence. Preserve source and provenance. Mark missing, stale, partial, contradictory, or unverifiable evidence. Static findings must not be represented as dynamically reproduced unless supplied evidence proves that status.

