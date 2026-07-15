# Responsibility Matrix

| Area | Primary agent | Human-only decisions |
| --- | --- | --- |
| Architecture governance, principles, standards, reference models, ADRs, review gates | `architecture-governance-agent` | Standard approval, exception approval, risk acceptance |
| Enterprise and solution architecture, context, trust boundaries, data flows, resilience | `enterprise-solution-architecture-agent` | Architecture approval, delivery commitment |
| IAM, PAM, cloud, platform, network, communications, endpoint, workspace | `identity-cloud-network-agent` | Privileged access approval, production control operation |
| Data protection, cryptography, protected material, container, Kubernetes, IaC, automation | `data-container-automation-agent` | Cryptographic authority decisions, production automation enablement |
| Independent review | `independent-architecture-reviewer` | Artifact approval, self-review |

Only one primary agent owns each artifact. Independent review is mandatory for high-impact outputs and must remain read-only.
