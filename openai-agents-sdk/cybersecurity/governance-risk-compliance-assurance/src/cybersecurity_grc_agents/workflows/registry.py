from __future__ import annotations

from dataclasses import dataclass

from cybersecurity_grc_agents.context import GrcDomain, WorkflowRequest


@dataclass(frozen=True, slots=True)
class WorkflowSpec:
    name: str
    objective: str
    trigger: str
    supported_domains: frozenset[GrcDomain]
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


ALL_DOMAINS = frozenset(GrcDomain)
FINAL_REVIEW = ("independent-assurance-reviewer",)


WORKFLOW_SPECS: dict[str, WorkflowSpec] = {
    "governance-policy-frameworks": WorkflowSpec(
        name="governance-policy-frameworks",
        objective="Create traceable governance, policy, standards, ownership, and framework mapping artifacts.",
        trigger="Policy, standard, control framework, ownership, or crosswalk request.",
        supported_domains=frozenset({GrcDomain.GOVERNANCE_POLICY}),
        primary_owner="governance-policy-frameworks-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("confirm scope", "identify source authorities", "map requirements", "draft ownership", "record gaps", "independent review"),
        validation_gates=("source for every mapping", "inferences flagged", "approval needs listed"),
        stop_conditions=("legal interpretation", "unsupported compliance claim", "missing authoritative source"),
        evidence=("framework clauses", "policy sections", "control IDs", "assumption log"),
        outputs=("policy draft", "control crosswalk", "RACI", "gap register", "decision log"),
        acceptance_criteria=("traceable mappings", "reviewer findings addressed or listed", "human approvals explicit"),
        human_approvals=(),
        prohibited_actions=("approve policy", "certify compliance", "external distribution"),
    ),
    "risk-exceptions-remediation": WorkflowSpec(
        name="risk-exceptions-remediation",
        objective="Prepare cyber risk, exception, treatment, residual-risk, and remediation governance packages.",
        trigger="Risk register, exception, acceptance package, or remediation governance request.",
        supported_domains=frozenset({GrcDomain.CYBER_RISK}),
        primary_owner="cyber-risk-exceptions-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("define risk context", "validate assumptions", "document treatment options", "draft remediation milestones", "list decisions", "independent review"),
        validation_gates=("owner defined", "evidence labeled", "treatment options documented", "approval needs listed"),
        stop_conditions=("risk acceptance requested", "control waiver requested", "closure approval requested"),
        evidence=("risk rationale", "control gap sources", "compensating controls", "residual-risk notes"),
        outputs=("risk update", "exception package", "treatment summary", "remediation plan"),
        acceptance_criteria=("decision owner explicit", "risk acceptance not performed", "review complete or required"),
        human_approvals=(),
        prohibited_actions=("accept risk", "waive controls", "approve remediation closure"),
    ),
    "assurance-third-party-reporting": WorkflowSpec(
        name="assurance-third-party-reporting",
        objective="Prepare assurance, evidence, third-party risk, maturity, executive status, and remediation reporting outputs.",
        trigger="Assurance, audit evidence, vendor risk, maturity reporting, or dashboard request.",
        supported_domains=frozenset({GrcDomain.ASSURANCE_EVIDENCE, GrcDomain.THIRD_PARTY_MATURITY}),
        primary_owner="assurance-evidence-remediation-agent",
        reviewers=FINAL_REVIEW,
        ordered_steps=("confirm audience", "map scope to evidence", "classify evidence state", "document gaps", "prepare report", "independent review"),
        validation_gates=("each claim sourced or labeled", "each gap owned when available", "external claims flagged"),
        stop_conditions=("audit sign-off requested", "vendor approval requested", "unsupported maturity claim"),
        evidence=("evidence inventory", "vendor data", "maturity criteria", "issue register"),
        outputs=("evidence request list", "assurance status", "vendor risk summary", "maturity rationale", "dashboard narrative"),
        acceptance_criteria=("evidence states explicit", "human decisions listed", "review complete or required"),
        human_approvals=(),
        prohibited_actions=("certify effectiveness", "approve vendor", "distribute external report"),
    ),
    "independent-assurance-review": WorkflowSpec(
        name="independent-assurance-review",
        objective="Provide independent read-only review before GRC artifacts are treated as complete.",
        trigger="Review, final validation, evidence challenge, or readiness request.",
        supported_domains=ALL_DOMAINS,
        primary_owner="independent-assurance-reviewer",
        reviewers=(),
        ordered_steps=("confirm independence", "verify scope", "compare claims to evidence", "flag gaps", "order findings", "report readiness"),
        validation_gates=("self-review excluded", "findings sourced", "approvals explicit", "unavailable evidence reported"),
        stop_conditions=("self-review detected", "legal interpretation required", "approval requested from reviewer"),
        evidence=("draft artifact", "source evidence", "assumptions", "acceptance criteria"),
        outputs=("findings", "evidence gaps", "approval requirements", "readiness recommendation"),
        acceptance_criteria=("severity ordered findings", "residual risk listed", "human approval requirements explicit"),
        human_approvals=(),
        prohibited_actions=("implement changes", "approve risk", "certify compliance", "close findings"),
    ),
}


def get_workflow(name: str) -> WorkflowSpec:
    try:
        return WORKFLOW_SPECS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown workflow: {name}") from exc
