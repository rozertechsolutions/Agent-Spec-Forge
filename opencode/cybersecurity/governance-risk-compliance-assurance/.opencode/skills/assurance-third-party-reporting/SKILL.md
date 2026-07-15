---
name: assurance-third-party-reporting
description: Use for control evidence, assurance requests, remediation validation, third-party assurance, maturity scoring, and executive reporting.
compatibility: opencode
metadata:
  owner: assurance-evidence-remediation-agent
---

# assurance-third-party-reporting

- Objective: prepare evidence-backed assurance, third-party, maturity, and reporting outputs.
- Trigger: user asks for evidence matrix, assurance response, remediation closure pack, supplier summary, maturity dashboard, or committee report.
- Inputs: control objective, evidence period, source artifacts, findings, supplier assessment, maturity scale, reporting audience, prior-period data.
- Primary owner: `assurance-evidence-remediation-agent`.
- Reviewers: `third-party-maturity-reporting-agent` for supplier or dashboard work; `independent-assurance-reviewer` for final challenge.
- Steps: define evidence period; inventory artifacts; map evidence to controls or findings; assess sufficiency; identify remediation status; apply maturity criteria; draft audience-fit narrative; disclose limitations.
- Conditional steps: route supplier scoring and dashboard narrative to `third-party-maturity-reporting-agent`.
- Validation gates: evidence period is clear; each claim has source support; ratings follow defined criteria; issue status has owner and validation basis.
- Failures: stop on unsupported effectiveness claim, missing period, conflicting evidence, or requested audit opinion.
- Stop conditions: evidence upload, live issue closure, external report submission, supplier contact, or publication.
- Evidence: source artifact, control or supplier identifier, period, finding, owner, status, rating criterion, and remaining gap.
- Outputs: evidence matrix, assurance response draft, remediation closure checklist, supplier summary, maturity report, dashboard narrative.
- Acceptance criteria: every material claim is traceable, rating limitations are visible, and unavailable evidence is clearly marked.
- Human approvals: audit response, issue closure, supplier status change, committee submission, and external communication.
- Prohibited actions: uploading evidence, changing third-party records, publishing reports, or asserting effectiveness without support.
