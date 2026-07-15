---
name: independent-assurance-review
description: Use for independent read-only review of cybersecurity GRC artifacts, evidence, claims, risks, exceptions, and remediation packages.
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# Independent Assurance Review

Use this procedure for independent findings before a GRC artifact is treated as complete.

1. Confirm reviewer independence, scope, acceptance criteria, source evidence, and artifact version.
2. Compare claims to evidence and flag unsupported conclusions, contradictions, and missing approvals.
3. Check ownership, decision points, residual risk, evidence freshness, and external-use restrictions.
4. Order findings by severity and cite affected sections or source gaps.
5. Return readiness recommendation, approval requirements, limitations, and next corrections.

Stop for self-review, unavailable evidence without a gap label, legal interpretation, or requests to approve risk or certify compliance.
