# Mistral Vibe - Software Development

This directory implements the Software Development specialization for Mistral Vibe using native project content only. It is language-, framework-, database-, provider-, model-, and vendor-agnostic, and it must follow the repository's existing stack and conventions.

## Native content

- `AGENTS.md` contains repository-scoped department instructions.
- `.vibe/config.toml` names `software-development-lead` as the intended default agent.
- `.vibe/agents/software-development-lead.toml` is the user-facing coordinator with read/search plus the native `task` delegation tool.
- `.vibe/agents/*.toml` defines seven specialist subagents. Only `implementation-and-maintenance-engineer` has edit authority through `write_file` and `search_replace`; every other specialist is read-only.
- `.vibe/prompts/*.md` contains role prompts that require specialists to return evidence to the Lead.
- `.vibe/skills/*/SKILL.md` covers fourteen reusable capability areas.
- `docs/workflows/*.md` contains eleven differentiated workflow references.

## Safe selection requirement

For interactive use, select the `software-development-lead` agent before starting Software Development work. For programmatic use, explicitly select `software-development-lead` in the caller. Do not rely on an implicit default, ambient automation, or auto-approval setting because Mistral Vibe host behavior may bypass the package's intended safe selection path.

The Lead is the only agent with `task`; specialists cannot delegate or aggregate final completion. The Lead can route bounded work to specialists, collect evidence, require independent review after implementation, and stop for human approval.

## Safety limits

`safety = "safe"` is metadata, not an enforcement mechanism. Safety is enforced here through explicit tool allowlists and role instructions. The package contains no Bash grant, web tool, MCP configuration, hooks, executable launcher, model pin, provider pin, endpoint, credential, account identifier, deployment automation, publication automation, signing automation, release automation, or Git mutation authority.

Human approval is mandatory before destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, or irreversible actions. Release, deployment, publication, signing, notarization, submission, and Git mutation remain human-controlled and outside this package.

## Department responsibilities

1. Software Development Lead: scope, routing, approvals, dependency control, separation of duties, and final evidence aggregation.
2. Requirements and Planning Specialist: requirements, acceptance criteria, constraints, assumptions, exclusions, risks, and implementation planning.
3. Software Architect: boundaries, contracts, decisions, compatibility, migrations, and trade-offs.
4. Implementation and Maintenance Engineer: approved implementation, fixes, refactors, maintenance, and implementation evidence.
5. Test and Quality Engineer: validation strategy, regression coverage, edge cases, acceptance evidence, and untested areas.
6. Code Quality Reviewer: independent correctness, maintainability, architecture conformance, complexity, duplication, readability, and compatibility review.
7. Engineering Risk Reviewer: independent software security, dependency, supply-chain, performance, concurrency, reliability, data-integrity, and operational-risk review.
8. Documentation and Release Readiness Specialist: technical documentation, compatibility notes, migrations, versioning implications, readiness evidence, and unresolved limitations.

## Intentionally omitted

- model, provider, endpoint, account, or credential configuration
- Bash, shell, process, web, MCP, connector, deployment, publication, signing, release, or Git tools
- hooks, generated runtime code, installers, launchers, wrappers, or validators
- platform-loading claims beyond the static file structure represented here
