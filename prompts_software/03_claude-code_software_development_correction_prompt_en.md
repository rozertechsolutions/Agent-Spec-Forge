# AI Specialized Departments — Claude Code Software Development Correction Prompt

## Exact target root

`claude-code/software-development/`

## Purpose

Correct the existing **Software Development** implementation for **Claude Code** in place.

**Previous audit result:** `PASS WITH CORRECTIONS`  
**Selected product surface:** `CLAUDE.md`, `.claude/settings.json`, project subagents, and project Skills


## Absolute static-only execution boundary

This correction prompt authorizes direct file reading, creation, editing, and deletion only inside the exact target root stated above.

You must not:

- use a terminal, shell, command runner, process runner, script, notebook, interpreter, compiler, package manager, build tool, test runner, linter, formatter, generator, validator, or executable;
- run any command, including commands that only list files, inspect status, count files, validate syntax, create directories, compare content, or delete files;
- install or update software, packages, plugins, runtimes, models, extensions, or dependencies;
- inspect or mutate Git in any way;
- access the network, browse documentation, call APIs, authenticate, connect to external services, or use MCP;
- inspect environment variables, home-directory configuration, installed software, processes, hardware, accounts, IDE state, or operating-system settings;
- read or write outside the target root;
- follow or create symbolic links, aliases, mounts, or traversal paths that leave the target;
- execute hooks or generated configuration;
- create scripts, binaries, installers, launchers, scheduled tasks, background jobs, or executable files;
- modify another platform, specialization, repository-root file, or user-global configuration.

Use only direct file/editor APIs. Before reading, editing, creating, or deleting a path, normalize it logically and confirm that it remains beneath the exact target root.

If direct deletion is unavailable, do not use a command as a substitute. Leave the file unchanged and report the unresolved deletion.

## Correction principles

- This is an in-place correction, not a full blind regeneration.
- Inventory the existing target through direct file APIs.
- Preserve every valid native component and all unique useful content.
- Modify only what is needed to correct a defect, remove duplication, improve native accuracy, deepen professional coverage, or enforce safety.
- Delete a file only when it is unsupported, misleading, unsafe, obsolete, irreducibly duplicated, or replaced by a verified native equivalent.
- Before deletion, migrate every unique useful requirement to the correct surviving component.
- Do not create empty files, placeholders, TODO-only files, `unsupported/` directories, decorative folders, compatibility shims, universal adapters, `common/`, installers, or shared cross-platform runtime code.
- Keep all generated content in English.
- Keep the package language-, framework-, database-, provider-, model-, and vendor-agnostic.
- Do not include secrets, credentials, tokens, private URLs, real endpoints, account identifiers, environment-specific paths, or fixed models.
- Do not claim that a platform loaded, accepted, executed, or validated a configuration unless directly observed; execution is prohibited here.

## Department responsibility model

Preserve these eight responsibility areas without forcing eight agent files when the platform does not support them:

1. Software Development Lead — primary-session coordination, scope, routing, approvals, dependency control, and final evidence aggregation; no self-implementation plus self-approval.
2. Requirements and Planning Specialist.
3. Software Architect.
4. Implementation and Maintenance Engineer.
5. Test and Quality Engineer.
6. Code Quality Reviewer.
7. Engineering Risk Reviewer.
8. Documentation and Release Readiness Specialist.

Implementation, code-quality review, engineering-risk review, and release-readiness assessment must remain distinguishable. No circular delegation or self-review is allowed.

## Mandatory safeguards

- Least privilege.
- Human approval for destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, and irreversible actions.
- No secret exposure.
- No automatic Git mutation, issue/PR submission, deployment, publication, package publication, release, signing, notarization, store submission, purchase, spending, account change, or external communication.
- No hidden scope expansion.
- Evidence-based completion; list every check not executed.
- Independent review after implementation.


## Mandatory platform-specific corrections

1. Make the primary Claude Code session the Software Development Lead through `CLAUDE.md`.
2. Delete `.claude/agents/software-development-lead.md`. A subagent must not own orchestration when the primary session already delegates and aggregates evidence.
3. Retain seven specialist subagents: requirements/planning, architecture, implementation/maintenance, test/quality, code-quality review, engineering-risk review, and documentation/release readiness.
4. Rewrite every retained subagent so it reports only to the primary session, never delegates recursively, never claims final completion, and never reviews its own work.
5. Keep review specialists read-only. Give the implementation specialist only the minimum edit capability supported by the current native format; do not grant unrestricted Bash, network, MCP, deployment, release, signing, publication, or Git mutation authority.
6. Harden `.claude/settings.json`: deny destructive commands, Git mutation, publication, deployment, signing, package publication, secret reads, sensitive key material, and external authentication. Do not add hooks or MCP.
7. Update `CLAUDE.md` with explicit routing and review gates. The primary session plans and delegates; it does not implement substantive changes and approve them itself.
8. Rewrite the eleven workflow documents so each contains domain-specific gates rather than a shared generic template.
9. Remove duplicated role/safety blocks from agent files where `CLAUDE.md` can remain authoritative, while preserving each agent's unique scope, inputs, outputs, tools, stop conditions, and prohibitions.

