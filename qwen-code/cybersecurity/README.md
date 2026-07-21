# Cybersecurity Department for qwen-code

This Cybersecurity department is a professional, adaptable baseline for qwen-code covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience.

Its purpose is to help humans produce evidence-based cybersecurity work products while preserving clear professional ownership, least privilege, independent review, and human authority for consequential decisions.

Possible uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

The department contains eight Cybersecurity areas under `qwen-code/cybersecurity/<area>/`. Each area is scoped to a distinct professional ownership boundary and is intended for static analysis, planning, review, documentation, and assurance using supplied evidence.

It does not authorize live scanning, exploitation, containment, recovery execution, production changes, publication, external integrations, legal determinations, risk acceptance, or closure decisions. Human owners remain accountable for authorization, approvals, exceptions, risk acceptance, incident declaration or closure, offensive testing authorization, and production action.

## Possible uses

- Risk and compliance assessment using supplied policies, control evidence, and framework mappings.
- Security architecture and engineering review for proposed designs and reference patterns.
- Threat modeling, secure SDLC review, release-readiness support, and supply-chain evidence review.
- Vulnerability prioritization, remediation planning, and hardening governance from provided findings.
- Detection engineering, telemetry coverage review, SOC triage methods, and threat-hunt planning.
- Incident-response readiness, DFIR planning, evidence governance, recovery planning, and lessons learned.
- Authorized offensive assessment planning, rules of engagement review, validation planning, and retest assurance.
- Resilience exercises, ransomware recovery planning, specialized technology review, and independent assurance.

## Platform compatibility

Product surface: Qwen Code CLI project context, `QWEN.md`, `AGENTS.md`, project settings in `.qwen/settings.json`, custom subagents in `.qwen/agents/*.md`, Agent Skills in `.qwen/skills/<name>/SKILL.md`, and custom slash-command prompts in `.qwen/commands/*.md`.

Validated documentation date: 2026-07-21. Qwen Code must be a recent CLI release that supports custom subagents, Agent Skills, project settings, approval modes, and hooks configuration. Provider account, model access, workspace policy, IDE integration, and SDK/headless availability are user- or organization-dependent. This package documents static, repository-local components only.

## Prerequisites

Qwen Code installed, launched from an intended area directory, and the workspace trusted according to Qwen Code folder-trust behavior. Provider credentials and account setup must be configured outside this repository only by a human.

Do not place credentials, tokens, keys, private endpoints, personal data, confidential customer data, or live system access material in this package. Connectors, MCP servers, cloud accounts, scanners, SIEM/EDR/XDR/SOAR tools, ticketing systems, identity providers, and hosted tools are disabled or absent unless a retained native file explicitly documents a human-approved external configuration.

## Installation or import

Open Qwen Code from the selected area directory so the nearest `QWEN.md`, `AGENTS.md`, `.qwen/settings.json`, `.qwen/agents/`, `.qwen/skills/`, and `.qwen/commands/` are the active project-local package:

```bash
cd qwen-code/cybersecurity/governance-risk-compliance-assurance
qwen
```

Use one area per session unless the human explicitly asks for a cross-area handoff. Keep approval conservative; this package sets custom cybersecurity agents to `approvalMode: plan` and read-only native tools.

Use project-local or repository-local setup only. Do not install tools globally from this package, and do not authenticate services merely to import the instructions.

## Working directory and discovery

Qwen Code discovers project settings from `.qwen/settings.json`, project context from `QWEN.md`, repository agent instructions from `AGENTS.md`, custom subagents from `.qwen/agents/*.md`, Skills from `.qwen/skills/<skill-name>/SKILL.md`, and custom commands from `.qwen/commands/*.md` relative to the active project/workspace.

Launch from `qwen-code/cybersecurity/<area>/` for area isolation. The area-level `.qwen/settings.json`, agents, Skills, and commands are not a single repository-wide installation; they are intended to be loaded from the selected area. Qwen Code settings precedence follows the documented order of defaults, system, user, project, environment, and command-line flags. User-level settings, command-line flags, or a more permissive parent session can override or weaken project defaults, so confirm `/status` and approval mode before relying on them.

## Area map

