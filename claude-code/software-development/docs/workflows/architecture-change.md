# Architecture Change

Identifier: `architecture-change`

## Purpose

Change boundaries or core structure through a documented decision.

## Common Lifecycle

- Primary Claude Code session confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- decision record with alternatives
- boundary and contract changes
- migration stages and compatibility plan
- engineering-risk and independent architecture review
- rollback plan before implementation

## Required Evidence

- scope and requirement traceability
- approvals needed or obtained
- validation performed and checks not run
- independent review findings
- unresolved limitations and human decisions

## Claude Code Routing

- The primary session remains Lead and may delegate once to a matching specialist.
- Specialists return evidence to the primary session and never delegate recursively.
- Workflow guidance is auxiliary and is not an executable command.
