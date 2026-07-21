# Cybersecurity Department for Kilo Code

This Cybersecurity department is a reusable Kilo Code baseline for governance, risk, compliance, and assurance; security architecture and engineering; application, product, and DevSecOps security; exposure, vulnerability, and hardening management; defensive operations, detection, and threat intelligence; incident response, DFIR, and recovery; authorized offensive validation; and resilience and specialized technologies.

It solves the professional problem of producing scoped, evidence-based cybersecurity work products while keeping authorization, approvals, risk acceptance, incident command, offensive testing authorization, and production decisions under human control.

Possible uses include risk and compliance assessment, architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering review, incident-response planning, authorized validation planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight isolated Kilo Code project packages under `kilo-code/cybersecurity/<area>/`. Each area uses current Kilo Code surfaces: `AGENTS.md`, `kilo.jsonc`, `.kilo/agents/*.md`, `.kilo/commands/*.md`, `.kilo/skills/<skill>/SKILL.md`, `.kilo/rules/*.md` where unique rule files are needed, and `.kilocodeignore`.

The AI is not authorized to accept enterprise risk, approve its own work, authorize offensive testing, approve production changes, make legal determinations, approve incident closure or recovery completion, hide residual risk, or claim execution without evidence.

## Possible uses

- Draft governance, risk, policy, control, exception, assurance, third-party, and reporting artifacts from supplied evidence.
- Review enterprise, solution, identity, cloud, network, data, container, automation, and control architecture.
- Support secure SDLC, threat modeling, secure design/code review, CI/CD, supply-chain, PSIRT, and release-readiness evidence review.
- Triage supplied vulnerabilities and exposures, plan remediation and hardening, and review validation evidence.
- Review telemetry requirements, detection logic, SOC triage, hunting, intelligence, malware-analysis planning, automation, and coverage quality.
- Prepare incident readiness, evidence handling, DFIR planning, containment planning, recovery coordination, tabletop, and corrective-action artifacts.
- Plan explicitly authorized offensive validation, scope, rules of engagement, deconfliction, emulation, Purple Team validation, retest, and cleanup assurance.
- Review resilience, ransomware recovery, specialized technology, OT/ICS, IoT, embedded, AI security, hardware, firmware, cryptography, and critical infrastructure.

## Platform compatibility

Validated against current Kilo Code documentation checked on 2026-07-21. The relevant surface is Kilo Code 1.0 or later in the current VS Code extension and CLI, which are built on the Kilo CLI.

Current native mechanisms used here:

- Project configuration in `kilo.jsonc`.
- Project instructions through root `AGENTS.md`.
- Additional project rules through `instructions` entries in `kilo.jsonc`.
- Custom subagents in `.kilo/agents/*.md`.
- Agent Skills in `.kilo/skills/<skill>/SKILL.md`.
- Slash-command workflows in `.kilo/commands/*.md`.
- File access exclusions in `.kilocodeignore`.

Legacy `.kilocodemodes`, `.kilocode/rules`, and `.kilo/workflows` layouts are not used.

## Prerequisites

- Kilo Code VS Code extension or Kilo CLI version 1.0 or later.
- User-managed Kilo provider authentication outside this repository if the user later runs Kilo.
- A trusted workspace opened at the selected area root.
- Explicit authorized scope, exclusions, human owner, reviewer, approver role, and redacted evidence.
- No committed credentials, API keys, provider configs, private endpoints, scanner credentials, SIEM/EDR/XDR/SOAR credentials, cloud credentials, incident contacts, or customer secrets.

## Installation or import

For CLI use from the repository root, start Kilo with the selected area as the project:

```bash
kilo kilo-code/cybersecurity/governance-risk-compliance-assurance
```

For one-shot CLI use after the user has configured Kilo outside this repository, change into the area first:

```bash
cd kilo-code/cybersecurity/application-product-devsecops-security
kilo run "Use /threat-modeling for a static review of the supplied payment-service design evidence. Do not scan, exploit, deploy, connect MCP, or modify production."
```

