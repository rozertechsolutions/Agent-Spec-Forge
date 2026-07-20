# Cybersecurity Department for ChatGPT

This Cybersecurity department is a professional, adaptable ChatGPT baseline covering governance, architecture, product security, vulnerability management, defensive operations, incident response, authorized offensive validation, and resilience. Its purpose is to help qualified humans prepare structured cybersecurity analysis, plans, reviews, evidence requests, and assurance outputs without granting the AI authority to execute security actions or accept risk. Realistic uses include risk and compliance assessment, security architecture review, threat modeling, secure SDLC review, vulnerability prioritization, detection engineering, incident-response planning, authorized penetration-test planning, resilience exercises, and independent assurance.

## Department overview

This package is a set of copy-ready ChatGPT Project, Custom GPT, Workspace Agent, knowledge, workflow, template, and Skill materials for the eight Cybersecurity areas under `chatgpt/cybersecurity/`. It covers professional advisory and drafting workflows only. It does not authorize live scanning, exploitation, containment, recovery, production change, legal decision-making, risk acceptance, connector authorization, or external communication. Accountable humans remain responsible for authorization, evidence quality, risk decisions, approvals, implementation, and final sign-off.

## Possible uses

- Assess cybersecurity governance, policy, control mapping, exceptions, and assurance evidence.
- Review security architecture, cloud, identity, network, data, container, and automation patterns.
- Support secure SDLC, threat modeling, code-review planning, supply-chain review, PSIRT, and remediation governance.
- Normalize and prioritize vulnerability, exposure, and hardening findings from authorized inputs.
- Design detection logic, triage guidance, threat-hunting plans, telemetry coverage, and SOC quality reviews.
- Prepare incident command, evidence handling, DFIR planning, containment planning, recovery planning, and lessons-learned material.
- Plan explicitly authorized offensive validation, penetration-test scope, purple-team exercises, and retest evidence.
- Run resilience exercises and specialized technology reviews for AI, OT, IoT, cryptography, privacy, and critical services.

## Platform compatibility

Validated against official OpenAI ChatGPT Help Center documentation checked on 2026-07-20 for Projects, GPTs, Skills, apps/plugins, Workspace Agents, and ChatGPT release notes. ChatGPT Projects are available to logged-in free and paid users, with file limits varying by plan. Creating or editing GPTs requires paid ChatGPT access and is limited to the web builder. Personal Skills are generally available for Business, Enterprise, Healthcare, and Edu users, with workspace permissions controlling creation, upload, sharing, publishing, and installation. Workspace Agents are documented for eligible Business and Enterprise workspaces where admins enable the feature. Apps, plugins, connectors, Work, and Slack deployment depend on plan, region, rollout, workspace settings, RBAC, and per-app permissions.

## Prerequisites

- A ChatGPT account and the plan or workspace features needed for the chosen surface: Project, Custom GPT, Skill, or Workspace Agent.
- Permission to create or edit the Project, GPT, Skill, or Workspace Agent in the relevant workspace.
- Repository trust in the local files before upload or copy-paste import.
- No credentials, secrets, private keys, tokens, personal data, production endpoints, or confidential organization values in imported files unless the organization has approved that data handling.
- Connectors, apps, custom actions, MCP apps, Slack deployment, Work, and web access disabled unless separately approved by workspace owners and the accountable security authority.

## Installation or import

Use one area at a time.

1. In ChatGPT, create a Project or Custom GPT for the selected area.
2. Copy the area `PROJECT_INSTRUCTIONS.md` into Project instructions, Custom GPT instructions, or Workspace Agent instructions.
3. Upload the area's `knowledge/`, `templates/`, and `workflows/` files as Project files, GPT knowledge, or Workspace Agent files, subject to plan limits.
4. If ChatGPT Skills are enabled, upload or recreate each `skills/<skill-name>/SKILL.md` from that area through the ChatGPT Skills page or editor.
5. Leave apps, actions, connectors, MCP apps, code execution, scheduled tasks, Slack deployment, and external write actions disabled unless a separate human-approved integration design exists.

Do not run repository commands to install this package globally. ChatGPT does not automatically load repository files from disk.

## Working directory and discovery

The documented working directory is the selected area path, for example `chatgpt/cybersecurity/governance-risk-compliance-assurance/`. ChatGPT discovers only what a user manually pastes into instructions, uploads as files, uploads as Skills, or configures in the Workspace Agent/GPT builder. There is no automatic upward or downward repository discovery for ChatGPT. Each area is an isolated import package: use only that area's instructions, files, workflows, templates, and Skills unless a human explicitly authorizes a cross-area handoff. Project instructions apply only inside the Project and override global custom instructions; GPT instructions apply inside the GPT; Workspace Agent instructions and tool settings apply to that agent.

## Area map

