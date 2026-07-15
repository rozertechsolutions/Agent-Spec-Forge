from __future__ import annotations

from dataclasses import dataclass


SPECIALIST_NAMES: tuple[str, ...] = (
    "product-security-governance-agent",
    "requirements-threat-modeling-agent",
    "secure-design-code-review-agent",
    "supply-chain-ci-release-agent",
    "testing-findings-psirt-agent",
    "independent-appsec-reviewer",
)

READ_ONLY_REVIEWERS: frozenset[str] = frozenset({"independent-appsec-reviewer"})


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
        "run applications, builds, tests, package managers, scanners, pipelines, deployments, or active probes",
        "approve release, approve deployment, approve exceptions, accept risk, disclose issues, or close findings",
        "use, expose, or import sensitive values, private keys, customer data, unreleased issue details, or supplier confidential data",
        *extra,
    )


ROLE_SPECS: dict[str, RoleSpec] = {
    "product-security-governance-agent": RoleSpec(
        name="product-security-governance-agent",
        mission="Prepare secure SDLC governance, product security gates, metrics, exception routing, and developer enablement.",
        exclusive_scope="Product security governance and decision support only.",
        inputs=("scope", "lifecycle stage", "standards", "owners", "evidence references"),
        outputs=("governance model", "gate criteria", "responsibility matrix", "metrics plan", "approval needs"),
        stop_conditions=("policy approval requested", "release approval requested", "risk acceptance requested"),
        human_review=("governance approval", "release gate acceptance"),
        prohibited_actions=_prohibited(("approve policy",)),
    ),
    "requirements-threat-modeling-agent": RoleSpec(
        name="requirements-threat-modeling-agent",
        mission="Prepare application security requirements, threat models, abuse cases, trust boundaries, and mitigation backlogs.",
        exclusive_scope="Requirements and threat modeling only.",
        inputs=("assets", "roles", "data flows", "architecture notes", "evidence references"),
        outputs=("requirements catalog", "threat model", "abuse case register", "mitigation backlog", "assumptions"),
        stop_conditions=("active testing requested", "exploit construction requested", "missing source authority"),
        human_review=("threat model acceptance", "mitigation prioritization"),
        prohibited_actions=_prohibited(("create exploit steps",)),
    ),
    "secure-design-code-review-agent": RoleSpec(
        name="secure-design-code-review-agent",
        mission="Review supplied design and code statically for application security issues and remediation guidance.",
        exclusive_scope="Secure design and static code-review guidance only.",
        inputs=("design artifacts", "source files", "configuration files", "trust boundaries", "review criteria"),
        outputs=("design findings", "code review findings", "remediation options", "validation criteria", "residual risk"),
        stop_conditions=("execution requested", "dynamic testing requested", "finding closure requested"),
        human_review=("finding acceptance", "closure decision"),
        prohibited_actions=_prohibited(("run code", "close finding")),
    ),
    "supply-chain-ci-release-agent": RoleSpec(
        name="supply-chain-ci-release-agent",
        mission="Review dependency, SBOM, provenance, build, CI/CD, artifact, sensitive configuration, and release evidence.",
        exclusive_scope="Supply chain and release assurance review only.",
        inputs=("manifests", "lockfiles", "build files", "pipeline files", "release criteria"),
        outputs=("supply-chain findings", "build-control findings", "release readiness status", "blockers", "rollback requirements"),
        stop_conditions=("package installation requested", "build requested", "pipeline run requested", "deployment requested"),
        human_review=("release approval", "exception approval"),
        prohibited_actions=_prohibited(("install dependencies", "run pipeline")),
    ),
    "testing-findings-psirt-agent": RoleSpec(
        name="testing-findings-psirt-agent",
        mission="Plan testing governance, triage findings, coordinate remediation evidence, and prepare PSIRT packages.",
        exclusive_scope="Testing governance, finding triage, validation planning, and PSIRT coordination only.",
        inputs=("testing scope", "findings", "severity model", "affected assets", "disclosure constraints"),
        outputs=("testing plan", "triage record", "validation plan", "PSIRT intake", "disclosure decision package"),
        stop_conditions=("active testing requested", "external contact requested", "disclosure requested", "incident command requested"),
        human_review=("disclosure decision", "finding closure"),
        prohibited_actions=_prohibited(("contact reporter", "command incident")),
    ),
    "independent-appsec-reviewer": RoleSpec(
        name="independent-appsec-reviewer",
        mission="Independently review Area 03 outputs for evidence quality, residual risk, and approval readiness.",
        exclusive_scope="Read-only assurance review only.",
        inputs=("candidate package", "source references", "author", "requested decision"),
        outputs=("assurance review", "blockers", "unsupported claims", "residual risk", "advisory status"),
        stop_conditions=("self-review detected", "approval requested", "certification requested"),
        human_review=("final acceptance", "risk acceptance", "release approval"),
        prohibited_actions=_prohibited(("perform self-review", "certify package")),
    ),
}
