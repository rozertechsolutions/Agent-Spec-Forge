# GRC Decision Package

## Purpose

Manually prepare a traceable Cybersecurity Area 01 decision package for explicit human approval without changing live records, submitting external material, uploading evidence, or contacting third parties.

## Invocation

Invoke manually with `/grc-decision-package` after intake validation identifies exact scope, owner, required inputs, independent reviewers, and approval authority.

## Stages

1. **Validate scope and source set.** Capture objective, source artifacts, source period, exclusions, owner, reviewers, approval authority, and state. Do not advance while a blocker remains.
2. **Reconcile ownership and framework basis.** Capture applicable frameworks, policies, controls, owners, RACI, assumptions, and gaps. Do not advance while a blocker remains.
3. **Resolve risk, exception, and remediation status.** Capture rating basis, residual risk, exception expiry, treatment owner, due date, validation method, and unresolved risk. Do not advance while a blocker remains.
4. **Verify evidence, third-party, and maturity claims.** Capture evidence sufficiency, supplier limitations, maturity criteria, reporting audience, findings, and unavailable evidence. Do not advance while a blocker remains.
5. **Run independent assurance review.** Capture reviewer, findings, required corrections, residual limitations, and final readiness. Do not advance while a blocker remains.
6. **Record final human decision request.** Capture decision options, recommended path, approvals required, limitations, next owner, and exact non-actions.

## Stage Transition Contract

A stage may advance only when its owner, inputs, output, evidence, measurable checks, risks, dependencies, reviewer, and next state are recorded. Failed review returns the work to the responsible stage.

## Mandatory Gates

- Intake and scope gate.
- Framework and ownership gate.
- Risk, exception, and remediation gate.
- Evidence, third-party, and maturity gate when applicable.
- Independent assurance gate.
- Explicit human decision gate before any live action.

## Failure Behavior

Stop at the affected stage, preserve valid outputs, issue a blocker record in the response, and resume only when the named condition is satisfied. Do not skip, merge, or fabricate a passed gate.

## Final Output

A traceable decision package containing the approved objective, owners, sources, evidence, findings, risks, unresolved items, review records, approval path, exact requested human decision, and confirmation that no external write or live-system action occurred.
