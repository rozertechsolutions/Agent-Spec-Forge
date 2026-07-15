from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from cybersecurity_security_architecture_agents.agents.definitions import ROLE_SPECS
from cybersecurity_security_architecture_agents.config import SecurityArchitectureConfig
from cybersecurity_security_architecture_agents.context import ArchitectureDomain, WorkflowRequest
from cybersecurity_security_architecture_agents.outputs import (
    CompletionCriterion,
    CriterionStatus,
    WorkflowResult,
    WorkflowState,
)
from cybersecurity_security_architecture_agents.workflows.registry import WorkflowSpec, get_workflow


DOMAIN_OWNER: dict[ArchitectureDomain, str] = {
    ArchitectureDomain.GOVERNANCE: "architecture-governance-agent",
    ArchitectureDomain.ENTERPRISE_SOLUTION: "enterprise-solution-architecture-agent",
    ArchitectureDomain.ENDPOINT_WORKSPACE: "enterprise-solution-architecture-agent",
    ArchitectureDomain.IDENTITY_ACCESS: "identity-cloud-network-agent",
    ArchitectureDomain.CLOUD_PLATFORM: "identity-cloud-network-agent",
    ArchitectureDomain.NETWORK_COMMUNICATIONS: "identity-cloud-network-agent",
    ArchitectureDomain.DATA_CRYPTOGRAPHY: "data-container-automation-agent",
    ArchitectureDomain.CONTAINER_IAC: "data-container-automation-agent",
    ArchitectureDomain.AUTOMATION_PATTERNS: "data-container-automation-agent",
    ArchitectureDomain.INDEPENDENT_REVIEW: "independent-architecture-reviewer",
}


@dataclass(frozen=True, slots=True)
class RoutedWorkflow:
    spec: WorkflowSpec
    primary_owner: str
    reviewers: tuple[str, ...]
    validation_issues: tuple[str, ...]


def configure_sdk(config: SecurityArchitectureConfig | None = None) -> None:
    resolved = config or SecurityArchitectureConfig.from_env()
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
    if owner != "independent-architecture-reviewer" and "independent-architecture-reviewer" not in reviewers:
        issues.append("independent-architecture-reviewer must be an independent final reviewer")
    if owner in reviewers:
        issues.append("self-review is not allowed")
    return RoutedWorkflow(spec=spec, primary_owner=owner, reviewers=reviewers, validation_issues=tuple(issues))


def classify_completion_criteria(spec: WorkflowSpec, request: WorkflowRequest) -> tuple[CompletionCriterion, ...]:
    criteria: list[CompletionCriterion] = [
        CompletionCriterion("scope and evidence traceability", CriterionStatus.REQUIRED, "Every workflow starts from explicit scope and evidence state."),
        CompletionCriterion("security and protected material handling", CriterionStatus.REQUIRED, "Sensitive architecture evidence is always protected."),
        CompletionCriterion("human approval boundaries", CriterionStatus.REQUIRED, "Formal approvals are outside agent authority."),
    ]
    domain_values = {domain.value for domain in request.domains}
    for domain in ArchitectureDomain:
        if domain in request.domains:
            criteria.append(CompletionCriterion(domain.value, CriterionStatus.CONDITIONALLY_REQUIRED, f"{domain.value} requested."))
        else:
            criteria.append(CompletionCriterion(domain.value, CriterionStatus.NOT_APPLICABLE, f"{domain.value} not in scope; requested: {sorted(domain_values)}."))
    if spec.name != "independent-architecture-assurance":
        criteria.append(CompletionCriterion("independent architecture review", CriterionStatus.REQUIRED, "Final review is required before formal use."))
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


async def run_workflow(request: WorkflowRequest, config: SecurityArchitectureConfig | None = None) -> Any:
    routed = route_workflow(request)
    if routed.validation_issues:
        return dry_run_workflow(request)
    configure_sdk(config)
    from agents import Runner
    from cybersecurity_security_architecture_agents.agents.coordinator import build_coordinator_agent

    coordinator = build_coordinator_agent(config)
    prompt = (
        f"Execute workflow {routed.spec.name}. Primary owner: {routed.primary_owner}. "
        f"Reviewers: {', '.join(routed.reviewers)}. Objective: {request.objective}. "
        "Do not approve architecture, accept risk, certify compliance, publish, deploy, configure live systems, operate production controls, activate integrations, import credentials, or fabricate evidence."
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

