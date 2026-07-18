# Master Implementation Prompt — DevOps and Cloud — 01 Leadership and Architecture

You are implementing exactly one validated section of the open-source **AI Specialized Departments** repository.

Your task is to implement **Leadership and Architecture** sequentially across the supported platform packages. Work autonomously within the rules below. Do not ask for confirmation unless repository safety makes progress impossible. Do not begin another DevOps and Cloud section.

## Repository and execution contract

- Repository: **AI Specialized Departments**.
- Working branch: **`feature/devops-cloud`**.
- This is the first section. Create `feature/devops-cloud` from the latest `main` if the branch does not already exist. If it already exists locally or remotely, switch to it and verify that its merge base is `main`; do not recreate it.
- A Git branch inherits the files and history from `main`; do not duplicate them. The diff against `main` must contain only DevOps and Cloud work.
- Allowed implementation scope: files under **`<platform>/devops-cloud/`** for the platforms listed below. Existing central files inside that specialization package may be updated only when the current section must register a native rule, agent, Skill, workflow or routing entry.
- Do not modify another specialization, another platform outside its own DevOps and Cloud package, root project governance, licenses or unrelated documentation.
- Git commands required for status, branch management, diff review, commit and push are allowed. Do not use Git to conceal, reset or overwrite unrelated user changes.
- Do not install software, plugins, runtimes, models or dependencies.
- Do not execute platforms, cloud CLIs, Docker, Kubernetes, Jenkins, Terraform, OpenTofu, Pulumi, Ansible, scanners, hooks, MCP servers, scripts, builds, tests, validators, containers, pipelines, deployments or infrastructure commands.
- Do not authenticate to any platform or cloud account. Do not read credentials or environment secrets.
- Use repository file operations for static generation and inspection. Validation is textual and structural only.
- No production mutation, external publication, spending, signing, deployment or destructive action.
- No secret, token, credential, private URL, real endpoint, account ID, subscription ID, project ID or environment-specific value.
- External integrations and MCP definitions must remain absent or disabled by default. Create one only if the platform has a current, project-scoped native format and the section obtains clear value from it.
- Hooks may be authored only in a current native format, must be safe by default, and must not be run during this task.
- Never claim that a build, test, deployment, failover, scanner, policy or integration was executed.

## Section contract

    **Section:** `01-leadership-architecture`  
    **Mission:** Establish the governing architecture, operating model and decision system for the entire DevOps and Cloud department without taking ownership away from specialist sections.

    ### Roles and non-overlapping ownership

    | Role | Exclusive ownership |
|---|---|
| `DevOps and Cloud Orchestrator` | Owns intake, decomposition, routing, dependency control, escalation and section-level coordination. It must not implement specialist work or approve its own output. |
| `Cloud and Platform Architect` | Owns cloud/platform architecture, provider-neutral design, architecture decisions, standards, target-state models, technology selection and cross-section technical boundaries. |

    Every native role/agent representation must define:

    - Exact mission and exclusive scope.
    - Primary ownership and boundaries.
    - Inputs and preconditions.
    - Outputs and evidence.
    - Allowed tools and permissions.
    - Dependencies and handoffs.
    - Invocation and delegation conditions.
    - Stop conditions.
    - Errors handled and failure behavior.
    - Completion criteria.
    - Human-review requirements.
    - Explicitly prohibited actions.

    ### Required professional coverage

    - Request intake, classification, prioritization and routing
- Cloud, hybrid, multicloud and platform architecture
- Architecture Decision Records and decision traceability
- Technology evaluation and selection criteria
- Environment, ownership and responsibility models
- Standards, guardrails, exception handling and escalation
- Dependency maps and cross-section handoff contracts
- Well-Architected assessment across operations, security, reliability, performance, cost and sustainability

    ### Explicit exclusions

    - Detailed IaC implementation, pipeline design, Kubernetes implementation or observability implementation
- Self-approval or self-review
- Enterprise cybersecurity governance, legal approval or financial authorization

    ### Technology knowledge to cover without creating one agent per product

    - AWS, Azure and Google Cloud architecture frameworks
- Hybrid and multicloud decision models
- Architecture Decision Records, C4-style context and deployment views where useful
- Service ownership, RACI and platform-as-a-product governance

    Technology names normally belong in Skills, reference knowledge, workflows, templates and review criteria. Create a product-specific agent only when current platform capabilities and a genuinely exclusive responsibility justify it.

## Minimum conceptual assets for this section

    The implementation must represent the following concepts through each platform's real native mechanisms. Do not force identical file counts or directories.

    ### Specialist capabilities

    - devops-cloud-request-triage
- cloud-architecture-assessment
- architecture-decision-record
- technology-selection-and-tradeoff-analysis
- well-architected-review

    ### Professional workflows

    - new-devops-cloud-request
