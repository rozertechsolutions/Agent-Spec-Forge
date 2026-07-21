# Cybersecurity Department for Windsurf and Devin Local

This Cybersecurity department is a professional, reusable baseline for Windsurf Cascade and Devin Local/CLI. It helps humans produce evidence-based cybersecurity artifacts for governance, risk, compliance, and assurance; security architecture and engineering; application, product, and DevSecOps security; exposure, vulnerability, and hardening management; defensive operations, detection, and threat intelligence; incident response, DFIR, and recovery; authorized offensive validation; and cyber resilience with specialized technologies.

It solves the problem of giving Cascade or Devin Local scoped, repository-owned cybersecurity instructions and Skills without granting automatic authority to scan, exploit, deploy, change production, approve risk, close incidents, or connect external systems. Realistic uses include risk reviews, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection planning, incident readiness, authorized assessment planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight area packages under `windsurf/cybersecurity/<area>/`. Each area has an `AGENTS.md` file for directory-scoped instructions and Windsurf workspace Skills in `.windsurf/skills/<skill-name>/SKILL.md`. The platform-level `.devin/config.json` is retained for Devin Local/CLI sessions launched from this department and sets conservative project permissions.

The AI is not authorized to accept enterprise risk, approve exceptions, authorize offensive testing, perform live scans, run incident containment, complete recovery, change production, publish external statements, make legal determinations, approve its own work, or claim execution without evidence. Human owners remain accountable for authorization, approvals, risk acceptance, incident command, production action, external reporting, and final decisions.

## Possible uses

- Review policies, control mappings, exceptions, third-party evidence, and compliance gaps.
- Review designs, identity/network/cloud/data controls, reference patterns, and security engineering decisions.
- Support threat modeling, secure design review, supply-chain review, CI/CD evidence review, and PSIRT planning.
- Triage vulnerability and exposure evidence, plan hardening, and prepare remediation governance.
- Design telemetry, detection logic, triage methods, threat hunts, and intelligence handoffs.
- Prepare incident response plans, DFIR evidence handling, containment options, recovery plans, and lessons learned.
- Plan explicitly authorized penetration tests, Red Team exercises, Purple Team validation, retests, and rules of engagement.
- Assess resilience, backup/recovery readiness, OT/ICS, IoT, AI security, firmware, cryptography, and critical infrastructure concerns.

## Platform compatibility

Validated documentation date: 2026-07-21.

Supported native surfaces in this package:

- Windsurf/Devin Desktop Cascade: `AGENTS.md` files, `.windsurf/skills/<skill-name>/SKILL.md`, and optional workspace hooks at `.windsurf/hooks.json` if an organization creates them later. This package does not ship hooks.
- Devin Local and Devin CLI: `.devin/config.json`, `AGENTS.md`, and imported Windsurf Skills/rules when `read_config_from.windsurf` is enabled.
- Shared rule behavior: `AGENTS.md` is recognized by Cascade and Devin CLI as project or directory-scoped rule context.

Not included: repository-defined Windsurf custom agents, Devin cloud schedules, cloud Devins, MCP servers, connectors, scanner integrations, deployment automation, live hooks, credentials, or provider-specific runtime state.

Devin Local is a preview local agent surface in Devin Desktop. Devin CLI requires a Devin account and local CLI installation. Cascade availability depends on the installed Devin Desktop/Windsurf release, workspace trust, organization controls, and plan/admin policy.

## Prerequisites

- Devin Desktop/Windsurf with Cascade for Cascade use, or Devin CLI/Devin Local for the `.devin` configuration path.
- A trusted workspace opened at the selected area directory when using area Skills.
- No committed secrets, API keys, tokens, private endpoints, personal data, or confidential evidence.
- Explicit authorization and approved scope before any cybersecurity analysis that could affect live systems or third parties.

## Installation or import

For Windsurf Cascade:

1. Open the selected area directory as the workspace, for example `windsurf/cybersecurity/application-product-devsecops-security/`.
2. Confirm Cascade sees that directory's `AGENTS.md`.
3. Use natural language or an `@skill-name` mention to invoke an area Skill from `.windsurf/skills/`.
4. Provide redacted evidence, authorized scope, exclusions, owner, intended audience, and required decision.