- `qwen-code/cybersecurity/governance-risk-compliance-assurance/` - Governance, Risk, Compliance, and Assurance: governance, cyber risk, compliance mapping, policies, assurance, exceptions, and risk-decision support.
- `qwen-code/cybersecurity/security-architecture-engineering/` - Security Architecture and Engineering: security architecture, engineering patterns, identity, network, cloud, data, platform, and control design review.
- `qwen-code/cybersecurity/application-product-devsecops-security/` - Application, Product, and DevSecOps Security: product security, secure SDLC, threat modeling, code/design review, CI/CD, supply chain, PSIRT, and release assurance.
- `qwen-code/cybersecurity/exposure-vulnerability-hardening/` - Exposure, Vulnerability, and Hardening: asset exposure, vulnerability triage, prioritization, hardening, remediation governance, and validation evidence.
- `qwen-code/cybersecurity/defensive-security-operations-detection-intelligence/` - Defensive Security Operations, Detection, and Intelligence: SOC operating model, telemetry, detection engineering, alert triage, hunting, intelligence, and coverage quality.
- `qwen-code/cybersecurity/incident-response-dfir-recovery/` - Incident Response, DFIR, and Recovery: incident planning, evidence governance, DFIR analysis planning, containment planning, recovery coordination, and lessons learned.
- `qwen-code/cybersecurity/offensive-security-authorized-validation/` - Offensive Security and Authorized Validation: explicitly authorized assessment planning, rules of engagement, emulation governance, retest planning, and safety review.
- `qwen-code/cybersecurity/cyber-resilience-specialized-technologies/` - Cyber Resilience and Specialized Technologies: resilience, ransomware recovery planning, specialized technology review, cryptography, critical infrastructure, OT/IoT/cloud edge, and transition assurance.

## Native components

- `QWEN.md` and `AGENTS.md` where present: area coordinator and repository-agent instructions.
- `.qwen/settings.json`: conservative project settings, disabled hooks, MCP exclusion, telemetry/logging restrictions, folder trust, and default approval behavior.
- `.qwen/agents/*.md`: Qwen custom subagents with native frontmatter fields `name`, `description`, `model`, `approvalMode`, `tools`, and `disallowedTools`.
- `.qwen/skills/<name>/SKILL.md`: Agent Skills with `name`, `description`, and procedural instructions.
- `.qwen/commands/*.md`: user-invoked slash-command prompt files that delegate to the retained Skills and agents.

Unsupported native mechanisms are omitted rather than simulated. The package does not include fake MCP servers, live hooks that execute security actions, hosted scanner integrations, cloud deployment automation, or credentials.

## How to use the department

Select the area that owns the requested work, open that area in Qwen Code, and provide authorized scope, exclusions, accountable owner, requester, intended audience, decision needed, evidence inventory, assumptions, constraints, reviewer, and approver role.

Examples:

```text
/governance-policy-frameworks
Scope: repository policy files under docs/security/.
Evidence: supplied control matrix and policy excerpts.
Output: control-gap assessment with evidence states and human approval points.
```

```text
Use the threat-modeling Skill for this API design. Approved scope is the attached design note only. Do not scan, call services, or edit code. Expected output is a threat model with assumptions, mitigations, validation criteria, and independent-review triggers.
```

```text
Invoke independent-offensive-safety-reviewer for the attached rules of engagement. Confirm whether authorization, target scope, stop conditions, evidence handling, and retest boundaries are sufficient. Do not run tools beyond read/search/list operations.
```

Expected outputs are scoped artifacts with evidence tables, assumptions, findings or recommendations separated by evidence state, limitations, confidence, residual risk, required human decisions, and completion criteria. High-impact outputs must be routed to an independent reviewer that did not create the work. Components stop when authorization is missing, sensitive data is unredacted, scope is unclear, a live action is requested, evidence is insufficient for a conclusion, or self-review would occur.

## Permissions and safety

Default behavior is read-only and static. Custom agents use `approvalMode: plan`, native read/search/list tools `read_file`, `grep_search`, `glob`, and `list_directory`, and deny write, edit, notebook edit, shell, and web-fetch tools. Area settings keep Qwen Code in default ask-before-changing behavior, disable hooks, exclude MCP, disable interactive shell/computer-use settings, and deny common secret paths.