## Strictly justified deletion policy for this platform

- Delete `.claude/agents/software-development-lead.md`.
- Delete any hook, MCP, command script, executable helper, or unsupported configuration introduced previously.
- Delete obsolete workflow documents only when replaced by a complete corrected version at the same supported/documented location.

## Required corrected target state

The primary Claude Code session is the non-implementing Lead. Seven native specialists perform bounded work and return evidence. Implementation and independent review remain separated. No recursive delegation, active integration, executable hook, or automatic external action exists.


## Required workflow differentiation

Do not keep eleven copies of one generic template. Preserve a common lifecycle only where useful, then add the following exclusive depth:

- `new-feature-development`: validated user/system requirements, acceptance criteria, architecture fit, implementation slices, integration evidence, and feature-specific documentation.
- `bug-investigation-and-correction`: observable symptom, reproducibility, affected versions/paths, root cause, minimal fix, regression test/evidence, and confirmation that symptoms were not merely suppressed.
- `controlled-refactoring`: explicit invariants, unchanged external behavior, bounded transformation, compatibility evidence, and rollback/reversal plan.
- `architecture-change`: decision record, alternatives, boundaries, contracts, migration stages, compatibility, risk review, rollback, and independent architecture approval.
- `api-or-library-evolution`: consumer impact, contract/schema changes, source/binary/behavioral compatibility, versioning, deprecation, migration, and examples.
- `dependency-update`: demonstrated need, provenance, maintenance status, transitive changes, license signals, vulnerability context, compatibility, lockfile impact, and rollback.
- `security-remediation`: threat/weakness, affected trust boundary, exploitability assumptions, secret-safe handling, least-change remediation, regression evidence, and disclosure-safe reporting.
- `performance-and-reliability-improvement`: observed baseline or stated absence of one, hypothesis, resource/concurrency/failure analysis, correctness guardrails, evidence, and regression risk.
- `technical-debt-reduction`: identified debt and impact, prioritization rationale, bounded scope, preserved behavior, measurable improvement, and prevention of unrelated cleanup.
- `maintenance-and-compatibility-update`: supported environments/contracts, compatibility matrix, migrations, deprecations, data/config implications, and fallback.
- `release-readiness-review`: acceptance evidence, unresolved defects/risks, documentation/changelog/migration readiness, artifact/version implications, rollback readiness, and an explicit stop before publication, deployment, signing, or release.


## Required working order

1. Read and inventory only the existing files beneath `claude-code/software-development/` using direct file APIs.
2. Map each existing file to a native purpose and identify unsupported, unsafe, duplicated, misleading, or incomplete content.
3. Apply the mandatory corrections above.
4. Preserve valid content and minimize churn.
5. Perform any strictly necessary deletions only after migrating unique useful content.
6. Reconcile all internal references and README claims.
7. Apply the three static verification passes.
8. Stop with a precise limitation report if a required native format cannot be represented without guessing.


## Static verification

Perform three independent static passes using direct file reads only:

1. **Native pass:** verify each surviving path, file format, field, and claimed loading behavior belongs to this platform surface.
2. **Safety and authority pass:** verify least privilege, human approvals, no self-review, no circular delegation, no inactive safeguard presented as active, and no forbidden executable/integration content.
3. **Completeness and quality pass:** verify the eight responsibilities, fourteen capability areas, eleven differentiated workflows, documentation, limitations, and internal references.

Compare findings, correct them through direct file APIs, then re-read every changed file for a final static verification. Do not use external validators or execute anything.

## Completion response

Return only:

- exact target root;
- files created;
- files modified;
- files deleted;
- files intentionally preserved;
- native mechanisms used;
- unsupported or intentionally omitted mechanisms;
- results of the three static passes;
- unresolved limitations or deletions;
- confirmation that no command, script, build, test, linter, Git action, network call, authentication, integration, hook, or generated configuration was executed.
