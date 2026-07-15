---
name: governance-policy-frameworks
description: Use for cybersecurity governance, policy hierarchy, control framework mapping, ownership, RACI, and applicability analysis.
compatibility: opencode
metadata:
  owner: governance-policy-frameworks-agent
---

# governance-policy-frameworks

- Objective: produce source-backed governance and framework material for Cybersecurity Area 01.
- Trigger: user asks for policy, standard, control framework, ownership, operating model, or governance forum work.
- Inputs: scope, framework names, policy artifacts, control catalog, owner list, risk appetite, committee model, constraints.
- Primary owner: `governance-policy-frameworks-agent`.
- Reviewers: `independent-assurance-reviewer`; affected risk or assurance owners when relevant.
- Steps: confirm scope; inventory source artifacts; map policies to controls; identify owners and decision forums; classify applicability; record gaps and assumptions; prepare decision-ready output.
- Conditional steps: ask for missing authority, framework source, or owner data before presenting conclusions.
- Validation gates: every framework claim has a source; every owner assignment is supported; every non-applicable control has rationale.
- Failures: stop on missing authority, unsupported compliance claim, or conflicting sources.
- Stop conditions: legal opinion, authoritative approval, live record change, or external submission.
- Evidence: source artifact, section, control identifier, owner, decision, and unresolved gap.
- Outputs: framework map, policy gap list, RACI, governance narrative, approval questions.
- Acceptance criteria: scope, source basis, ownership, gaps, and approval dependencies are explicit.
- Human approvals: framework adoption, policy approval, owner assignment, and governance forum change.
- Prohibited actions: approving policy, asserting compliance without evidence, changing live records, or contacting external parties.