For the VS Code extension, open the selected `kilo-code/cybersecurity/<area>/` folder as the workspace root, then use Kilo's agent picker, `/agents`, `/reload`, and slash command picker from that workspace.

This package does not run Kilo, authenticate providers, install global tools, connect MCP, or call a model during repository validation.

## Working directory and discovery

Use one area directory as the Kilo project root, for example `kilo-code/cybersecurity/incident-response-dfir-recovery/`.

Kilo discovers:

- `kilo.jsonc` from the project root.
- `AGENTS.md` from the project root, plus per-directory `AGENTS.md` files when files in those directories are read.
- `.kilo/agents/*.md` as project custom agents/subagents.
- `.kilo/commands/*.md` as slash-command workflows invoked as `/<filename>`.
- `.kilo/skills/<skill>/SKILL.md` as project Skills.
- `.kilocodeignore` as a supported access-control compatibility file that is migrated into read/edit deny behavior.

Configuration precedence is layered: built-in defaults, global config, project `kilo.jsonc`, `.kilo` agent files, and environment overrides. Project instructions take precedence over global instructions for conflicts, but user/global settings can still broaden behavior if the user configured them.

Do not open `kilo-code/cybersecurity/` as one combined project and expect all eight nested area packages to merge correctly. Choose one area root per task.

## Area map

- `kilo-code/cybersecurity/governance-risk-compliance-assurance/` - governance, policy, risk, compliance mapping, exceptions, assurance, third-party review, and reporting.
- `kilo-code/cybersecurity/security-architecture-engineering/` - enterprise, solution, identity, cloud, network, data, platform, container, automation, and control architecture.
- `kilo-code/cybersecurity/application-product-devsecops-security/` - product security, secure SDLC, threat modeling, secure design/code review, CI/CD, supply chain, PSIRT, and release assurance.
- `kilo-code/cybersecurity/exposure-vulnerability-hardening/` - exposure management, vulnerability triage, finding prioritization, remediation, hardening, and validation reporting.
- `kilo-code/cybersecurity/defensive-security-operations-detection-intelligence/` - SOC governance, telemetry, detection, triage, hunting, intelligence, malware-analysis planning, automation review, and coverage quality.
- `kilo-code/cybersecurity/incident-response-dfir-recovery/` - incident command support, evidence governance, DFIR planning, containment planning, recovery coordination, scenarios, and post-incident action.
- `kilo-code/cybersecurity/offensive-security-authorized-validation/` - authorization, scope, rules of engagement, assessment planning, emulation, deconfliction, retest, cleanup, and safety review.
- `kilo-code/cybersecurity/cyber-resilience-specialized-technologies/` - resilience, backup/recovery, ransomware recovery, specialized technology, OT/ICS, IoT, AI security, hardware, firmware, cryptography, and critical infrastructure.

## Native components

Each area retains:

- `AGENTS.md` for project-level and per-directory instruction discovery.
- `kilo.jsonc` for instructions, permissions, and empty MCP configuration.
- `.kilo/agents/*.md` custom subagents with `mode: subagent`.
- `.kilo/commands/*.md` slash-command workflow prompts.
- `.kilo/skills/<skill>/SKILL.md` Agent Skills.
- `.kilo/rules/*.md` only where the rule file contains unique content referenced by `kilo.jsonc`.
- `.kilocodeignore` for sensitive-file and bulky-output access exclusions.

## How to use the department

Select the area that owns the work, open that area as the Kilo project, and provide a scoped request such as:

```text
Use /authorization-scope-roe for the authorized API validation plan. Scope: staging API endpoints listed in evidence/scope.md. Exclusions: production, exploitation, credential use, DoS, persistence, and social engineering. Output: ROE review, missing approvals, safe test boundaries, evidence table, and independent safety review checklist.
```

Use slash commands by typing the filename with a leading slash, such as `/governance-policy-frameworks`, `/security-architecture-review`, `/threat-modeling`, `/incident-readiness-triage`, or `/independent-offensive-safety-review`.

Custom subagents can be invoked by primary agents or manually with `@agent-name`, for example:

