# AI Specialized Departments — DevOps and Cloud Prompt Package

This package contains only the validated executable master prompts for the DevOps and Cloud specialization.

## Contents

It contains the ten validated section master prompts and the final audit/merge prompt.

It also contains:

- A current official-documentation discovery baseline.
- A final cross-platform static audit and merge prompt.
- A package validation report with file hashes.

## Execution order

Run only the ten master prompts, in numeric order, followed by the final audit and merge prompt.

The independent drafts and comparison reports are included as evidence of the requested three-way design and consolidation process. They are not intended to be executed after the master exists.

## Repository behavior encoded in the prompts

- Section 01 creates or resumes `feature/devops-cloud` from `main`.
- Sections 02–10 require that branch.
- Each section processes platforms sequentially and performs three static verification passes before moving forward.
- Each section commits and pushes only after full section validation.
- The final audit owns the merge to `main`.
- The feature branch is preserved locally and remotely.
- Generated configurations are never executed.
