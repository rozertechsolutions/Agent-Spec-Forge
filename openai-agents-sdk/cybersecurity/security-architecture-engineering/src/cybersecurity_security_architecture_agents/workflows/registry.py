from __future__ import annotations

from dataclasses import dataclass

from cybersecurity_security_architecture_agents.context import ArchitectureDomain, WorkflowRequest


@dataclass(frozen=True, slots=True)
class WorkflowSpec:
    name: str
    objective: str
    trigger: str
    supported_domains: frozenset[ArchitectureDomain]
    primary_owner: str
    reviewers: tuple[str, ...]
    ordered_steps: tuple[str, ...]
    validation_gates: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    evidence: tuple[str, ...]
    outputs: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    human_approvals: tuple[str, ...]
    prohibited_actions: tuple[str, ...]

    def validate_request(self, request: WorkflowRequest) -> tuple[str, ...]:
        issues: list[str] = []
        if request.workflow != self.name:
            issues.append(f"request workflow {request.workflow!r} does not match {self.name!r}")
        unsupported = request.domains - self.supported_domains
        if unsupported:
            issues.append("unsupported domains: " + ", ".join(sorted(d.value for d in unsupported)))
        if request.cancellation_requested:
            issues.append("cancellation requested")
        missing_approvals = set(self.human_approvals) - set(request.human_approvals)
        if missing_approvals:
            issues.append("missing approvals: " + ", ".join(sorted(missing_approvals)))
        return tuple(issues)


ALL_DOMAINS = frozenset(ArchitectureDomain)
FINAL_REVIEW = ("independent-architecture-reviewer",)


WORKFLOW_SPECS: dict[str, WorkflowSpec] = {
    "security-architecture-governance": WorkflowSpec(
        name="security-architecture-governance",
        objective="Create traceable security architecture governance, reference, standards, ownership, and decision artifacts.",
        trigger="Architecture governance, reference model, decision record, or review gate request.",
        supported_domains=frozenset({ArchitectureDomain.GOVERNANCE}),
        primary_owner="architecture-governance-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("confirm scope", "identify authorities", "map standards", "draft decisions", "list approvals", "independent review"),
        validation_gates=("source for every mapping", "inferences flagged", "approval needs listed"),
        stop_conditions=("policy approval requested", "risk acceptance requested", "missing authoritative source"),
        evidence=("standards", "control IDs", "architecture principles", "decision history"),
        outputs=("governance model", "reference index", "standards mapping", "decision record", "approval log"),
        acceptance_criteria=("traceable mappings", "reviewer findings addressed or listed", "human approvals explicit"),
        human_approvals=(),
        prohibited_actions=("approve policy", "accept risk", "certify architecture"),
    ),
    "enterprise-solution-patterns": WorkflowSpec(
        name="enterprise-solution-patterns",
        objective="Review enterprise, solution, platform, endpoint, and workspace designs for secure reusable patterns.",
        trigger="Enterprise, solution, platform, endpoint, or workspace architecture review request.",
        supported_domains=frozenset({ArchitectureDomain.ENTERPRISE_SOLUTION, ArchitectureDomain.ENDPOINT_WORKSPACE}),
        primary_owner="enterprise-solution-architecture-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("inventory assets", "map trust boundaries", "map patterns", "document tradeoffs", "prepare decision package", "independent review"),
        validation_gates=("assets mapped", "dependencies recorded", "residual risk documented"),
        stop_conditions=("deployment requested", "product delivery requested", "insufficient architecture context"),
        evidence=("architecture diagrams", "asset inventory", "trust boundaries", "data flows"),
        outputs=("design review", "pattern map", "gap register", "dependency register", "decision package"),
        acceptance_criteria=("sources listed", "assumptions labeled", "review complete or required"),
        human_approvals=(),
        prohibited_actions=("deploy changes", "operate controls", "approve architecture"),
    ),
    "identity-cloud-network-data-design": WorkflowSpec(
        name="identity-cloud-network-data-design",
        objective="Draft identity, privileged access, cloud, platform, network, communications, data protection, and cryptography target state.",
        trigger="Identity, cloud, network, data protection, cryptography, or communications architecture request.",
        supported_domains=frozenset({
            ArchitectureDomain.IDENTITY_ACCESS,
            ArchitectureDomain.CLOUD_PLATFORM,
            ArchitectureDomain.NETWORK_COMMUNICATIONS,
            ArchitectureDomain.DATA_CRYPTOGRAPHY,
        }),
        primary_owner="identity-cloud-network-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("confirm environment scope", "map administration paths", "map data classes", "draft target state", "list decisions", "independent review"),
        validation_gates=("administration paths reviewed", "cloud boundaries mapped", "network paths documented"),
        stop_conditions=("access change requested", "live configuration requested", "key operation requested"),
        evidence=("identity flows", "privilege model", "cloud topology", "network paths", "data classes"),
        outputs=("target-state design", "control pattern map", "segmentation review", "data protection notes", "dependency log"),
        acceptance_criteria=("dependencies recorded", "approval needs listed", "review complete or required"),
        human_approvals=(),
        prohibited_actions=("grant access", "change live configuration", "operate network controls"),
    ),
    "container-iac-automation-review": WorkflowSpec(
        name="container-iac-automation-review",
        objective="Review container, Kubernetes, IaC, security tooling, and automation architecture patterns.",
        trigger="Container, orchestration, IaC, security tooling, or automation design request.",
        supported_domains=frozenset({ArchitectureDomain.CONTAINER_IAC, ArchitectureDomain.AUTOMATION_PATTERNS}),
        primary_owner="data-container-automation-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("confirm assets", "map orchestration boundaries", "review IaC guardrails", "design human gates", "document residual risk", "independent review"),
        validation_gates=("orchestration boundaries reviewed", "automation gates defined", "restricted material handling documented"),
        stop_conditions=("deployment requested", "cluster operation requested", "live key operation requested"),
        evidence=("orchestration design", "IaC modules", "automation requirements", "security tooling assumptions"),
        outputs=("orchestration review", "IaC guardrail map", "automation design package", "residual risk notes"),
        acceptance_criteria=("sources listed", "human gates explicit", "review complete or required"),
        human_approvals=(),
        prohibited_actions=("deploy IaC", "operate clusters", "activate integrations"),
    ),
    "independent-architecture-assurance": WorkflowSpec(
        name="independent-architecture-assurance",
        objective="Provide independent read-only review before security architecture artifacts are treated as complete.",
        trigger="Review, final validation, evidence challenge, or readiness request.",
        supported_domains=ALL_DOMAINS,
        primary_owner="independent-architecture-reviewer",
        reviewers=(),
        ordered_steps=("confirm independence", "verify scope", "compare claims to evidence", "flag gaps", "order findings", "report readiness"),
        validation_gates=("self-review excluded", "findings sourced", "approvals explicit", "unavailable evidence reported"),
        stop_conditions=("self-review detected", "approval requested from reviewer", "production operation requested"),
        evidence=("draft artifact", "source evidence", "assumptions", "acceptance criteria"),
        outputs=("findings", "evidence gaps", "residual risk notes", "approval requirements", "readiness recommendation"),
        acceptance_criteria=("severity ordered findings", "residual risk listed", "human approval requirements explicit"),
        human_approvals=(),
        prohibited_actions=("implement changes", "approve architecture", "accept risk", "close findings"),
    ),
}


def get_workflow(name: str) -> WorkflowSpec:
    try:
        return WORKFLOW_SPECS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown workflow: {name}") from exc