```text
@independent-assurance-reviewer review this draft exception package for unsupported conclusions and missing evidence.
```

Expected output is a static artifact with scope, assumptions, evidence table, findings separated by evidence state, limitations, confidence, residual risk, human decisions, handoffs, stop conditions, and completion criteria. Stop when authorization is missing, evidence is insufficient, sensitive data is unredacted, a live action is requested, self-review would occur, or a human-only decision is requested.

## Permissions and safety

Area `kilo.jsonc` files allow repository read/search behavior, route subagent delegation through `permission.task`, ask before project writes, deny external-path writes, deny destructive Git and remove operations, and define an empty `mcp` object. Subagent files are stricter: they allow read/search and deny edit, write, bash, and task delegation.

Kilo permission rules resolve to `allow`, `ask`, or `deny`; pattern rules are evaluated with the last matching rule winning. Review user/global Kilo settings before use because global configuration, organization-managed agents, or environment overrides can alter behavior.

MCP is absent in this package. Do not add MCP servers, provider API keys, proxy configs, hosted tools, scanner connectors, cloud accounts, terminal auto-approval, or broad Action Allowlist entries unless a separate authorized environment and human approval explicitly require them.

## Configuration and customization

### Project-dependent configuration

Adapt repository paths, source directories, application architecture, build systems, technology stack, deployment model, cloud provider, CI/CD structure, telemetry locations, product requirements, threat-model scope, project assets, approved targets, area working directory, and repository-specific policies per project.

### User/organization-dependent configuration

Supply or approve Kilo account/subscription, provider credentials, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, API credentials, MCP endpoints, cloud accounts, SIEM/EDR/XDR/SOAR systems, ticketing systems, incident contacts, offensive-testing scope, data retention, legal constraints, and privacy constraints outside this repository. Never commit real secrets or confidential organization values.

### Fixed baseline configuration

Keep area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, conservative permissions, prohibited unauthorized actions, stop conditions, and human approval gates unless a formal governance decision changes the baseline.

## Validation

Repository validation covers JSONC parsing, Markdown/YAML frontmatter parsing, agent names and modes, permission fields, command location, Skill structure, rule references, duplicate/orphan review, `.kilocodeignore`, empty files, broken references, secrets, and temporary residue.

Runtime validation of actual Kilo model behavior, provider authentication, MCP connections, agent execution, live scans, incident actions, and production changes requires a separate authorized environment and was not performed by this repository remediation.

## Troubleshooting

- If commands are missing, confirm they are in `.kilo/commands/`, not `.kilo/workflows/`, and run `/reload`.
- If an agent is not available, confirm the file is in `.kilo/agents/`, has valid YAML frontmatter, and uses `mode: subagent`, `primary`, or `all`.
- If a Skill is not used, check `.kilo/skills/<name>/SKILL.md` and make the `description` specific enough for Kilo to select it.
- If rules appear duplicated, rely on `AGENTS.md` for the area baseline and keep only unique `.kilo/rules` files referenced in `kilo.jsonc`.
- If permissions are broader than intended, inspect project `kilo.jsonc`, global `~/.config/kilo/kilo.jsonc`, organization-managed agents, and environment overrides.
- If sensitive files are accessible, confirm `.kilocodeignore` and `permission.read`/`permission.edit` deny rules are active from the selected workspace root.

## Removal or uninstall

To remove this package from a repository, delete `kilo-code/cybersecurity/<area>/` or `kilo-code/cybersecurity/` after preserving any real project evidence stored elsewhere. To remove imported global components, delete only the user-owned copies from `~/.config/kilo/agents/`, `~/.config/kilo/commands/`, `~/.kilo/skills/`, or global `kilo.jsonc` after explicit approval.

To stop using Kilo for the area without deleting repository content, close the workspace, remove any manually imported MCP or provider settings from Kilo's UI/config, and clear broad approval rules that were added outside this package.

## Limitations

This package is a static professional baseline, not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, DFIR platform, legal opinion, compliance certification, or production-control system. Kilo feature availability and extension/CLI behavior can change.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and sensitive evidence handling require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
