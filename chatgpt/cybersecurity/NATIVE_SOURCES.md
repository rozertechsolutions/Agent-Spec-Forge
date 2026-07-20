# Native Source Verification

Official sources checked on 2026-07-20:

- OpenAI Help Center, "Projects in ChatGPT", `https://help.openai.com/en/articles/10169521-projects-in-chatgpt`.
- OpenAI Help Center, "Creating and editing GPTs", `https://help.openai.com/en/articles/8554397-creating-and-editing-gpts`.
- OpenAI Help Center, "Skills in ChatGPT", `https://help.openai.com/en/articles/20001066-skills-in-chatgpt`.
- OpenAI Help Center, "Apps in ChatGPT", `https://help.openai.com/en/articles/11487775-connectors-in-chatgpt`.
- OpenAI Help Center, "ChatGPT Workspace Agents for Enterprise and Business", `https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business`.
- OpenAI Help Center, "ChatGPT release notes", `https://help.openai.com/en/articles/6825453-chatgpt-release-notes`.

## Product surface

The current ChatGPT-native surfaces relevant to this package are Projects, Custom GPTs, ChatGPT Skills, uploaded files/knowledge, apps/plugins/connectors, Workspace Agents in eligible managed workspaces, and ChatGPT Work where available. Projects support project instructions, uploaded files, project sources, project memory behavior, project sharing, and connected apps subject to workspace settings. Custom GPTs support name, description, conversation starters, instructions, knowledge files, capabilities, apps/actions, preview, save/update, and version history. Skills are reusable workflows with instructions and optional supporting files or code; workspace permissions control whether users can create, upload, share, publish, install, and use them.

## Current version or date

ChatGPT is a hosted product without a repository-pinnable version. This package records source dates instead of a binary version. Official documentation was rechecked on 2026-07-20. Relevant release notes in July 2026 include ChatGPT Work availability, desktop app Projects support, app/plugin directory changes, and increased custom-instruction limits.

## Project paths and filenames

This repository uses:

- `PROJECT_INSTRUCTIONS.md` for manual Project, GPT, or Workspace Agent instruction import.
- `knowledge/*.md` for uploaded Project/GPT/Agent knowledge files.
- `skills/<skill-name>/SKILL.md` for uploadable ChatGPT Skills.
- `templates/*.md` for uploaded output schemas.
- `workflows/*.md` for uploaded workflow guidance.
- `README.md` and `NATIVE_SOURCES.md` as repository documentation only.

ChatGPT does not automatically discover these paths from disk. Users must manually paste instructions, upload files, or upload/recreate Skills.

## Schema fields and removed fields

No repository-local ChatGPT schema is used. Skill files use the OpenAI Skills open-standard style with `name` and `description` frontmatter followed by task instructions. No repository-side fields are used for agents, subagents, hooks, MCP, connectors, apps, actions, permissions, model selection, or approval policy because ChatGPT does not load those from this directory.

## Discovery, precedence, and trust

Project instructions apply only inside the selected Project and override global custom instructions there. GPT instructions apply inside the selected GPT. Workspace Agent instructions, files, tools, apps, and safeguards are configured in the Workspace Agent builder. Uploaded Skills can be used automatically when installed and helpful, subject to workspace controls and upload trust scanning. Project/GPT/Agent files are trusted only after a human reviews and uploads them to the intended surface.

## Permissions and limitations

Apps/plugins/connectors are external integrations. They require workspace enablement, role access, app permissions, app action controls, and user connection or admin configuration where applicable. Default app permissions ask before important actions; conservative cybersecurity use should require approval before sensitive reads and all changes. Enterprise and Edu workspaces commonly keep some features off by default or controlled by RBAC. This package does not enable apps, actions, MCP apps, Slack deployment, scheduled tasks, browser automation, code execution, or live connectors.

## Omitted mechanisms and reason

Repository-loaded agents, subagents, local hooks, local MCP servers, runnable commands, and automatic workflow execution are omitted because they are not ChatGPT-native repository configuration surfaces. Fake connector definitions and dummy endpoints are omitted because they would misrepresent installation and safety behavior.

## Validation method

Validation is static: local file inventory, Markdown/frontmatter inspection, reference resolution, official-documentation comparison, and confirmation that no executable ChatGPT integration artifacts are present. No generated agent, Skill, workflow, connector, app, model call, MCP server, or live system was executed.