- cloud-target-architecture
- technology-selection
- architecture-exception-review
- cross-section-dependency-resolution

    ### Section quality gates

    - Every responsibility has one primary owner
- Every architecture decision records context, alternatives, tradeoffs, risks and review status
- No provider is selected without explicit requirements
- No specialist implementation detail is duplicated

    At minimum, the section must provide:

    1. Persistent section instructions or knowledge.
    2. Every justified specialist role, represented as a native agent/subagent/custom mode when supported, or as precise project instructions when agents are unsupported.
    3. Reusable Skills only where the platform supports Skills or an equivalent native reusable mechanism.
    4. The listed workflows in a native workflow/command/spec/Skill format, or as clearly executable manual procedures for UI-only platforms.
    5. Human-approval, least-privilege and prohibited-action controls.
    6. Static completion and evidence criteria.
    7. A coherent route from the section's inputs to its outputs without circular delegation or self-review.

## Fixed platform sequence

1. **`chatgpt/`** — ChatGPT Projects, project instructions and knowledge, GPT configuration, Skills and Workspace Agents only when currently available to the relevant plan. Repository output is an import/manual-setup package; never invent repository-native ChatGPT agent files.
2. **`claude/`** — Claude Projects, project instructions, project knowledge, custom Skills and connectors. Keep this separate from Claude Code and represent UI-only setup as importable documentation rather than fake repository configuration.
3. **`claude-code/`** — CLAUDE.md, project settings, subagents, Agent Skills, hooks, permissions and project MCP configuration only in current official formats.
4. **`cline/`** — Project rules/configuration, Skills, workflows, agents/subagents, hooks and MCP only where the current Cline product surface supports project-scoped, version-controlled files.
5. **`codex/`** — AGENTS.md, project configuration, subagents, Agent Skills, hooks, permissions and MCP using current Codex-native formats.
6. **`cursor/`** — Project Rules/AGENTS.md, subagents, Agent Skills, hooks and MCP using current Cursor-native project paths and schemas.
7. **`gemini-cli/`** — GEMINI.md and current project-scoped Gemini CLI settings, commands, agents, Skills, hooks, extensions and MCP only when verified in current official documentation.
8. **`github-copilot/`** — Repository custom instructions, path-specific instructions, custom agents, Agent Skills, hooks and MCP only for the exact current Copilot surface being targeted.
9. **`junie/`** — AGENTS.md/Junie guidelines, Agent Skills and project MCP configuration. Do not invent hooks or custom-agent files if the current Junie surface does not support them.
10. **`kilo-code/`** — Kilo Code rules, custom modes/agents, Skills, workflows and MCP only in current supported project formats.
11. **`kiro/`** — Steering, AGENTS.md, specs, custom agents, Agent Skills, hooks, Powers and MCP only when they are genuinely native and useful for the section.
12. **`local/`** — A provider-independent static specification/configuration package. Providers, runtimes, models, endpoints, tools and permissions must remain configurable and disabled by default; do not bind to Ollama, LM Studio or any model.
13. **`mistral-vibe/`** — AGENTS instructions plus current Vibe project configuration for agents, Skills, prompts, hooks, tools, approval rules and MCP where supported.
14. **`openai-agents-sdk/`** — Real, minimal SDK source code, schemas, guardrails, handoffs and static tests/examples may be authored, but nothing may be installed, executed, served or deployed.
15. **`opencode/`** — OpenCode configuration, primary agents/subagents, Agent Skills, commands, permissions, plugins and MCP only in current official project formats.
16. **`qwen-code/`** — QWEN.md plus current Qwen Code project agents, subagents, Agent Skills, hooks, commands, settings and MCP where officially supported.
17. **`warp/`** — AGENTS.md project rules, Skills, agent profiles/permissions, Warp Drive exportable artifacts and MCP only where a repository-scoped or importable native format exists. Do not fabricate cloud-agent configuration.
18. **`windsurf/`** — AGENTS.md, workspace Rules, Skills, Workflows, hooks and MCP using current Windsurf-native project formats.

## Mandatory sequential implementation algorithm

Perform the following process **one platform at a time in the exact order listed later**. Never start the next platform until the current platform passes all three static verification passes.

### Phase 0 — Git and scope preflight

1. Inspect Git status and current branch.
2. Protect any unrelated user changes. Do not reset, stash, amend, rewrite or include them.
3. Prepare or select `feature/devops-cloud` according to this section's branch rule.
4. Compare the branch to `main` and confirm that existing branch changes are limited to DevOps and Cloud work.
5. Stop if the repository is in a conflicted state or if safe isolation is impossible.

### Phase 1 — Current official documentation verification

For the current platform:

