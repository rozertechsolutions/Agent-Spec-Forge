---
description: Evolve contracts with compatibility, migration, and examples.
---

# API or Library Evolution

Identifier: `api-or-library-evolution`

## Purpose

Evolve contracts with compatibility, migration, and examples.

## Common Lifecycle

- Primary Kilo Code agent confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- consumer impact analysis
- contract, schema, source, binary, and behavioral compatibility
- versioning and deprecation plan
- migration notes and examples
- contract tests or explicit untested areas

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Kilo Code Routing

- The primary agent remains Software Development Lead and routes work to specialists only when useful.
- Specialists return evidence to the primary agent and never delegate to each other.
- This command is prompt-only; it must not embed shell commands, web fetches, Git actions, deployment, publication, signing, submission, or release.
