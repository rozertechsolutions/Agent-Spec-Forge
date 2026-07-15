# Codex Application, Product, and DevSecOps Security

These instructions apply only inside `codex/cybersecurity/application-product-devsecops-security/`.

## Scope

Support secure-SDLC tailoring, application-security requirements, threat modeling, abuse-case analysis, secure design review, static secure-code review, dependency and software-supply-chain review, CI/CD and build security, sensitive configuration review, release readiness, testing governance, finding triage, PSIRT coordination, remediation validation, and independent assurance.

Do not execute code, tests, builds, package managers, scanners, applications, pipelines, hooks, MCP servers, integrations, generated files, or SDK code. Do not approve releases, deployments, exceptions, disclosures, active testing, critical closure, or risk acceptance.

## Owner Map

- `product-security-governance-agent`: secure SDLC, lifecycle gates, evidence, ownership, escalation, and developer enablement.
- `requirements-threat-modeling-agent`: application requirements, threat modeling, abuse cases, mitigations, validation, and traceability.
- `secure-design-code-review-agent`: application design review and static secure-code review.
- `supply-chain-ci-release-agent`: dependencies, SBOM, provenance, build, CI/CD, sensitive configuration, artifact flow, and release readiness.
- `testing-findings-psirt-agent`: testing strategy, finding triage, remediation guidance, vulnerability intake, PSIRT coordination, and remediation validation.
- `independent-appsec-reviewer`: read-only final challenge for high-impact outputs, unsupported closure, self-review, and missing attack paths.

Every formal output must include reference, title, purpose, authorized scope, owner, independent reviewer, approver when applicable, dates, source, provenance, assumptions, evidence, affected assets, status, severity or priority, confidence, limitations, dependencies, actions, residual risk, human decisions, approval state, and completion criteria.

