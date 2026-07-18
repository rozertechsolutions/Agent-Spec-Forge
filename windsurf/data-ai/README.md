# Windsurf / Cascade Data and AI

This package implements the Data and AI specialization for Windsurf/Cascade using current repository-native Cascade surfaces. It is neutral across data platforms, warehouses, lakehouses, BI tools, model providers, vector stores, orchestration tools, and ML/GenAI frameworks.

## Supported Native Surface

- `AGENTS.md`: location-based persistent project instructions for Cascade.
- `.windsurf/rules/data-ai-human-review-gate.md`: conditional rule for high-impact, external, destructive, or risk-accepting Data and AI actions.
- `.windsurf/skills/*/SKILL.md`: workspace Skills for reusable Data and AI procedures.
- `.windsurf/workflows/*.md`: slash-command workflow prompts for lifecycle work with explicit invocation value.
- `.windsurf/hooks.json` and `.windsurf/hooks/data_ai_guard.py`: deterministic local hooks that block unsafe command, MCP, write, and prompt patterns.

Memories, active MCP servers, app deploys, previews, analytics configuration, credentials, global/system hooks, enterprise administration, and account settings are intentionally omitted.

## Installation and Discovery

1. Open Windsurf/Devin Desktop in this repository or directly in `windsurf/data-ai`.
2. Cascade reads the nearest `AGENTS.md` for this specialization.
3. Workspace Skills are available from `.windsurf/skills`; ask Cascade what Skills it can use if discovery is unclear.
4. Workflows under `.windsurf/workflows` are available as manual slash-command workflows when the workspace is loaded.
5. Hooks are configured by `.windsurf/hooks.json` and run locally when Windsurf invokes the matching hook events.

## Component Map

- `AGENTS.md`: scope, operating model, routing, separation of duties, safety, and completion gates.
- `data-ai-human-review-gate`: conditional rule for human approval and risk acceptance.
- `use-case-risk-triage`: intake, feasibility, impact, value, alternatives to AI, and risk classification.
- `data-contract-dataset-readiness`: contracts, schemas, semantics, governance, provenance, collection, annotation, leakage, splits, and dataset acceptance.
- `data-platform-analytics-quality`: pipelines, data products, quality, reliability, lineage, observability, metrics, BI, and decision intelligence.
- `analytics-experiment-review`: analytics, statistics, causal inference, uncertainty, calibration, segmentation, experiment design, and metric certification.
- `ml-genai-system-evaluation`: ML, RAG, prompts, agents, inference, model comparison, red-team evidence, groundedness, safety, and release-candidate evaluation.
- `ops-risk-assurance`: MLOps, LLMOps, monitoring, drift, provider/model change, incidents, rollback, retirement, deletion/rectification, responsible AI risk, and independent assurance.
- `data_ai_guard.py`: deterministic guard for blocked commands, protected files, active MCP use, secret-shaped input, and unsafe prompt requests.

## Invocation and Delegation

Start with `use-case-risk-triage` for new or ambiguous work. Invoke focused Skills for reusable complex procedures. Use Workflows when the task spans multiple Skills and a named slash command is useful. Builders return evidence to an independent reviewer before release-readiness or final assurance. Completion status is exactly `PASS`, `FAIL`, or `BLOCKED`.

## Permissions and Safety

Use restrictive Cascade permissions for this specialization:

- Code edits: ask before applying changes unless the user explicitly authorized the current scoped edit.
- Terminal commands: ask before running commands that write files, install dependencies, contact networks, mutate Git, deploy, publish, download models, access credentials, or touch production.
- MCP: disabled by default; do not add `mcp_config.json` without explicit server-level authorization.
- Memories: omitted; do not store persistent memory containing project data, private data, or sensitive conclusions.
- Hooks: workspace-local deterministic safety hooks only; no global/system hooks.

Human review is required before high-impact decisions, provider/model selection, risk acceptance, policy exceptions, external integration activation, destructive actions, production changes, releases, publication, spending, signing, submission, or access expansion.

## Optional Integrations

MCP servers, data catalogs, warehouses, BI tools, experiment trackers, vector stores, model registries, observability systems, app previews, app deploys, and analytics integrations remain disabled. Enable them manually only after the human provides allowed scope, data boundaries, credentials handling instructions, server definitions, and approval rules.

## Limitations

Behavior depends on the installed Windsurf/Devin Desktop version, account plan, model settings, workspace trust, indexing, and OS hook execution. This package does not authenticate Windsurf, configure Devin Local, run model inference, inspect production systems, contact external APIs, or prove live platform loading. Cascade and Devin Local are distinct products; this package targets Cascade repository behavior only.

## Maintainer Verification

Run these repository-local checks:

```bash
find windsurf/data-ai -type f | sort
find windsurf/data-ai -type f -name '*.md' -exec test -s {} \;
python3 -m json.tool windsurf/data-ai/.windsurf/hooks.json >/dev/null
python3 - <<'PY'
from pathlib import Path
compile(Path('windsurf/data-ai/.windsurf/hooks/data_ai_guard.py').read_text(), 'data_ai_guard.py', 'exec')
for path in Path('windsurf/data-ai/.windsurf/skills').glob('*/SKILL.md'):
    text = path.read_text()
    assert text.startswith('---\n'), path
    assert '\nname:' in text and '\ndescription:' in text, path
print('windsurf data-ai static validation ok')
PY
test ! -e windsurf/data-ai/mcp_config.json
find windsurf/data-ai -type f \( -name '.DS_Store' -o -name '._*' -o -name 'AUDIT.md' -o -name 'VALIDATION.md' -o -name 'REPORT.md' \) -print
```