- `governance-risk-compliance-assurance/`: governance, risk, compliance, policy, assurance, exceptions, and risk-decision support.
- `security-architecture-engineering/`: security architecture, engineering patterns, identity, cloud, network, data, container, and automation review.
- `application-product-devsecops-security/`: product security, application security, secure SDLC, software supply chain, and DevSecOps review.
- `exposure-vulnerability-hardening/`: exposure management, vulnerability prioritization, hardening, and remediation governance.
- `defensive-security-operations-detection-intelligence/`: monitoring design, detection engineering, triage, hunting, intelligence, and SOC quality.
- `incident-response-dfir-recovery/`: declared incident planning, evidence governance, DFIR, containment planning, recovery planning, and lessons learned.
- `offensive-security-authorized-validation/`: explicitly authorized offensive assessment planning, validation, purple-team support, findings, and retest assurance.
- `cyber-resilience-specialized-technologies/`: resilience, recovery exercises, specialized technologies, and transition assurance.

## Native components

This package uses ChatGPT-native manual components: Project or GPT instructions, uploaded knowledge files, uploaded workflow and template files, ChatGPT Skills, and optional Workspace Agent builder instructions/files when the workspace supports agents. It intentionally does not include repository-loaded agents, subagents, local hooks, local MCP servers, action schemas, runnable workflows, connector definitions, or fake app integrations.

## How to use the department

Select the area that owns the request, open the matching Project, GPT, Workspace Agent, or Skill, and provide authorized scope, objective, source artifacts, constraints, evidence available, desired output type, and accountable human owner. Expect structured advisory outputs such as reviews, matrices, plans, findings, evidence requests, decision packages, test plans, or assurance notes. Human review is mandatory for high-impact outputs, risk decisions, legal interpretations, production changes, incident closure, recovery completion, external communications, and offensive testing authorization. The component must stop when authorization, scope, evidence, human owner, or confidence is insufficient, and it should hand off to another area only by naming the receiving area and the reason.

## Permissions and safety

ChatGPT Projects and GPTs have no repository-level read/write permission policy. They can use only the conversation, manually uploaded files, enabled built-in tools, and configured apps/actions. Keep app permissions at conservative settings, preferably requiring approval for reads and all changes when sensitive data is involved. Network access, web search, Work, apps, connectors, actions, MCP apps, code execution, Slack deployment, and scheduled tasks are disabled for this static package unless an authorized workspace owner enables them separately. AI output cannot self-approve, accept risk, authorize offensive testing, approve production change, close incidents, or approve recovery.

## Configuration and customization

Organizations may add approved policies, control frameworks, asset context, risk appetite statements, severity models, SLAs, tool names, responsible roles, approved integration names, sector requirements, data-handling rules, and review boards as additional uploaded knowledge or instruction text. Keep values organization-neutral in the reusable package. Use placeholders for confidential details unless the organization has approved uploading that information to ChatGPT.

## Validation

Static validation can confirm files exist, Markdown and YAML frontmatter parse, Skills have names and descriptions, all eight areas are present, references resolve locally, and no repository-native agents, hooks, MCP servers, or connector definitions are claimed. Live behavior, feature availability, uploads, app permissions, Workspace Agent settings, and Skill installation require an authorized ChatGPT workspace and were not live-tested by this repository package.

## Troubleshooting

- If instructions seem ignored, verify they were pasted into the correct Project, GPT, or Workspace Agent and that the conversation is inside that surface.
- If files are unavailable, check plan file limits, upload status, file type support, and whether the file was uploaded to the selected area surface.
- If Skills do not trigger, confirm Skills are enabled for the workspace, installed on the current surface, trusted after upload scanning, and described clearly in the request.
- If a connector appears, disable it or set app permissions to require approval unless the integration is separately authorized.
- If cross-area context leaks, create separate Projects or GPTs per area and avoid uploading multiple area packages into one surface.

## Removal or uninstall

Delete the ChatGPT Project, Custom GPT, Workspace Agent, uploaded files, and uploaded Skills created from this package. In shared workspaces, remove collaborator access first, then delete or unpublish according to workspace policy. Disconnect any separately authorized apps, actions, connectors, MCP apps, or Slack deployments through workspace settings; none are included in this repository package.

## Limitations

ChatGPT does not load this repository automatically. There is no project-local permission file, local hook runner, repository MCP configuration, or subagent manifest for ChatGPT. Feature availability changes by plan, workspace policy, rollout, and admin settings. The package provides professional analysis scaffolding, not execution authority or proof that any live system was tested.

## Security notice

Offensive testing, incident actions, production changes, external integrations, connector use, credential handling, and live-system access require explicit authorization, human control, and appropriate organizational approvals. Do not use this package to bypass security, privacy, legal, change-management, or incident-command processes.
