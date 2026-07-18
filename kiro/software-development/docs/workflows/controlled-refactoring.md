# Controlled Refactoring

Identifier: `controlled-refactoring`

## Purpose

Improve structure while preserving external behavior.

## Common Lifecycle

- Primary Kiro agent confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- explicit invariants and public behavior that must not change
- bounded transformation plan
- compatibility evidence before and after
- regression checks focused on unchanged behavior
- rollback or reversal plan

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
