# Cursor Cybersecurity Security Architecture Engineering

This package configures Cursor-native static guidance for Cybersecurity Area 02: Security Architecture Engineering.

## Native Artifacts

- `AGENTS.md` defines area scope, mission, routing, safety boundaries, and structured output requirements.
- `.cursor/rules/security-architecture-engineering.mdc` applies Cursor workspace rules for scope and safety.
- `.cursor/agents/*.md` defines specialized read-only agents for architecture governance, solution architecture, identity/cloud/network, data/container/automation, and independent review.
- `.cursor/skills/*/SKILL.md` defines reusable static workflows for architecture review, reference patterns, identity/cloud/network/data design, and container/IaC/automation review.
- `reference/NATIVE_SOURCES.md` records official Cursor documentation checked for native feature support.

## Scope Boundaries

The package supports design, review, documentation, governance, and independent assurance of security architectures. It does not approve architectures, accept risk, publish standards, deploy controls, operate production systems, authenticate to services, run scans, or manage incidents.

Use the structured output header in `AGENTS.md` for every deliverable and route high-impact artifacts to the independent reviewer.
