# Web Development — Warp

## Department overview

This is a professional Web Development department for Warp. It is already specialized for Web Development and is not a generic AI template awaiting manual specialization. It is stack-aware rather than tied to one framework and covers frontend, backend/API, architecture, authentication and authorization, sessions and cookies, storage and integrations, responsive design, accessibility, performance and Core Web Vitals, SEO and crawlability, browser compatibility, testing, dependency and supply-chain review, security and privacy, observability, and release readiness.

The lead uses detected project evidence to decide which specialists and Skills are applicable. The department works immediately after correct installation; local configuration adds constraints rather than creating the specialization.

## Possible uses

- Discover an existing web stack from repository evidence.
- Understand unfamiliar web code and conventions.
- Plan or review frontend, backend/API, or full-stack work.
- Review REST, GraphQL, WebSocket, or webhook APIs when applicable.
- Review authentication, authorization, sessions, cookies, CSP, CORS, CSRF, validation, privacy, and secure data handling.
- Debug web regressions.
- Audit responsive behavior, accessibility, performance, Core Web Vitals, SEO, crawlability, metadata, and rendering strategy.
- Review dependency and supply-chain risks.
- Prepare testing, browser compatibility, observability, rollback, and release-readiness evidence.

## Supported product surface

This package targets Warp project Rules and project Skills. It uses root `AGENTS.md` for project rules and `.agents/skills/<skill>/SKILL.md` for project Skills. It is static configuration, not an SDK, MCP server, Oz cloud-run setup, schedule, trigger, environment, or API automation package. Warp must be installed and opened in the actual target repository.

## Included native components

- `AGENTS.md`: root Project Rules loaded by Warp in the target repository; defines Web Development scope, evidence expectations, safety boundaries, and review model.
- `.agents/skills/<skill>/SKILL.md`: native project Skills for stack discovery, architecture decisions, frontend delivery, backend/API/auth, security/privacy, accessibility/performance/SEO, testing/browser compatibility, dependency review, release readiness, and manual workflow support.
- `.agents/skills/workflow-*/SKILL.md`: manually invoked workflow Skills for planning, implementation support, debugging, audits, dependency review, and release readiness.

Skills are invoked explicitly with `/<skill-name>` where Warp exposes project Skill slash invocation, or selected by Warp when the user references the Skill. The root rules remain always-on guidance.

## Installation and integration

1. Install and open Warp.
2. Open the actual target Git repository in Warp.
3. Copy `warp/web-development/AGENTS.md` to the target repository root.
4. Copy `warp/web-development/.agents/skills/` to the target repository root as `.agents/skills/`.
5. Keep `.agents/skills/` as a hidden project directory.
6. Allow Warp to discover the Project Rules and Skills; reopen or reload the workspace if needed.
7. Verify available Skills in Warp and try a read-only command such as `/stack-discovery`.
8. Keep Oz cloud runs, schedules, triggers, environments, MCP, API/SDK automation, and cloud agent infrastructure unconfigured unless the user explicitly adds them.

## How to use

Use natural language under the project rules for broad work:

```text
Review the checkout page and API session handling. Use applicable Web Development Skills. Do not deploy, install packages, publish, or mutate Git.
```

Invoke a Skill explicitly when supported:

```text
/security-privacy-review Review CSP, CORS, cookies, CSRF, authz, logging, and sensitive data handling.
```

```text
/workflow-verify-release-readiness Prepare release-readiness evidence for the current web feature.
```

`PASS` means applicable evidence supports the result. `FAIL` means defects remain. `BLOCKED` means required evidence, permission, approval, credential, or product decision is missing. `NOT_APPLICABLE` needs a reason. `NOT_EXECUTED` is not a pass.

## Operating model

1. Task and scope intake.
2. Existing-project stack discovery.
3. Acceptance criteria confirmation.
4. Applicable specialist/Skill selection.
5. Proposal or implementation support.
6. Security/privacy review.
7. Accessibility, performance, SEO, testing, and release-readiness review.
8. Independent final review.
9. Evidence reconciliation.
10. Human approval where required.
11. Final result.

Detected framework conventions drive behavior; users do not rewrite the department for each stack.

## Examples

- Feature development: ask Warp to plan a SvelteKit profile page and API endpoint, then invoke `/frontend-delivery` and `/backend-api-auth` as applicable.
- Review/audit: run `/accessibility-performance-seo Audit responsive behavior, keyboard access, LCP, CLS, metadata, and crawlability.`
- Stack selection: if the repository contains Laravel Blade and Alpine.js, the Skills adapt review guidance to that stack.
- Project customization: add "PHP 8.3, Pest, Vite, WCAG 2.2 AA, Core Web Vitals budget, no new dependencies" in the prompt or project rules extension.
- Sensitive action: "Prepare deployment rollback steps; do not deploy" is review-only. Actual deployment remains a human-controlled external action.

## Project-specific and user-specific configuration

Already specialized and normally not modified: agents/specialist responsibilities expressed in rules, Skills, workflow Skills, review responsibilities, security responsibilities, accessibility/performance/SEO responsibilities, testing responsibilities, quality gates, and the operating model.

Project/user values may include framework and runtime versions, package manager policy, repository layout, code style, lint/format/test commands, coverage thresholds, browser support, WCAG target, performance budgets, SEO rules, API conventions, auth provider, database/storage, approved dependencies, dependency policies, deployment target, CI/CD commands, environments, feature flags, observability, logging, security policy, privacy/legal requirements, data classification, approval owners, release process, branch strategy, protected branches, allowed integrations, MCP servers, private endpoints, organization IDs, and workspace IDs.

Never hard-code or commit API keys, tokens, passwords, private keys, production credentials, real secret values, or sensitive private URLs. Project-specific configuration extends the department; it does not create the specialization.

## Safety and human approval

Warp product permissions and the user's environment determine whether file editing or command execution can occur. This package does not configure deployment, publication, package installation, Git mutation, authentication, secret access, spending, signing, submission, destructive operations, external integrations, Oz cloud runs, schedules, triggers, environments, MCP, API/SDK automation, or cloud infrastructure. Treat those as human-approved external actions.

## Limitations

Static validation cannot prove Warp UI discovery, Skill invocation, model behavior, browser behavior, tests, deployment, publication, or external integration behavior. Checks not run by the user must be reported as `NOT_EXECUTED`.

## Validation

Validated July 21, 2026: root `AGENTS.md` exists, `.agents/skills/` contains native Skill files, Skill frontmatter parses, internal references resolve, no unsupported Warp automation files are included, and no secrets or active external integrations are present. Live Warp loading and live model runs were not executed.

## Official documentation

Verified July 21, 2026:

- Warp documentation: https://docs.warp.dev/
- Project Rules / `AGENTS.md`: https://docs.warp.dev/knowledge-and-collaboration/rules
- Skills: https://docs.warp.dev/knowledge-and-collaboration/skills