Example Cascade request:

```text
@threat-modeling Review this proposed payment-service design from the supplied diagram and ADRs. Scope is design review only. No live testing, no connector use, and no production changes are authorized. Output a threat model with assumptions, evidence gaps, recommended controls, and required human approvals.
```

Expected output: a scoped artifact with evidence mapping, assumptions, threats, control recommendations, residual risk, limitations, confidence, stop conditions, and independent-review requirements.

For Devin Local or Devin CLI:

1. Start from `windsurf/cybersecurity/` or a selected area directory.
2. Use the committed `.devin/config.json` for project permissions.
3. Keep the session in `/plan` mode for read-only planning when using the CLI for assessment or review.
4. Use `devin skills list` or `devin skills show <name>` only to inspect available Skills; do not authenticate MCP or start integrations from this package.

Example CLI prompt after `cd windsurf/cybersecurity/exposure-vulnerability-hardening`:

```text
devin -- "Use AGENTS.md and the exposure-lifecycle-triage Skill to review these supplied vulnerability findings. Treat all data as static evidence. Do not run scanners, execute shell commands, connect MCP, or change files unless I explicitly approve a static documentation edit."
```

Human approval is required before writes, shell use, MCP, connector setup, live target access, incident action, offensive testing, recovery action, publication, or any final risk/closure decision.

## Working directory and discovery

Cascade:

- `AGENTS.md` files are automatically discovered in the workspace and scoped by file location.
- `.windsurf/skills/<skill-name>/SKILL.md` is a workspace Skill path. Open the area directory as the workspace when you want that area's Skills to be available.
- `.devin/rules/*.md` is the preferred current Cascade rules path; `.windsurf/rules/*.md` is a supported fallback. This package uses `AGENTS.md` instead of separate rule copies to avoid duplicate instruction channels.
- `.windsurfrules` is a legacy single-file rule path and is intentionally omitted.
- `.windsurf/hooks.json` would be the workspace hook file, but this package intentionally ships no hooks.

Devin Local/CLI:

- `.devin/config.json` is discovered by walking from the current directory and is a committed project config.
- Nested `.devin` configs can take precedence over ancestor configs. Launch inside `windsurf/cybersecurity/` or a child area when using this department.
- Project config supports `permissions`, `mcpServers`, `read_config_from`, and hooks. This package leaves `mcpServers` empty and denies MCP tool use.
- `read_config_from.windsurf` is enabled so Devin can import supported Windsurf rules/Skills; Cursor and Claude imports are disabled to avoid cross-platform leakage.
- `AGENTS.md` is loaded as project rule context.

Files that are not auto-discovered by this package: platform README text, `NATIVE_SOURCES.md`, external evidence, uncommitted local overrides, global user rules, cloud Devin setup, connector credentials, and any MCP server not explicitly configured by a human outside this baseline.

## Area map

