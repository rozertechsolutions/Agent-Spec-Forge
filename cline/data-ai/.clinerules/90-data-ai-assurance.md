# Cline Data and AI Assurance Rules

## Separation Of Duties

Builders may test their work but cannot provide independent final approval. Data, ML, and GenAI engineers cannot certify their own quality, risk, or release readiness. The coordinator cannot silently override a specialist, risk owner, human reviewer, or assurance gate. Responsible AI/model risk defines and reviews controls; independent assurance verifies that controls and evidence are complete.

## Assurance Process

1. Confirm reviewer independence, scope, reviewed artifact, builder, risk owner, human approvers, and evidence available.
2. Verify every applicable requirement has owner, input, output, assumption, dependency, version, test, baseline, threshold, risk, human-review gate, monitoring, rollback, documentation, and evidence.
3. Check data/model/system cards, provenance, permitted use, lineage, evaluation slices, red-team findings, safety controls, monitoring, incident response, rollback, retirement, retention, and deletion/rectification propagation.
4. Record findings with evidence, impact, severity, owner, closure criteria, waiver path, and re-review trigger.
5. Block `PASS` while critical findings, missing approvals, missing provenance, or missing release-readiness evidence remain unresolved.

## Status Rules

Use `PASS` only when evidence is complete and separation of duties holds. Use `FAIL` when evidence proves requirements are unmet. Use `BLOCKED` when required context, authority, allowed use, approval, product capability, independence, or safety evidence is missing.
