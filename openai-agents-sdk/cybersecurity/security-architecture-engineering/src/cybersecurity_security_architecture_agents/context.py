from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ArchitectureDomain(str, Enum):
    GOVERNANCE = "security-architecture-governance"
    ENTERPRISE_SOLUTION = "enterprise-solution-architecture"
    IDENTITY_ACCESS = "identity-access-architecture"
    CLOUD_PLATFORM = "cloud-platform-architecture"
    NETWORK_COMMUNICATIONS = "network-communications-architecture"
    ENDPOINT_WORKSPACE = "endpoint-workspace-architecture"
    DATA_CRYPTOGRAPHY = "data-cryptography-architecture"
    CONTAINER_IAC = "container-kubernetes-iac-architecture"
    AUTOMATION_PATTERNS = "security-engineering-automation-patterns"
    INDEPENDENT_REVIEW = "architecture-assurance-independent-review"


@dataclass(frozen=True, slots=True)
class WorkflowRequest:
    workflow: str
    objective: str
    domains: frozenset[ArchitectureDomain]
    human_approvals: tuple[str, ...] = ()
    cancellation_requested: bool = False