- `windsurf/cybersecurity/governance-risk-compliance-assurance/` - governance, cyber risk, compliance mapping, policy, assurance, exceptions, and risk-decision support.
- `windsurf/cybersecurity/security-architecture-engineering/` - security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `windsurf/cybersecurity/application-product-devsecops-security/` - product security, application security, secure SDLC, threat modeling, CI/CD, supply chain, PSIRT, and release assurance.
- `windsurf/cybersecurity/exposure-vulnerability-hardening/` - exposure management, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `windsurf/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC model, telemetry, detection engineering, alert triage, threat hunting, intelligence, and coverage quality.
- `windsurf/cybersecurity/incident-response-dfir-recovery/` - incident planning, evidence governance, DFIR planning, containment options, recovery coordination, and lessons learned.
- `windsurf/cybersecurity/offensive-security-authorized-validation/` - explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and offensive safety review.
- `windsurf/cybersecurity/cyber-resilience-specialized-technologies/` - resilience, backup/recovery, OT/ICS, IoT, AI security, firmware, cryptographic agility, and critical infrastructure.

## Native components

- `windsurf/cybersecurity/.devin/config.json` - Devin Local/CLI project permissions, empty project MCP configuration, and import controls.
- `windsurf/cybersecurity/<area>/AGENTS.md` - Cascade and Devin scoped area instructions.
- `windsurf/cybersecurity/<area>/.windsurf/skills/<skill-name>/SKILL.md` - Cascade workspace Skills and Devin-importable Windsurf Skills.

No repository custom-agent files, live workflows, hook files, MCP servers, connectors, or cloud-agent schedules are shipped.

## How to use the department

1. Select the owning area from the area map.
2. Open that area as the Cascade workspace or launch Devin from `windsurf/cybersecurity/` or the selected area.
3. Provide the authorized scope, explicit exclusions, accountable owner, requester, intended audience, evidence inventory, assumptions, constraints, reviewer, approver role, and decision needed.
4. Invoke the most relevant Skill by natural language or `@skill-name` when Cascade supports manual Skill mentions.
5. Review the output for evidence quality, limitations, confidence, required human decisions, and independent review.
6. Stop if the request needs live testing, sensitive data, unapproved tools, production action, offensive authorization, incident command, recovery execution, external publication, or self-review.

## Permissions and safety

The Devin project config allows read/search/glob operations, asks before writes, denies shell execution, denies fetch, denies MCP tools, and denies writes to `.env` patterns or paths outside the selected tree. Cascade permissions and workspace trust remain controlled by the user's product settings and organization policy; this repository does not override those controls.

Network access, MCP, connectors, cloud accounts, SIEM/EDR/XDR/SOAR systems, scanners, ticketing systems, identity providers, remote Git actions, app deploys, shell hooks, and hosted tools are absent or denied by default. Any later integration must be approved by a human owner and configured outside this reusable baseline with secrets stored only in user/local secret mechanisms.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, architecture, build systems, technology stack, deployment model, cloud providers, CI/CD structure, telemetry locations, asset inventories, threat-model scope, project policies, evidence locations, approved test scope, approved targets, and area-specific working directories per project.

### User/organization-dependent configuration

Supply or approve account access, subscriptions, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, authorized offensive-testing scope, data-retention requirements, and legal/privacy constraints. Do not commit real secrets or confidential organization values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, no unauthorized active testing, safe default permissions, stop conditions, and human-approval gates intact. These properties define the safety and governance model.

## Validation

Static validation covers JSON syntax, Markdown and Skill frontmatter, required area paths, native path inventory, README/source consistency, duplicate/orphan checks, and absence of committed credentials or active integrations. Repository validation does not execute Cascade, launch Devin sessions, run hooks, authenticate, connect MCP, call models, scan targets, run incident actions, or test production systems.

## Troubleshooting

- If Cascade ignores an area Skill, open the area directory itself as the workspace and confirm the Skill lives at `.windsurf/skills/<skill-name>/SKILL.md`.
- If Devin does not load the permissions, launch from `windsurf/cybersecurity/` or a child directory so `.devin/config.json` is in the discovery path.
- If Devin imports unexpected tool configuration, inspect `read_config_from` and user/global config. This baseline disables Cursor and Claude imports and leaves project MCP empty.
- If writes are requested, verify they are static documentation changes inside the authorized area and approve them explicitly.
- If hooks appear in the product UI, they came from user, workspace, system, or enterprise configuration outside this package; this repository ships no `.windsurf/hooks.json`.
- If MCP tools appear, they came from user/global/project configuration outside this baseline or an organization policy; do not use them without explicit approval.

## Removal or uninstall

For Cascade, remove the selected area from the workspace or delete the imported `.windsurf/skills/` and `AGENTS.md` files from the project copy. For Devin Local/CLI, delete `windsurf/cybersecurity/.devin/config.json` from the project copy or remove the entire `windsurf/cybersecurity/` package. In the CLI, use `devin skills paths` and `devin rules paths` to confirm no copied project or global artifacts remain. Do not delete user-global Devin, Windsurf, MCP, or organization settings unless the responsible human owner explicitly approves that separate cleanup.

## Limitations

This package is static instruction and Skill content. It is not a scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, managed service, legal opinion, compliance certification, or production-control system. Cascade, Devin Local, Skills, hooks, permissions, and import behavior can change by release, plan, account, and administrator policy.

## Security notice

Explicit authorization and human control are mandatory for offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence. Do not use this package to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
