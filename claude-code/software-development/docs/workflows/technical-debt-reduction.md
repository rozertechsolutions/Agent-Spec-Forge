# Technical Debt Reduction

Identifier: `technical-debt-reduction`

## Purpose

Reduce prioritized debt without unrelated cleanup.

## Common Lifecycle

- Primary Claude Code session confirms scope, constraints, exclusions, approvals, and specialist routing.
- Requirements and Planning defines acceptance evidence and routing.
- Implementation occurs only after required human approvals.
- Test and Quality records validation evidence and checks not run.
- Code Quality and Engineering Risk reviews remain independent from implementation.
- Documentation and Release Readiness returns a human decision packet and stops before release actions.

## Workflow-Specific Gates

- identified debt and user or maintenance impact
- prioritization rationale
- bounded scope and preserved behavior
- measurable maintainability improvement
- prevention of opportunistic refactors

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
