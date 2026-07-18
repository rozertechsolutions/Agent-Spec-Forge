# Cline Data and AI

This package implements a Cline project-scoped Data and AI specialization using current native configuration: workspace rules in `.clinerules/`, project Skills in `.cline/skills/`, and `.clineignore` for sensitive/generated paths. It does not include project agent definitions because current Cline subagents are experimental read-only research agents rather than configurable implementation agents. It includes no hooks, MCP servers, plugins, schedules, cron jobs, Kanban automation, provider settings, credentials, or broad auto-approval configuration.

## Installation And Discovery

Use this directory as the Cline workspace root for Data and AI specialization work, or copy its contents into a Cline workspace only when the specialization should govern that workspace.

- `.clinerules/*.md`: Cline loads these as persistent workspace rules.
- `.cline/skills/*/SKILL.md`: Cline discovers these as project Skills; each Skill directory name matches its `name` frontmatter.
- `.clineignore`: prevents routine Cline context collection from including common sensitive or generated paths.

Keep approval requirements enabled in the Cline IDE/CLI. Do not enable auto-approval for writes, commands, MCP tools, browser actions, destructive actions, or external actions merely because this package is installed.

## Component Map

- `00-data-ai-core.md`: Data and AI scope, responsibility routing, lifecycle coverage, safety rules, and completion status requirements.
- `90-data-ai-assurance.md`: independent evidence review, separation of duties, risk review, waiver, release-readiness, rollback, retirement, and final assurance rules.
- `use-case-risk-triage`: intake, value, alternatives to AI, feasibility, impact, ownership, routing, and stop conditions.
- `data-contract-dataset-readiness`: governance, contracts, schemas, semantics, source provenance, labeling, synthetic data, leakage checks, and dataset acceptance.
- `pipeline-analytics-quality`: data products, pipelines, quality, reliability, lineage, observability, governed metrics, analytics, BI, and change control.
- `ml-genai-evaluation`: data science, experiments, ML, RAG, GenAI, agents, inference contracts, validation, red-team findings, and candidate evidence.
- `ops-risk-assurance`: MLOps/LLMOps readiness, monitoring, incidents, rollback, retirement, responsible AI, model risk, supplier risk, and final assurance.

For broad repository discovery, Cline may use its built-in read-only subagents when enabled. Treat subagent findings as research input only; subagents cannot edit, use MCP, browse, or approve work.

## Invocation And Delegation

Use Cline rules for all Data and AI work. Invoke Skills with slash commands or rely on Cline's matching when a focused workflow is needed. The coordinator may route and aggregate evidence, but builders cannot certify their own quality, risk, or release readiness. Responsible AI/model risk review and independent assurance must remain separate from implementation.

## Permissions, Approval, And Safety

Operate with least privilege and minimum necessary context. Human approval is required for high-impact decisions, external writes, destructive or irreversible operations, production use, dependency/provider/model adoption, publishing, signing, submission, spending, deployment, risk acceptance, legal/privacy escalation, and release readiness.

Never expose sensitive datasets, secrets, credentials, private endpoints, proprietary prompts, personal data, or production records. Never fabricate data quality results, statistical significance, causal claims, model metrics, benchmarks, costs, latency, robustness, fairness, compliance status, lineage, monitoring state, or runtime validation.

## Optional Integrations

MCP servers, plugins, connectors, schedules, Kanban automation, external providers, notebooks, warehouses, BI tools, catalogs, registries, vector stores, and observability systems must be enabled manually outside this package. Store secrets outside the repository, review each tool call, limit auto-approval, and prefer read-only access until a human explicitly authorizes writes.

## Limitations

Cline behavior depends on IDE, CLI, SDK, extension version, model/provider configuration, command permissions, auto-approval settings, and experimental feature availability. Project agent schemas and hooks are intentionally omitted because the prompt requires only stable native value. This package does not validate live Cline behavior, execute model inference, authenticate services, or connect external tools.

## Maintainer Verification

Run these checks from the repository root:

```bash
find cline/data-ai -type f | sort
find cline/data-ai -type f -name '*.md' -print0 | xargs -0 -n1 sh -c 'test -s "$0"'
find cline/data-ai -type f \( -name '*.json' -o -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.py' \) -print
git diff -- cline/data-ai
```

Expected result: Markdown rules and Skills are non-empty, no hooks/plugins/MCP/provider configs or executable scripts exist, and changes are limited to `cline/data-ai`.
