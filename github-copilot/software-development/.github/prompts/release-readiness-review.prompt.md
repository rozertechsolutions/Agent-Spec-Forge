---
description: Prepare a human release decision without releasing.
---

# Release Readiness Review

Identifier: `release-readiness-review`

## Purpose

Prepare a human release decision without releasing.

## Common Lifecycle

- Primary GitHub Copilot session confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- acceptance and validation evidence
- unresolved defects and risks
- documentation, changelog, migration, artifact, and version readiness
- rollback readiness
- explicit stop before publication, deployment, signing, submission, or release

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## GitHub Copilot Routing

- The primary session remains Software Development Lead and routes work to specialists only when useful.
- Specialists return evidence to the primary session and never delegate to each other.
- This prompt must not create GitHub Actions or instruct automatic issue, pull request, commit, push, deployment, publication, signing, submission, or release operations.
