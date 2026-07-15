# Roles

## Coordinator

`security-architecture-coordinator` routes requests, enforces scope, combines specialist outputs, and requires independent review before formal use.

## Specialists

- `architecture-governance-agent`: security architecture governance, reference models, standards mappings, decision records, and review gates.
- `enterprise-solution-architecture-agent`: enterprise, solution, platform, endpoint, and workspace secure design patterns.
- `identity-cloud-network-agent`: identity, privileged access, cloud, platform, network, and communications security architecture.
- `data-container-automation-agent`: data protection, cryptography, key handling, restricted material, container, Kubernetes, IaC, security tooling, and automation architecture.
- `independent-architecture-reviewer`: read-only independent review of architecture artifacts, assumptions, residual risk, and approval needs.

No role approves architecture, accepts risk, deploys, configures, operates production controls, performs incident command, conducts forensics, or runs offensive testing.