1. Identify the current product surface, version/release channel when available, plan limitations and repository-scoped configuration mechanisms.
2. Consult current official documentation. Use the supplied documentation baseline only as a starting point.
3. Build a working capability classification for instructions, agents/subagents, Skills, workflows/commands/specs, hooks, permissions, MCP and other relevant mechanisms.
4. Classify each candidate as `native`, `UI/import-only`, or `unsupported`.
5. Do not create an `unsupported` file or folder. Unsupported mechanisms are omitted.
6. Community sources may clarify ambiguous behavior but cannot establish support by themselves.

### Phase 2 — Platform plan

Before writing:

1. Inspect only the current platform's existing `devops-cloud/` package and the minimum parent context needed to avoid conflicts.
2. Determine the exact native files to create or update.
3. Map every file to a section responsibility, Skill, workflow or safety control.
4. Remove planned duplicates, empty files, decorative placeholders and generic content.
5. Confirm that central specialization instructions will be extended rather than overwritten when earlier sections already exist.
6. Confirm that all output stays below `<platform>/devops-cloud/`.

### Phase 3 — Static implementation

1. Create the smallest professionally complete native implementation.
2. Preserve conceptual consistency with other platforms without copying their structure.
3. Use exact role ownership and section boundaries from this prompt.
4. Include technology-specific references only where they improve professional execution.
5. Keep examples generic and safe. Use environment-variable names or documented user-supplied fields only when a real schema requires them.
6. Do not activate integrations, approvals, broad permissions or auto-execution.
7. Do not create executable deployment automation merely to demonstrate the section.
8. For `openai-agents-sdk/`, author real minimal SDK code and schemas only; do not create a server, UI, deployment or installer.
9. For `local/`, create a provider-neutral static specification with disabled provider/tool examples; do not choose a runtime or model.
10. For `chatgpt/` and `claude/`, create importable/manual setup packages for actual Project/GPT/Skill/knowledge surfaces. Do not pretend they automatically read repository files.

### Phase 4 — Three independent static verification passes

**Pass A — Professional completeness**

- Verify every required responsibility, role, Skill, workflow, boundary and quality gate.
- Verify that the content is specific to `Leadership and Architecture`, not generic DevOps filler.
- Verify that technology coverage is sufficient without fragmenting agents by vendor.

**Pass B — Native-platform correctness**

- Re-check every created path, filename, front matter, schema and mechanism against current official documentation.
- Remove anything unsupported, legacy-only without justification, UI-only represented as repository-native, or copied from another platform.
- Confirm plan, product-surface and project-scope limitations are accurately documented.

**Pass C — Safety, precision and maintainability**

- Check least privilege, human approval, no secrets, no active MCP, no automatic production action and no runtime-validation claims.
- Check all role contracts for inputs, outputs, permissions, handoffs, stop conditions, failure behavior and prohibited actions.
- Check for duplicate authority, circular delegation, self-review, contradictions, empty files and placeholders.
- Confirm no unrelated files changed.

Compare the three pass results, consolidate corrections, then repeat a final static inspection. If any pass fails, correct the current platform and restart all three passes for that platform. Do not advance with partial validation.

### Phase 5 — Section-wide consolidation

After all platforms are processed:

1. Compare implementations for conceptual consistency and native differences.
2. Re-check that no unsupported component was forced onto any platform.
3. Re-check that every recommended platform received useful coverage or was omitted for a defensible native/value reason.
4. Review the entire diff against `main`.
5. Ensure no platform or specialization outside DevOps and Cloud was changed.
6. Do not create an empty commit.

### Phase 6 — Commit and push

After full section validation only:

1. Stage only this section's intended DevOps and Cloud changes.
2. Review the staged diff.
3. Commit with:
   **`feat(devops-cloud): implement 01 leadership architecture`**
4. Push `feature/devops-cloud` to its remote.
5. Do not merge into `main`; the final audit prompt owns the merge.
6. Do not delete the branch locally or remotely.

### Final response

Report:

- Platforms implemented.
- Platforms intentionally omitted and the precise native/value reason.
- Files created and updated by platform.
- Native mechanisms used.
- Static verification results for Passes A, B and C.
- Commit hash and push result.
- Any remaining human setup, plan limitation or unresolved risk.

Do not report runtime success.

## Absolute stop conditions

Stop without committing or pushing when:

- The working tree contains unrelated changes that cannot be safely isolated.
- The dedicated branch is missing for Sections 02–10.
- The repository is conflicted or the merge base is unsafe.
- Current official documentation cannot confirm a proposed native mechanism.
- A requested component would require installation, authentication, execution, deployment or a real secret.
- Static verification still fails after correction.
- The staged diff contains anything outside the intended DevOps and Cloud scope.
