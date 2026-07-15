---
name: independent-assurance-review
description: Use for read-only challenge of governance, risk, exception, assurance, third-party, maturity, and executive reporting outputs.
compatibility: opencode
metadata:
  owner: independent-assurance-reviewer
---

# independent-assurance-review

- Objective: verify that final GRC and assurance outputs are source-backed, consistent, and transparent about limitations.
- Trigger: final review is requested or material is intended for governance, risk acceptance, exception approval, audit support, supplier review, or committee reporting.
- Inputs: draft output, source artifacts, scope statement, evidence matrix, risk or exception pack, rating criteria, owner list, approval path.
- Primary owner: `independent-assurance-reviewer`.
- Reviewers: none; this is the independent challenge step.
- Steps: confirm independence; verify scope; trace each material claim; test rating consistency; check owner and date fields; identify unsupported assertions; classify findings; recommend corrections.
- Conditional steps: require a different reviewer if independence is impaired.
- Validation gates: every material claim is traceable; every rating has criteria; every approval dependency is explicit; unresolved assumptions are visible.
- Failures: stop on missing source set, self-review, hidden limitation, or requested approval decision.
- Stop conditions: source edits, acceptance decisions, live record changes, external submissions, or suppression of findings.
- Evidence: claim, source artifact, review test, result, gap, severity, and recommended disposition.
- Outputs: review findings, severity, required corrections, residual limitations, final readiness statement.
- Acceptance criteria: blockers are corrected or explicitly reported as unresolved; advisory findings are separated from required corrections.
- Human approvals: final governance approval, risk acceptance, exception approval, assurance conclusion, and external reporting.
- Prohibited actions: editing reviewed material, approving own work, accepting risk, closing findings, or hiding limitations.
