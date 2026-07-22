# Web Development — Windsurf / Devin Desktop

## Department overview

This is a professional Web Development department for Devin Desktop / Cascade-compatible Windsurf workspaces. It is already specialized for Web Development and is not a generic AI template awaiting manual specialization. It is stack-aware rather than tied to one framework and covers frontend, backend/API, architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

The lead selects applicable specialists and workflows according to project evidence. The package is intended to work immediately after installation; customization supplies local constraints, not the core specialization.

## Possible uses

- Discover an existing web stack and conventions.
- Understand unfamiliar frontend, backend, or full-stack code.
- Plan or review a new web feature.
- Review REST, GraphQL, WebSocket, or webhook APIs when applicable.
- Review authentication, authorization, sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions.
- Audit responsive behavior, accessibility, performance, Core Web Vitals, SEO, metadata, structured data, crawlability, and rendering strategy.
- Review dependency and supply-chain risks.
- Prepare testing, observability, rollback, browser compatibility, and release-readiness evidence.

## Supported product surface

This package targets current Cascade workspace configuration for Windsurf-compatible repositories. It uses root `AGENTS.md`, workspace Rules in `.windsurf/rules/*.md`, Cascade workspace Skills in `.windsurf/skills/<skill>/SKILL.md`, and Cascade workflows in `.windsurf/workflows/*.md`. It is static configuration, not an SDK, hook package, MCP server, App Deploy setup, browser automation package, or external integration.

Current official Windsurf plugin documentation discovers Cascade workspace Rules from `.windsurf/rules/` directories in the workspace, subdirectories, and parent directories up to the Git root. Current Devin Desktop documentation also describes `.devin/rules/` as its preferred branded rule directory and `.windsurf/rules/` as a compatibility fallback. This package keeps one authoritative Cascade workspace Rules copy under `.windsurf/rules/` to avoid duplicate always-on rules. Current official documentation still uses `.windsurf/skills/` and `.windsurf/workflows/` for Cascade workspace Skills and Workflows.

## Included native components

- `AGENTS.md`: repository-root instruction surface for Devin-compatible agents; defines Web Development scope, evidence, review model, and stop conditions.
- `.windsurf/rules/web-development.md`: workspace Rule loaded by Cascade for always-on Web Development behavior.
- `.windsurf/rules/quality-gates.md`: workspace Rule for readiness, security, privacy, accessibility, performance, SEO, testing, and human-review gates.
- `.windsurf/skills/<skill>/SKILL.md`: Cascade workspace Skills for stack discovery, architecture decisions, frontend delivery, backend/API/auth, security/privacy, accessibility/performance/SEO, testing/browser compatibility, dependency review, and release readiness.
- `.windsurf/workflows/*.md`: manual Cascade workflow slash commands for planning, implementation support, debugging, audits, dependency review, API/auth review, and release readiness.

Rules are automatic according to their triggers. Skills may be selected by the model or invoked by the user where the product exposes Skills. Workflows are manual slash-command runbooks.

## Installation and integration

1. Install/open Devin Desktop or Cascade-compatible Windsurf.
2. Open the actual target Git repository.
3. Copy `windsurf/web-development/AGENTS.md` to the target repository root.
4. Copy `windsurf/web-development/.windsurf/rules/` to the target repository root as `.windsurf/rules/`.
5. Copy `windsurf/web-development/.windsurf/skills/` and `.windsurf/workflows/` to the target repository root.
6. Keep `.windsurf/` as a hidden project directory.
7. Reopen, reload, or refresh the workspace if discovery has already occurred.
8. Verify the Web Development Rules, Skills, and Workflows are visible or active in the product.
9. Keep hooks, MCP, App Deploy, browser automation, remote connectors, and external integrations disabled unless the user explicitly configures them.

## How to use

Use the lead behavior through normal Cascade/Devin chat:

```text
Plan a checkout address form and session API review. Use applicable Web Development specialists. Do not deploy, install packages, publish, or mutate Git.
```

Use a manual workflow slash command when available:

```text
/plan-web-change Add passwordless login to the existing web app with security and rollback review.
```

```text
/review-security-and-privacy Review authz, cookies, CSP, CORS, CSRF, logging, and sensitive data handling.
```

`PASS` requires evidence. `FAIL` means defects remain. `BLOCKED` means required scope, evidence, permission, approval, credential, or product decision is missing. `NOT_APPLICABLE` must include a reason. `NOT_EXECUTED` is not a pass.

## Operating model

1. Task and scope intake.
2. Existing-project stack discovery.
3. Acceptance criteria confirmation.
4. Applicable specialist/Skill/workflow selection.
5. Proposal or implementation support.
6. Security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final review.
9. Evidence reconciliation.
10. Human approval where required.
11. Final result.

Framework-specific behavior is adapted from detected project evidence. Devin Local and Cascade compatibility can differ by product rollout; install only the surfaces supported in the active product.

## Examples

- Feature development: `/implement-web-change Add a React form with server validation, no dependency changes without approval.`
- Review/audit: `/audit-accessibility-performance-seo Audit keyboard flow, focus, responsive layout, LCP, CLS, metadata, canonical tags, and crawlability.`
- Stack selection: if the repository shows Phoenix LiveView, Skills adapt review guidance to LiveView rather than assuming SPA behavior.
- Project customization: add "Elixir 1.17, Phoenix 1.8, WCAG 2.2 AA, p95 LCP 2.5s, no new dependencies" in project criteria without editing Skills or Rules.
- Sensitive action: "Prepare deployment readiness and rollback notes; do not deploy" is review-only. Actual deployment, publication, Git push, package installation, authentication, or secret access remains human-controlled.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents/specialist responsibilities, Skills, workflows, Rules, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO rules, API conventions, auth provider, database/storage, approved dependencies, dependency policies, deployment provider, CI/CD commands, environments, feature flags, observability, logging, organization security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, MCP servers/connectors, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

The product and user permissions determine whether file edits or command execution can occur. This package does not configure hooks, MCP, App Deploy, browser automation, deployment, publication, package installation, Git mutation, authentication, secret access, spending, signing, submission, destructive operations, or external integrations. Require explicit human approval for production, external systems, auth/authz, cryptography, secrets, sensitive data, database migrations, dependencies, tracking, payments, DNS, certificates, signing, publishing, deployment, release, merge, and destructive operations.

## Limitations

Static validation cannot prove live product discovery, model behavior, browser behavior, runtime tests, deployment, publication, or external integration behavior. Devin Desktop, Cascade, and Devin Local compatibility may vary by product version and rollout. Checks not executed must remain `NOT_EXECUTED`.

## Validation

Validated July 22, 2026: root `AGENTS.md` exists, `.windsurf/rules/` contains Cascade workspace Rules with valid frontmatter, `.devin/rules/` duplicate copies are removed, `.windsurf/skills/` and `.windsurf/workflows/` remain current native surfaces, Markdown references resolve, no secrets are included, and no hooks/MCP/App Deploy/browser automation/external integrations are configured. Live Devin Desktop/Cascade loading and live model runs were not executed.

## Official documentation

Verified July 22, 2026:

- Devin Desktop Cascade Rules: https://docs.devin.ai/desktop/cascade/memories
- Devin Desktop AGENTS.md: https://docs.devin.ai/desktop/cascade/agents-md
- Windsurf plugin Cascade Rules: https://docs.devin.ai/windsurf/plugins/cascade/memories
- Cascade Skills: https://docs.devin.ai/desktop/cascade/skills
- Cascade Workflows: https://docs.devin.ai/desktop/cascade/workflows
