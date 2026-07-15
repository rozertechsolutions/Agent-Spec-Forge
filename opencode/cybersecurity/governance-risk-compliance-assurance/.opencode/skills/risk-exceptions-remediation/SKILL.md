---
name: risk-exceptions-remediation
description: Use for cyber risk records, exception governance, treatment options, compensating controls, remediation tracking, and closure criteria.
compatibility: opencode
metadata:
  owner: cyber-risk-exceptions-agent
---

# risk-exceptions-remediation

- Objective: make risk, exception, and remediation decisions clear, traceable, time-bound, and reviewable.
- Trigger: user asks for a risk register entry, waiver, exception, treatment plan, compensating control, remediation tracker, or closure pack.
- Inputs: risk context, affected asset or process, control gap, rating criteria, exception request, treatment options, owners, due dates, validation evidence.
- Primary owner: `cyber-risk-exceptions-agent`.
- Reviewers: `assurance-evidence-remediation-agent` for closure evidence; `independent-assurance-reviewer` for final challenge.
- Steps: normalize risk statement; identify cause, event, and impact; apply rating method; document treatment options; define exception expiry; set remediation owner and validation criteria; list approval questions.
- Conditional steps: request missing rating criteria, acceptance authority, treatment owner, due date, or evidence period.
- Validation gates: risk rating basis exists; residual risk is explicit; exception expiry is present; remediation has owner, due date, and validation method.
- Failures: stop on requested acceptance decision, missing authority, unsupported rating, or active incident handling.
- Stop conditions: live register update, production change, audit response submission, or external notification.
- Evidence: risk identifier, source artifact, affected scope, control gap, rating basis, treatment owner, due date, and validation gap.
- Outputs: risk record, exception pack, treatment options, remediation tracker fields, approval questions.
- Acceptance criteria: decision material is complete enough for human review and unresolved gaps are visible.
- Human approvals: risk acceptance, exception approval, due-date deferral, rating override, and closure.
- Prohibited actions: accepting risk, approving exceptions, closing issues without evidence, or changing authoritative systems.