Repository writes, where Qwen Code technically allows them outside a custom plan-mode agent, must stay inside the selected `qwen-code/cybersecurity/<area>/` directory and require an explicit user task to update static artifacts. Shell, network, installation, deployment, scanning, exploitation, recovery execution, remote Git operations, MCP connections, hosted tools, and external connectors are prohibited by default.

AI components cannot self-approve, accept enterprise risk, authorize offensive testing, approve production changes, close incidents, certify compliance, make legal determinations, or conceal residual risk. Human review is mandatory for approvals, exceptions, risk acceptance, release or closure decisions, incident command, offensive authorization, external reporting, and production actions.

## Configuration and customization

Project-dependent configuration: repository paths, source directories, application architecture, technology stack, deployment model, CI/CD layout, telemetry locations, threat-model scope, asset lists, approved targets, area-specific working directories, and repository-specific policies must be supplied per project and should not be hard-coded globally.

User/organization-dependent configuration: account or subscription, provider credentials, user identity, organization policies, regulatory frameworks, risk appetite, asset criticality, SLAs, escalation contacts, approval authorities, permitted tools, permitted integrations, MCP endpoints, cloud/SIEM/EDR/XDR/SOAR/ticketing systems, incident contacts, offensive-testing authorization, retention rules, and legal/privacy constraints must be supplied or approved by the user or organization. Do not commit real secrets or confidential organization values.

Fixed baseline configuration: area ownership boundaries, independent review, no self-approval, no automatic risk acceptance, evidence requirements, disabled hooks, absent MCP/connectors, read-only custom-agent tools, prohibited unauthorized actions, stop conditions, and human-approval gates normally remain unchanged because they define the reusable safety model.

Organizations may add static policies, frameworks, asset context, service-level targets, approved tool names, sector requirements, and evidence templates in the relevant area after human review. Keep values organization-neutral in shared packages, redact sensitive information, and document any integration without enabling it by default.

## Validation

Static validation can check file syntax, native paths, frontmatter, JSON/TOML/YAML parsing, prompt references, Skill structure, duplicate or obsolete files, empty artifacts, broken links, and absence of secrets or active integrations. Live system behavior, connector access, model behavior, scanner operation, incident action, recovery, and production integration require a separate authorized environment and were not exercised by this repository package.

## Troubleshooting

- If instructions are ignored, confirm the platform was opened from the documented working directory or the files were manually imported into the correct Project, Skill, agent, or rule location.
- If an agent or Skill is unavailable, verify the feature is enabled and that `.qwen/agents/<name>.md` or `.qwen/skills/<name>/SKILL.md` exists under the launched area.
- If a slash command is unavailable, confirm `.qwen/commands/<command>.md` is under the launched area and restart or refresh the Qwen Code session if required by the CLI.
- If permissions appear broader than intended, inspect `/status`, approval mode, user settings, command-line flags, and project `.qwen/settings.json` before use; deny shell, network, MCP, connector, deployment, scanner, and remote Git access.
- If paths fail to resolve, use paths relative to the selected area package unless the platform documentation states otherwise.
- If a platform preview feature changes, re-check official documentation and update `qwen-code/cybersecurity/NATIVE_SOURCES.md` before relying on it.

## Removal or uninstall

Stop the Qwen Code session, remove any manually copied area files from the consuming project, or delete the selected `qwen-code/cybersecurity/<area>/` directory from a repository that no longer needs it. To remove one native component, delete that area's `.qwen/agents/<name>.md`, `.qwen/skills/<name>/`, or `.qwen/commands/<name>.md` file and restart or refresh Qwen Code. Do not delete organizational evidence, user settings, provider credentials, or platform-global settings unless a human owner explicitly authorizes that cleanup.

## Limitations

This package is a static professional baseline. It is not a managed security service, scanner, SIEM, SOAR, EDR/XDR integration, penetration-testing tool, incident-response platform, legal opinion, compliance certification, or production-control system. Platform support and schema details can change, especially for preview agent, Skill, hook, and permission features.

## Security notice

Offensive testing, incident actions, production changes, external integrations, live scans, exploitation, deployment, recovery, publication, and use of sensitive evidence require explicit authorization, validated scope, and human control. Do not use these components to bypass approval, access secrets, contact external systems, or claim live execution without evidence.
