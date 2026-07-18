# Marketing remediation prompts by platform

This package contains 18 independent English prompts for correcting the existing
Marketing specialization in AI Specialized Departments.

## Use

Run one prompt at a time, from the matching platform directory or repository root.
Do not combine them into one execution.

Each prompt:

- works only inside `<platform>/marketing/**`;
- requires three independent static reviews;
- uses current official documentation as the source of truth;
- defines a closed deletion allowlist;
- prohibits every deletion not explicitly named;
- removes model-generated `human_approved`;
- corrects least-privilege and reviewer independence;
- migrates generic workflow documents only when a native retained mechanism exists;
- prohibits Git, terminal execution, tests, builds, installs, authentication, and live
  external actions.

## Recommended order

1. chatgpt
2. claude
3. claude-code
4. cline
5. codex
6. cursor
7. gemini-cli
8. github-copilot
9. junie
10. kilo-code
11. kiro
12. local
13. mistral-vibe
14. openai-agents-sdk
15. opencode
16. qwen-code
17. warp
18. windsurf

The prompts for `cline`, `cursor`, and `gemini-cli` are included even though those
platforms were missing from the submitted `marketing.zip`, because their Marketing
trees exist in the full repository package and require correction.
