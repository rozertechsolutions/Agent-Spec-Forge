# Architecture Change

Identifier: `architecture-change`

## Purpose

Change boundaries or core structure through a documented decision.

## Common Lifecycle

- Primary Kiro agent confirms scope, constraints, exclusions, approvals, and specialist routing.
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

## Kiro Routing

- The primary Kiro agent remains Software Development Lead and may route to one of seven `.kiro/agents/` specialists.
- Specialists return evidence to the primary agent and never delegate to each other.
- This workflow file is auxiliary unless Kiro IDE natively loads it in the target environment; it is not a spec or executable workflow engine.
