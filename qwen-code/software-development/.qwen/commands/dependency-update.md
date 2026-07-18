---
description: Change dependencies only after need, provenance, maintenance, license, compatibility, lockfile, and rollback evidence are clear.
---

# Dependency Update

## Purpose

Change dependencies only after need, provenance, maintenance, license, compatibility, lockfile, and rollback evidence are clear.

## Workflow-specific gates

- demonstrated need
- provenance and maintenance status
- transitive changes
- license signals
- vulnerability context
- compatibility
- lockfile impact
- rollback

## Risk triggers

- new transitive dependencies
- major version
- license change
- security advisory

Any trigger requires main-session classification, possible human approval, and Engineering Risk Reviewer participation where relevant.

## Prompt-only workflow

Route this command through the main Qwen Code session acting as Software Development Lead. The Lead may call specialist subagents for bounded evidence, but specialists must return to the main session, never call each other, never expand scope, and never claim final completion.

## Common gates

1. Main session confirms objective, authorized scope, constraints, exclusions, and approval requirements.
2. Requirements and Planning Specialist defines requirements, acceptance criteria, assumptions, and plan when needed.
3. Software Architect provides boundaries, contracts, alternatives, migrations, and compatibility evidence when triggered.
4. Implementation and Maintenance Engineer performs only approved edits under `approvalMode: default` and records implementation evidence.
5. Test and Quality Engineer records validation evidence and checks not run.
6. Code Quality Reviewer performs independent review after implementation.
7. Engineering Risk Reviewer reviews security, dependency, performance, reliability, data-integrity, or operational risk when triggered.
8. Documentation and Release Readiness Specialist records documentation, migration, compatibility, versioning, and readiness evidence.
9. Main session aggregates evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop on missing approval, conflicting requirements, secret exposure, unsupported platform behavior, unbounded scope, insufficient evidence, self-review, circular delegation, permissive parent approval mode, or any requested `run_shell_command`, shell, web, browser, network, Git, MCP, deployment, publication, signing, release, submission, account, credential, purchase, spending, or external communication action.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Validation evidence and checks not run.
- Independent code-quality review.
- Engineering-risk review when triggered.
- Documentation, compatibility, migration, versioning, and readiness status.
- Human decisions and unresolved limitations.
- Main-session final summary with no automatic release, deployment, publication, signing, submission, shell command, external action, or Git mutation.
