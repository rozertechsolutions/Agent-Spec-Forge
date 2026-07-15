from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WorkflowSpec:
    name: str
    owner: str
    reviewers: tuple[str, ...]
    steps: tuple[str, ...]
    prohibited_actions: tuple[str, ...]


WORKFLOWS: dict[str, WorkflowSpec] = {
    "secure-sdlc-governance": WorkflowSpec(
        name="secure-sdlc-governance",
        owner="product-security-governance-agent",
        reviewers=("independent-appsec-reviewer",),
        steps=("confirm scope", "map lifecycle controls", "draft gates", "list human decisions", "review independently"),
        prohibited_actions=("approve policy", "approve release", "accept risk"),
    ),
    "requirements-threat-modeling": WorkflowSpec(
        name="requirements-threat-modeling",
        owner="requirements-threat-modeling-agent",
        reviewers=("independent-appsec-reviewer",),
        steps=("confirm assets", "map trust boundaries", "identify abuse cases", "define mitigations", "review independently"),
        prohibited_actions=("probe systems", "create exploit", "approve design"),
    ),
    "secure-design-code-review": WorkflowSpec(
        name="secure-design-code-review",
        owner="secure-design-code-review-agent",
        reviewers=("independent-appsec-reviewer",),
        steps=("confirm artifacts", "review controls", "document findings", "define validation", "review independently"),
        prohibited_actions=("run code", "run test", "close finding"),
    ),
    "supply-chain-ci-release": WorkflowSpec(
        name="supply-chain-ci-release",
        owner="supply-chain-ci-release-agent",
        reviewers=("independent-appsec-reviewer",),
        steps=("inventory files", "review dependency evidence", "review build controls", "define blockers", "review independently"),
        prohibited_actions=("install dependency", "run build", "run pipeline", "deploy"),
    ),
    "testing-findings-psirt": WorkflowSpec(
        name="testing-findings-psirt",
        owner="testing-findings-psirt-agent",
        reviewers=("independent-appsec-reviewer",),
        steps=("confirm testing scope", "triage findings", "define validation", "draft PSIRT package", "review independently"),
        prohibited_actions=("run test", "disclose issue", "command incident", "close finding"),
    ),
}
