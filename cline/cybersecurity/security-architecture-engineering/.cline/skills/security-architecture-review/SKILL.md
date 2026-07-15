---
name: security-architecture-review
description: Use for authorized security architecture reviews of systems, solutions, trust boundaries, control placement, findings, and remediation roadmaps.
---

# security-architecture-review

- Mission: perform a static, evidence-based security architecture review.
- Scope: system context, data flows, trust boundaries, identities, dependencies, deployment, operations, threats, controls, resilience, findings, requirements, residual risk, and validation criteria.
- Inputs: authorized scope, business context, lifecycle stage, diagrams or descriptions, source artifacts, constraints, and reviewers.
- Preconditions: review authority and non-goals are known; no live access is required.
- Output: architecture review record and remediation roadmap.
- Allowed tools: repository reads and user-supplied static evidence only.
- Permissions: advisory only.
- Dependencies: specialist Skills and independent assurance.
- Invocation: use when a system, solution, or design is being reviewed.
- Delegation: route domain questions to specialist Skills.
- Stop conditions: missing scope, live access requirement, requested approval, or self-review conflict.
- Failure behavior: mark missing, stale, partial, contradictory, or unverifiable evidence.
- Completion criteria: findings, requirements, residual risk, validation criteria, and human decisions are traceable.
- Human review: required for high-impact decisions and production change.
- Prohibited actions: implementation, scanning, deployment, operational claims, or exception approval.
