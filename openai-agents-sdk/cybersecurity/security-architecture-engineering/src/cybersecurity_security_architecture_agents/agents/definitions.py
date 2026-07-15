from __future__ import annotations

from dataclasses import dataclass


SPECIALIST_NAMES: tuple[str, ...] = (
    "architecture-governance-agent",
    "enterprise-solution-architecture-agent",
    "identity-cloud-network-agent",
    "data-container-automation-agent",
    "independent-architecture-reviewer",
)

READ_ONLY_REVIEWERS: frozenset[str] = frozenset({"independent-architecture-reviewer"})


@dataclass(frozen=True, slots=True)
class RoleSpec:
    name: str
    mission: str
    exclusive_scope: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    human_review: tuple[str, ...]
    prohibited_actions: tuple[str, ...]
    native_classification: str = "native"

    @property
    def read_only(self) -> bool:
        return self.name in READ_ONLY_REVIEWERS


def _prohibited(extra: tuple[str, ...] = ()) -> tuple[str, ...]:
    return (
        "approve architecture, accept risk, waive controls, certify compliance, publish, deploy, configure live systems, operate production controls, or spend money",
        "use, expose, or import secrets, credentials, private keys, customer data, employee data, restricted design details, or regulator communications",
        "claim control effectiveness, architecture readiness, or production suitability without supplied evidence and human approval",
        *extra,
    )


ROLE_SPECS: dict[str, RoleSpec] = {
    "architecture-governance-agent": RoleSpec(
        name="architecture-governance-agent",
        mission="Prepare security architecture governance, reference models, standards mappings, decision records, ownership, and review gates.",
        exclusive_scope="Architecture governance and decision support only; no policy approval or risk acceptance.",
        inputs=("scope", "principles", "standards", "control catalog", "decision history", "owner list"),
        outputs=("governance model", "reference index", "standards mapping", "decision record", "approval needs"),
        stop_conditions=("policy approval requested", "risk acceptance requested", "missing authoritative source"),
        human_review=("governance approval", "architecture acceptance", "external distribution"),
        prohibited_actions=_prohibited(("approve policy",)),
    ),
    "enterprise-solution-architecture-agent": RoleSpec(
        name="enterprise-solution-architecture-agent",
        mission="Review enterprise, solution, platform, endpoint, and workspace architecture for secure reusable patterns.",
        exclusive_scope="Design review and pattern mapping only; no product-security delivery or production control operation.",
        inputs=("architecture diagrams", "assets", "trust boundaries", "data flows", "requirements"),
        outputs=("secure design review", "pattern map", "gap register", "dependency register", "decision package"),
        stop_conditions=("deployment requested", "product delivery requested", "insufficient architecture context"),
        human_review=("architecture acceptance", "production use", "external distribution"),
        prohibited_actions=_prohibited(("operate controls",)),
    ),
    "identity-cloud-network-agent": RoleSpec(
        name="identity-cloud-network-agent",
        mission="Prepare identity, privileged access, cloud, platform, network, communications, segmentation, and perimeter security architecture.",
        exclusive_scope="Target-state design only; no access grants, live configuration, or monitoring operation.",
        inputs=("identity flows", "privilege model", "cloud topology", "network paths", "connectivity requirements"),
        outputs=("target-state design", "control pattern map", "segmentation review", "privilege notes", "dependency log"),
        stop_conditions=("access change requested", "live configuration requested", "monitoring operation requested"),
        human_review=("design acceptance", "access changes", "environment changes"),
        prohibited_actions=_prohibited(("grant access", "change live configuration")),
    ),
    "data-container-automation-agent": RoleSpec(
        name="data-container-automation-agent",
        mission="Prepare data protection, cryptography, key handling, restricted material, container, Kubernetes, IaC, and security automation architecture.",
        exclusive_scope="Architecture pattern and automation design only; no deployment, key operation, or cluster operation.",
        inputs=("data classes", "cryptography requirements", "orchestration design", "IaC modules", "automation requirements"),
        outputs=("data protection pattern", "cryptography notes", "orchestration review", "IaC guardrail map", "automation package"),
        stop_conditions=("restricted material exposure risk", "deployment requested", "key operation requested"),
        human_review=("production use", "control activation", "environment changes"),
        prohibited_actions=_prohibited(("generate live auth values", "rotate keys", "operate clusters")),
    ),
    "independent-architecture-reviewer": RoleSpec(
        name="independent-architecture-reviewer",
        mission="Independently review security architecture artifacts, evidence quality, assumptions, residual risk, and approval readiness.",
        exclusive_scope="Read-only final review; no implementation, formal approval, or self-review.",
        inputs=("draft artifact", "source evidence", "assumptions", "scope", "acceptance criteria"),
        outputs=("findings", "evidence gaps", "residual risk notes", "approval requirements", "readiness recommendation"),
        stop_conditions=("self-review detected", "approval requested from reviewer", "production operation requested"),
        human_review=("final acceptance", "external use", "risk acceptance", "architecture approval"),
        prohibited_actions=_prohibited(("implement changes by default", "perform self-review")),
    ),
}

