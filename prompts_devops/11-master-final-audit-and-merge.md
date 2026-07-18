# Master Final Audit and Merge Prompt — DevOps and Cloud

You are performing the final static audit of the complete **DevOps and Cloud** specialization in the **AI Specialized Departments** repository. All ten section prompts should already have been completed on `feature/devops-cloud`.

Do not treat prior completion reports as proof. Re-read the repository files and current official platform documentation. Correct defects on the feature branch, repeat the audit, and merge only after every gate passes.

## Required sections

1. `01-leadership-architecture` — Leadership and Architecture
2. `02-cloud-foundation-infrastructure` — Cloud Foundation and Infrastructure
3. `03-ci-cd-release-engineering` — CI/CD and Release Engineering
4. `04-containers-platform-engineering` — Containers and Platform Engineering
5. `05-sre-observability-operations` — SRE, Observability and Operations
6. `06-resilience-disaster-recovery` — Resilience and Disaster Recovery
7. `07-performance-capacity-efficiency` — Performance, Capacity and Efficiency
8. `08-devsecops` — DevSecOps
9. `09-finops-sustainability` — FinOps and Sustainability
10. `10-assurance-review` — Assurance and Independent Review

## Platforms

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

## Non-negotiable operating rules

- Work on `feature/devops-cloud` until the audit is fully complete.
- Git commands for inspection, branch management, commits, push and merge are allowed.
- Do not install or execute any platform, dependency, script, hook, MCP server, cloud CLI, Docker/Kubernetes command, pipeline, build, test, scanner, validator, deployment or infrastructure tool.
- Do not authenticate to cloud or AI services.
- Do not expose or request credentials, tokens, endpoints or real identifiers.
- Perform textual and structural validation only.
- Do not modify unrelated specializations or files.
- Do not delete the feature branch locally or remotely.
- Never convert static inspection into a claim of runtime validation.

## Phase 1 — Repository and Git isolation

1. Fetch Git refs and switch to `feature/devops-cloud`.
2. Confirm the branch exists, is based on `main`, and contains no unresolved conflicts.
3. Inspect `git status` and protect unrelated user work.
4. Review the complete diff from `main`.
5. The intended implementation diff may contain only DevOps and Cloud package files below the platform directories. Any related correction must remain in those packages.
6. Stop if unrelated changes cannot be safely isolated.

## Phase 2 — Independent audit pass A: professional coverage

For every platform and section:

1. Verify that the section mission is represented.
2. Verify all justified roles and exclusive ownership.
3. Verify inputs, preconditions, outputs, permissions, dependencies, invocation, delegation, stop conditions, error behavior, completion, human review and prohibited actions.
4. Verify required Skills and workflows are present through native mechanisms or precise instructions where agents/Skills are unsupported.
5. Verify Docker, Kubernetes, Jenkins, cloud providers, IaC, observability, resilience, performance, DevSecOps and FinOps knowledge appears in the correct sections rather than as arbitrary product agents.
6. Verify no professional capability has been omitted merely to make structures uniform.
7. Verify DevSecOps is integrated but does not absorb pentesting, SOC, threat intelligence, forensics, enterprise GRC or general security incident response.

Record every finding with platform, section, file, evidence, severity, owner and closure criterion.

## Phase 3 — Independent audit pass B: current native-platform accuracy

For each platform:

1. Re-check current official documentation and product surface.
2. Verify every instruction, agent/subagent, Skill, workflow/command/spec, hook, permission and MCP file path/schema.
3. Verify `chatgpt/` and `claude/` contain honest import/manual packages and no fake repository-native agents.
4. Verify `claude-code/`, `codex/`, IDE and CLI platforms use only their own current native formats.
5. Verify `openai-agents-sdk/` contains real minimal SDK implementation artifacts without server, UI, installer or deployment.
6. Verify `local/` is provider/runtime/model neutral with integrations disabled by default.
7. Remove unsupported, obsolete, copied, simulated, placeholder-only or empty files.
8. Do not require identical file structures between platforms.

If a mechanism cannot be confirmed through current official documentation, remove it or replace it with a supported mechanism and restart this pass.

## Phase 4 — Independent audit pass C: safety, coherence and evidence

Verify:

- No secrets, credentials, tokens, real endpoints, private URLs or account identifiers.
- No default-active MCP, connector or external integration.
- No automatic production, deployment, signing, spending, publication or destructive action.
- Human approval for privileged, destructive, costly and externally visible actions.
- Least privilege and narrowly scoped tools.
- No circular delegation, hidden overlap or self-review.
- No conflicting authority between sections.
- No unverified claims of deployment, availability, rollback, recovery, compliance or test success.
- No unrelated repository changes.
- No empty files, generic filler or artificial `unsupported` directories.
- Central specialization instructions route cleanly to section assets without contradictions.
- Every platform package is internally coherent and maintainable.

## Phase 5 — Consolidation and restart rule

1. Compare Passes A, B and C.
2. Correct every critical or high-severity finding and every completeness/native-support defect.
3. Re-run all three passes from the beginning after any correction that affects ownership, structure, permissions or platform-native validity.
4. Medium and low findings may remain only when they are explicitly non-blocking, evidenced and require later human/UI configuration.
5. Do not accept partial validation.

## Phase 6 — Final diff and feature-branch completion

1. Review the full diff against `main`.
2. Use Git's own diff checks where useful, but do not run external validators.
3. Ensure every prior section commit is present or its equivalent content is present.
4. If audit corrections were required, stage only those DevOps and Cloud changes, review the staged diff, commit them with:
   `fix(devops-cloud): resolve final audit findings`
5. Push `feature/devops-cloud`.
6. Confirm the feature branch working tree is clean.

## Phase 7 — Merge to main

Merge only when all blocking findings are closed:

1. Switch to `main`.
2. Update `main` using a safe fast-forward pull.
3. Reconfirm that the feature branch diff contains only intended DevOps and Cloud work.
4. Merge with a non-fast-forward merge commit:
   `merge: add DevOps and Cloud specialization`
5. If conflicts occur, stop and report them; do not improvise destructive conflict resolution.
6. Push `main`.
7. Confirm the merge and remote push.
8. Preserve `feature/devops-cloud` locally and remotely. Do not delete it.

## Required final report

Report concisely:

- Audit status for Passes A, B and C.
- Coverage by section and platform.
- Platforms or components intentionally omitted with current native/value justification.
- Findings corrected.
- Remaining non-blocking limitations or manual UI setup.
- Feature-branch correction commit, when applicable.
- Merge commit and `main` push result.
- Confirmation that `feature/devops-cloud` was preserved.
- Explicit statement that validation was static and no DevOps/cloud platform or generated configuration was executed.

If any blocking requirement fails, do not merge.
