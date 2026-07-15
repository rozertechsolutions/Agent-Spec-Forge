from __future__ import annotations

from .definitions import ROLE_SPECS, RoleSpec


COORDINATOR_NAME = "application-product-devsecops-security-coordinator"


def route_for_workflow(workflow: str) -> RoleSpec:
    routing = {
        "secure-sdlc-governance": "product-security-governance-agent",
        "requirements-threat-modeling": "requirements-threat-modeling-agent",
        "secure-design-code-review": "secure-design-code-review-agent",
        "supply-chain-ci-release": "supply-chain-ci-release-agent",
        "testing-findings-psirt": "testing-findings-psirt-agent",
        "independent-appsec-review": "independent-appsec-reviewer",
    }
    return ROLE_SPECS[routing[workflow]]
