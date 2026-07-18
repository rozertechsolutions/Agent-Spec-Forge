# GitHub Copilot - Software Development

This directory configures GitHub Copilot for the Software Development specialization.

## Native Surfaces

- `.github/copilot-instructions.md` makes the primary Copilot agent/session the Software Development Lead.
- `.github/agents/` contains seven specialist `.agent.md` files; there is intentionally no Lead agent.
- `.github/instructions/software-development.instructions.md` is a concise path-scoped reminder file.
- `.github/prompts/*.prompt.md` contains prompt-only workflow guidance.
- `.github/skills/` contains static reusable Skills.

## Safety Model

Specialists return bounded evidence to the primary session, cannot recursively delegate, cannot expand scope, and cannot claim final completion. Reviewers and planners are read-only. The implementation specialist may edit with human approval but may not commit, push, create issues, open or merge pull requests, deploy, publish, sign, release, authenticate, or use unrestricted terminal/network tools.

IDE, account, organization, and product-surface support may vary. Runtime loading and GitHub operations have not been performed from this repository package.
