# AI Specialized Departments — Kilo Code Software Development Correction Prompt

## Exact target root

`kilo-code/software-development/`

## Purpose

Correct the existing **Software Development** implementation for **Kilo Code** in place.

**Previous audit result:** `PASS WITH MAJOR CORRECTIONS`  
**Selected product surface:** `AGENTS.md`, `kilo.jsonc`, `.kilo/rules/`, `.kilo/agents/`, `.kilo/skills/`, and native custom commands under `.kilo/commands/`


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

1. Make the primary Kilo Code agent the Software Development Lead through `AGENTS.md` and rules.
2. Delete `.kilo/agents/software-development-lead.md`.
3. Retain seven specialist subagents with current native Markdown frontmatter. Reviewers/planners must deny edits and shell; implementation edits must be approval-gated; all specialists must deny shell, web, MCP, Git mutation, deployment, publication, signing, and release actions.
4. Correct `kilo.jsonc`:
   - remove the current `$schema` value unless it is the exact official schema URI already verified by the current native format;
   - keep `"*": "ask"` as the broad fallback before narrower rules;
   - keep Bash and web fetch denied;
   - keep edits as ask/approval-gated;
   - do not add providers, models, MCP, hooks, endpoints, or credentials.
5. Convert each complete `docs/workflows/*.md` workflow into a native `.kilo/commands/*.md` command using current documented frontmatter and prompt-only content.
6. After verifying one-to-one migration and preserving all unique content, delete `docs/workflows/` to avoid duplicate authority.
7. Deepen the eleven native commands with unique gates and evidence.
8. Update all agents to report to the primary agent, not to another subagent, and prevent recursive delegation.
9. Preserve `.kilo/skills/` but remove executable resources and duplicated global policy prose.
10. Update `README.md` to describe the current format and the migration from auxiliary docs to native commands.

## Strictly justified deletion policy for this platform

- Delete `.kilo/agents/software-development-lead.md`.
- Delete the invalid or unverified `$schema` property from `kilo.jsonc`.
- Delete `docs/workflows/` only after complete migration to `.kilo/commands/`.
- Delete legacy `.kilocodemodes`, hooks, MCP configuration, scripts, and unsupported agent files.

## Required corrected target state

Kilo's primary agent is Lead; seven native specialist subagents are permission-bounded; eleven workflows are native `.kilo/commands/`; no duplicate auxiliary workflow tree or questionable schema reference remains.


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

1. Read and inventory only the existing files beneath `kilo-code/software-development/` using direct file APIs.
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
