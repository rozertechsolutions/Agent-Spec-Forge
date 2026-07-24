# GitHub Copilot

Surfaces:
- Supported IDEs
- Copilot CLI

Repository-level instructions, custom agents and Skills can be shared, so they live under
`common/`.

Native mechanisms demonstrated:
- Repository-wide instructions: `.github/copilot-instructions.md`
- Path-specific instructions: `.github/instructions/*.instructions.md`
- Repository custom agents: `.github/agents/*.agent.md`
- Repository Skills: `.github/skills/<skill>/SKILL.md`

CLI-specific user-level hooks, plugins and settings are supported but are not needed by this
minimal repository example.

Official documentation:
- https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot
- https://docs.github.com/en/copilot/reference/custom-agents-configuration
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/comparing-cli-features
