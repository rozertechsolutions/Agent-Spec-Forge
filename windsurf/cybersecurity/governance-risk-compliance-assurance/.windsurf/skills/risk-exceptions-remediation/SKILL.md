---
name: risk-exceptions-remediation
description: Use for cyber risk records, exception governance, treatment options, compensating controls, remediation tracking, and closure criteria.
---

# risk-exceptions-remediation

## Objective

Make risk, exception, and remediation decisions clear, traceable, time-bound, and reviewable.

## Inputs

Risk context, affected asset or process, control gap, rating criteria, exception request, treatment options, owners, due dates, and validation evidence.

## Primary Owner

`cyber-risk-exceptions-agent`

## Steps

1. Normalize risk statements into cause, event, impact, rating basis, treatment, and residual risk.
2. Identify exception expiry, approval authority, compensating controls, monitoring criteria, and escalation path.
3. Define remediation owner, due date, validation method, and closure criteria.
4. List missing evidence, unresolved assumptions, and approval questions.
5. Route closure evidence questions to `assurance-evidence-remediation-agent`.
6. Route final material to `independent-assurance-reviewer`.

## Validation Gates

Rating basis exists or is marked unavailable; residual risk is explicit; exception expiry and approval path are visible; remediation has owner, due date, validation method, and closure criterion.

## Outputs

Risk record, exception pack, treatment options, remediation tracker fields, closure criteria, approval questions, and residual limitations.
