---
name: independent-assurance-review
description: Use for read-only final review of GRC deliverables, evidence, mappings, risk ratings, exception packages, remediation closure, and reporting claims.
---

# independent-assurance-review

- Objective: Perform a read-only final review that identifies unsupported claims, evidence gaps, approval gaps, and residual risk.
- Trigger: User asks for final review, assurance review, audit readiness review, policy review, risk acceptance package review, exception closure review, or reporting quality gate.
- Inputs: Draft artifact, source evidence, mapping table, risk or exception record, remediation evidence, intended audience, and decision being supported.
- Primary owner: `independent-assurance-reviewer`.
- Reviewers: None. This role is the independent reviewer and must not review work it authored.
- Steps: Confirm scope and independence; inspect evidence traceability; challenge claims and ratings; verify approval boundaries; classify findings; list required decisions.
- Validation gates: Findings include severity, affected artifact, evidence, remediation guidance, open questions, and human approvals.
- Stop conditions: Requested edit, self-review, secret access, unsupported evidence set, or request to approve/certify.
- Outputs: Review findings, approval checklist, residual-risk notes, open questions, and go/no-go recommendation for human decision.
- Human approvals: Required for any formal decision, external communication, audit conclusion, exception approval, or residual-risk acceptance.
