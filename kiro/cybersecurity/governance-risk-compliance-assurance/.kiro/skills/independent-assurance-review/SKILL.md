---
name: independent-assurance-review
description: Use for independent read-only review of cybersecurity GRC artifacts, evidence, claims, risks, exceptions, and remediation packages.
---

# independent-assurance-review

- Objective: Provide independent findings before a GRC artifact is treated as complete.
- Trigger: User asks for review, final validation, assurance challenge, evidence quality check, risk package review, or control mapping critique.
- Inputs: Draft artifact, source evidence, assumptions, scope, acceptance criteria, prior findings, and requested decision.
- Primary owner: `independent-assurance-reviewer`.
- Reviewers: Human accountable owner only.
- Steps: Verify scope; compare claims to evidence; flag unsupported conclusions; check ownership and approvals; identify risks, gaps, contradictions, and missing validation; recommend precise corrections.
- Validation gates: Findings are ordered by severity and cite the affected artifact section or source gap.
- Stop conditions: Reviewer authored the artifact, evidence is unavailable, legal interpretation is required, or the user asks the reviewer to approve risk or certify compliance.
- Outputs: Findings, residual risk, evidence gaps, approval requirements, and completion readiness recommendation.
- Human approvals: Required for final acceptance, external use, risk acceptance, audit sign-off, and compliance claims.
