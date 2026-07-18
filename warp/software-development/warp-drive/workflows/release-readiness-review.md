# Release-Readiness Review

## Purpose

Aggregate readiness evidence and stop before publication, deployment, signing, or release.

## Workflow-specific gates

- acceptance evidence
- unresolved defects and risks
- documentation, changelog, and migration readiness
- artifact and version implications
- rollback readiness
- explicit stop before publication, deployment, signing, or release

## Risk triggers

- missing evidence
- known critical issue
- unreviewed change
- incomplete documentation

Any trigger requires primary Lead classification, possible human approval, and engineering-risk review where relevant.

## Workflow source boundary

This is Warp Drive workflow source material for manual import or supported Warp Drive surfaces. It is not a claim of universal automatic repository loading.

## Common lifecycle

1. Primary Warp Agent confirms objective, authorized scope, constraints, exclusions, and approval requirements.
2. Requirements stage defines requirements, acceptance criteria, assumptions, and plan when needed.
3. Architecture stage provides boundaries, contracts, alternatives, migrations, and compatibility evidence when triggered.
4. Implementation stage performs only explicitly approved edits and records implementation evidence.
5. Validation stage records acceptance, regression, edge-case evidence, and checks not run.
6. Independent code-quality stage reviews after implementation.
7. Engineering-risk stage reviews security, dependency, performance, reliability, data-integrity, or operational risk when triggered.
8. Documentation/readiness stage records documentation, migration, compatibility, versioning, and readiness evidence.
9. Primary Lead aggregates evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop on missing approval, conflicting requirements, secret exposure, unsupported Warp behavior, unbounded scope, insufficient evidence, self-review, circular routing, or any requested terminal command, edit, Git action, external action, MCP, connector, cloud/background schedule, deployment, publication, signing, release, submission, account, credential, purchase, spending, or external communication action without explicit interactive human approval.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Validation evidence and checks not run.
- Independent code-quality review.
- Engineering-risk review when triggered.
- Documentation, compatibility, migration, versioning, and readiness status.
- Human decisions and unresolved limitations.
- Primary Lead final summary with no automatic terminal command, edit, Git mutation, external action, release, deployment, publication, signing, or submission.
