# Kiro Data and AI Specialization

## Purpose
This package provides a Kiro-native Data and AI specialization for IDE and CLI use. It covers Data and AI strategy, governance, data architecture, datasets, data platforms, analytics, data science, ML, GenAI/RAG, AI applications, operations, responsible AI, and independent assurance.

Supported native surfaces:
- Workspace instructions in `AGENTS.md`.
- Kiro steering files in `.kiro/steering/*.md`.
- Kiro custom agents in `.kiro/agents/*.json`.
- Agent Skills in `.kiro/skills/<skill>/SKILL.md`.

No hooks, specs, Powers, active MCP servers, AWS-specific configuration, credentials, shell automation, deployment tasks, or model/provider settings are configured. Specs are omitted because this package is reusable specialization configuration, not a concrete feature implementation plan.

## Installation and Discovery
Use `kiro/data-ai/` as the Kiro workspace root for Data and AI work, or copy its native artifacts into an existing Kiro workspace using the same relative paths:

- `AGENTS.md`
- `.kiro/steering/*.md`
- `.kiro/agents/*.json`
- `.kiro/skills/*/SKILL.md`

Kiro includes `AGENTS.md` and steering files as persistent context. Custom agents inherit default resources unless the user changes Kiro CLI settings. Skills load on demand when relevant.

## Component Map
`AGENTS.md` defines the workspace-level operating contract and completion gates.

Steering:
- `.kiro/steering/data-ai-core.md`
- `.kiro/steering/data-ai-assurance.md`

Custom agents provide bounded specialist review:
- `data-ai-orchestrator`
- `data-ai-solution-governance-reviewer`
- `data-architecture-dataset-reviewer`
- `data-platform-analytics-reviewer`
- `ml-genai-evaluation-reviewer`
- `ops-risk-assurance-reviewer`

Skills provide reusable procedures:
- `use-case-risk-triage`
- `data-contract-dataset-readiness`
- `pipeline-analytics-quality`
- `ml-genai-evaluation`
- `ops-risk-assurance`

## Invocation and Delegation
Start with `AGENTS.md` and steering. Use the orchestrator for multi-domain Data and AI work, then delegate bounded review to the smallest specialist that owns the concern. Builders may test their own work, but independent evaluation, risk review, release readiness, and final assurance must be handled by a role that did not build the artifact.

Use Skills for repeatable procedures. Use Kiro specs only later for concrete approved features that need requirements/design/tasks tracking; do not create sample specs.

## Permissions and Safety
Custom agents are configured with read-only tools, no MCP servers, and no inherited MCP JSON. This package does not authorize external services, production data access, credential access, MCP tools, model downloads, shell automation, deployment, publishing, signing, spending, destructive operations, or production mutation.

Human review is required for high-impact decisions and any external, destructive, irreversible, expensive, publishing, deployment, signing, submission, credentialed, or production action. Completion status must be exactly `PASS`, `FAIL`, or `BLOCKED`, based only on direct evidence.

## Optional Integrations
Hooks may be added later only for deterministic local validation after explicit approval. MCP and Powers may be enabled later only after review, with credentials outside the repository and with no autonomous production action. Specs may be added later only for concrete implementation work.

## Limitations
Kiro behavior depends on IDE or CLI version, account, plan, workspace trust, feature availability, and resource inheritance settings. Subagents in Kiro do not have access to specs, and hooks do not trigger in subagents. Unsupported capabilities are omitted rather than simulated.

Infrastructure provisioning, cybersecurity operations, penetration testing, production deployment, and cloud administration remain outside this specialization. This package owns Data and AI operational requirements, risk assumptions, evaluation, monitoring specifications, and rollback criteria.

## Verification
Maintainers may run these checks from the repository root:

```sh
find kiro/data-ai -type f | sort
find kiro/data-ai -type f -name '*.md' -exec test -s {} \;
for f in kiro/data-ai/.kiro/agents/*.json; do jq empty "$f" || exit 1; done
for f in kiro/data-ai/.kiro/skills/*/SKILL.md; do d=$(basename "$(dirname "$f")"); grep -q "^name: $d$" "$f" || exit 1; done
for f in kiro/data-ai/.kiro/steering/*.md kiro/data-ai/.kiro/skills/*/SKILL.md; do sed -n '1p' "$f" | grep -q '^---$' || exit 1; done
find kiro/data-ai -type f \( -name '*.py' -o -name '*.sh' -o -name '*.js' -o -name '*.ts' -o -name '*.yml' -o -name '*.yaml' \) -print
```

Expected result: native Kiro files are present, Markdown artifacts are non-empty, agent JSON is valid, steering and Skill frontmatter exists, Skill names match directories, no scripts or active integration configs exist, and local scans return no placeholder markers, credentials, private key material, or real secrets.
