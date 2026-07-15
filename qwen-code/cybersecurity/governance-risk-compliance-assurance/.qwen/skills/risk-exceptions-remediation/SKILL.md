---
name: risk-exceptions-remediation
description: Use for cyber risk records, exception governance, treatment options, compensating controls, remediation tracking, and closure criteria.
user-invocable: true
---

# Risk Exceptions Remediation

## Objective

Make risk, exception, and remediation decisions clear, traceable, time-bound, and reviewable.

## Trigger

Use when the user asks for a risk register entry, waiver, exception, treatment plan, compensating control, remediation tracker, or closure pack.

## Inputs

- Risk context, affected asset or process, control gap, rating criteria, exception request, treatment options, owners, due dates, validation evidence.

## Ownership

- Primary owner: `cyber-risk-exceptions-agent`.
- Supporting owner for closure evidence: `assurance-evidence-remediation-agent`.
- Reviewer: `independent-assurance-reviewer`.

## Sequence

1. Normalize risk statement into cause, event, impact, rating basis, treatment, and residual risk.
2. Identify exception expiry, approval authority, compensating controls, monitoring criteria, and escalation path.
3. Define remediation owner, due date, validation method, and closure criteria.
4. List missing evidence, unresolved assumptions, and approval questions.
5. Route final material through independent review.

## Gates

- Rating basis exists or is marked unavailable.
- Residual risk is explicit.
- Exception expiry and approval path are visible.
- Remediation has owner, due date, validation method, and closure criterion.

## Outputs

Risk record, exception pack, treatment options, remediation tracker fields, closure criteria, approval questions, and residual limitations.
