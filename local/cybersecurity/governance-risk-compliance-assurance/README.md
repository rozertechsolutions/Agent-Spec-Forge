# Local Cybersecurity GRC Assurance

This specialization defines a local, model/runtime-independent configuration for Cybersecurity Area 01: Governance, Risk, Compliance, and Assurance.

It is a project-defined specification, not a runtime, daemon, API server, installer, provider client, model downloader, MCP server, or autonomous loop. External connections and providers are not configured by this package.

## Native Components

- `local.yaml`: specialization entry point, discovery rules, precedence, lifecycle, routing, and capability negotiation.
- `agents/` and `subagents/`: coordinator and five specialist role manifests.
- `skills/`: reusable GRC capability manifests.
- `workflows/`: four named orchestration processes.
- `tools/`: least-privilege tool contract manifests only.
- `policies/`: permissions, security, evidence handling, and approvals.
- `schemas/`: JSON Schemas for static manifest validation.
- `reference/`: source notes and native capability decisions.

## Unsupported Components

This specialization omits unsupported behavior rather than simulating it:

- No universal adapter, shared cross-platform runtime, active MCP server, provider connection, endpoint, port, credential, model ID, hardware limit, or context-size assumption.
- No executable hooks, scripts, daemons, autonomous loops, external writes, regulator submissions, risk acceptance, compliance certification, publication, deployment, or destructive operations.
- No final-review authority for implementation roles.

## Use

1. Open this directory as the local specialization root.
2. Read `local.yaml` and policies before selecting roles, skills, or workflows.
3. Validate manifests against `schemas/` before use.
4. Enable providers or MCP servers only through separate explicit human review outside this static package.
5. Report unavailable project infrastructure as unavailable, never as passed.
