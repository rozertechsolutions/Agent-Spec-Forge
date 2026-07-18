# Technical-Debt Reduction

## Purpose

Reduce prioritized debt with bounded scope and measurable maintainability benefit.

## Entry conditions

- A named human-requested objective exists.
- The authorized repository scope is known.
- Acceptance criteria or the maintenance objective can be verified.
- Required approvals are identified before any sensitive or irreversible action.

## Workflow-specific focus

- identified debt, impact, and prioritization rationale
- bounded scope that avoids unrelated cleanup
- preserved behavior and compatibility expectations
- measurable maintainability or risk reduction
- prevention notes for recurrence

## Risk triggers

- wide change surface
- architecture drift
- weak test safety net

Any trigger requires Engineering Risk Reviewer participation and may require explicit human approval before implementation.

## Common stages

1. **Intake - Software Development Lead:** confirm objective, authorized scope, exclusions, constraints, and required human approvals.
2. **Requirements - Requirements and Planning Specialist:** define requirements, acceptance criteria, assumptions, and unresolved questions.
3. **Context analysis - assigned specialist:** inspect only necessary repository context and return factual evidence to the Lead.
4. **Risk classification - Software Development Lead:** identify required reviews, approval checkpoints, and stop conditions.
5. **Design or plan - Software Architect or Requirements and Planning Specialist:** define contracts, ordered changes, validation strategy, and rollback considerations where applicable.
6. **Human checkpoint:** obtain explicit approval before sensitive, irreversible, dependency, architecture, public-contract, migration, permission, trust-boundary, or scope-changing decisions.
7. **Implementation - Implementation and Maintenance Engineer:** make only approved changes and return implementation evidence.
8. **Validation - Test and Quality Engineer:** evaluate acceptance, regression, edge cases, and every unexecuted check.
9. **Independent code review - Code Quality Reviewer:** review correctness, maintainability, architecture fit, compatibility, and unintended effects.
10. **Independent risk review - Engineering Risk Reviewer when triggered:** review security, dependencies, supply chain, performance, concurrency, reliability, data integrity, and operational risk.
11. **Documentation/readiness - Documentation and Release Readiness Specialist:** update required documentation and assess readiness without release execution.
12. **Close - Software Development Lead:** aggregate returned evidence, blockers, limitations, and human decisions.

## Stop conditions

Stop and escalate on missing approval, conflicting requirements, secret exposure, unsupported behavior, unbounded scope, unavailable evidence, failed critical validation, circular delegation, self-review, or any requested Bash, web, MCP, Git, deployment, publication, signing, release, submission, account, credential, or external communication action.

## Completion evidence

- Requirement-to-change traceability.
- Workflow-specific evidence listed above.
- Acceptance and validation matrix.
- Independent code-quality outcome.
- Engineering-risk outcome when triggered.
- Documentation, compatibility, migration, and readiness status.
- Explicit list of tests and checks not run.
- Human-controlled release-readiness verdict aggregated only by the Software Development Lead.
