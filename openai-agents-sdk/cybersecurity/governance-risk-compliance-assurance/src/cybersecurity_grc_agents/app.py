from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from cybersecurity_grc_agents.agents.definitions import ROLE_SPECS
from cybersecurity_grc_agents.config import GrcAgentsConfig
from cybersecurity_grc_agents.context import GrcDomain, WorkflowRequest
from cybersecurity_grc_agents.outputs import (
    CompletionCriterion,
    CriterionStatus,
    WorkflowResult,
    WorkflowState,
)
from cybersecurity_grc_agents.workflows.registry import WorkflowSpec, get_workflow


DOMAIN_OWNER: dict[GrcDomain, str] = {
    GrcDomain.GOVERNANCE_POLICY: "governance-policy-frameworks-agent",
    GrcDomain.CYBER_RISK: "cyber-risk-exceptions-agent",
    GrcDomain.ASSURANCE_EVIDENCE: "assurance-evidence-remediation-agent",
    GrcDomain.THIRD_PARTY_MATURITY: "third-party-maturity-reporting-agent",
    GrcDomain.INDEPENDENT_REVIEW: "independent-assurance-reviewer",
}


@dataclass(frozen=True, slots=True)
class RoutedWorkflow:
    spec: WorkflowSpec
    primary_owner: str
    reviewers: tuple[str, ...]
    validation_issues: tuple[str, ...]


def configure_sdk(config: GrcAgentsConfig | None = None) -> None:
    resolved = config or GrcAgentsConfig.from_env()
    if resolved.tracing_disabled:
        try:
            from agents import set_tracing_disabled
        except ImportError:
            return
        set_tracing_disabled(True)


def select_owner(request: WorkflowRequest, spec: WorkflowSpec) -> str:
    if len(request.domains) == 1:
        return DOMAIN_OWNER[next(iter(request.domains))]
    return spec.primary_owner


def route_workflow(request: WorkflowRequest) -> RoutedWorkflow:
    spec = get_workflow(request.workflow)
    issues = list(spec.validate_request(request))
    owner = select_owner(request, spec)
    reviewers = tuple(reviewer for reviewer in spec.reviewers if reviewer != owner)
    if owner != "independent-assurance-reviewer" and "independent-assurance-reviewer" not in reviewers:
        issues.append("independent-assurance-reviewer must be an independent final reviewer")
    if owner in reviewers:
        issues.append("self-review is not allowed")
    return RoutedWorkflow(spec=spec, primary_owner=owner, reviewers=reviewers, validation_issues=tuple(issues))


def classify_completion_criteria(spec: WorkflowSpec, request: WorkflowRequest) -> tuple[CompletionCriterion, ...]:
    criteria: list[CompletionCriterion] = [
        CompletionCriterion("scope and evidence traceability", CriterionStatus.REQUIRED, "Every workflow starts from explicit scope and evidence state."),
        CompletionCriterion("security and protected material handling", CriterionStatus.REQUIRED, "Secrets and sensitive evidence are always protected."),
        CompletionCriterion("human approval boundaries", CriterionStatus.REQUIRED, "Formal approvals are outside agent authority."),
    ]
    domain_values = {domain.value for domain in request.domains}
    for domain in GrcDomain:
        if domain in request.domains:
            criteria.append(CompletionCriterion(domain.value, CriterionStatus.CONDITIONALLY_REQUIRED, f"{domain.value} requested."))
        else:
            criteria.append(CompletionCriterion(domain.value, CriterionStatus.NOT_APPLICABLE, f"{domain.value} not in scope; requested: {sorted(domain_values)}."))
    if spec.name != "independent-assurance-review":
        criteria.append(CompletionCriterion("independent assurance review", CriterionStatus.REQUIRED, "Final review is required before formal use."))
    return tuple(criteria)


def dry_run_workflow(request: WorkflowRequest) -> WorkflowResult:
    routed = route_workflow(request)
    state = WorkflowState.NEEDS_APPROVAL if routed.validation_issues else WorkflowState.PLANNED
    return WorkflowResult(
        workflow=routed.spec.name,
        state=state,
        primary_owner=routed.primary_owner,
        reviewers=routed.reviewers,
        criteria=classify_completion_criteria(routed.spec, request),
        limitations=routed.validation_issues,
    )


async def run_workflow(request: WorkflowRequest, config: GrcAgentsConfig | None = None) -> Any:
    routed = route_workflow(request)
    if routed.validation_issues:
        return dry_run_workflow(request)
    configure_sdk(config)
    from agents import Runner
    from cybersecurity_grc_agents.agents.coordinator import build_coordinator_agent

    coordinator = build_coordinator_agent(config)
    prompt = (
        f"Execute workflow {routed.spec.name}. Primary owner: {routed.primary_owner}. "
        f"Reviewers: {', '.join(routed.reviewers)}. Objective: {request.objective}. "
        "Do not approve policy, accept risk, certify compliance, sign off audit, approve vendors, submit filings, publish, deploy, activate integrations, import credentials, or fabricate evidence."
    )
    return await Runner.run(coordinator, prompt)


def responsibility_matrix() -> dict[str, dict[str, str | bool]]:
    return {
        name: {
            "exclusive_scope": spec.exclusive_scope,
            "read_only": spec.read_only,
            "native_classification": spec.native_classification,
        }
        for name, spec in ROLE_SPECS.items()
    }
