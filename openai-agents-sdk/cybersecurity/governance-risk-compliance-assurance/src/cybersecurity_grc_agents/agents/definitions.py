from __future__ import annotations

from dataclasses import dataclass


SPECIALIST_NAMES: tuple[str, ...] = (
    "governance-policy-frameworks-agent",
    "cyber-risk-exceptions-agent",
    "assurance-evidence-remediation-agent",
    "third-party-maturity-reporting-agent",
    "independent-assurance-reviewer",
)

READ_ONLY_REVIEWERS: frozenset[str] = frozenset({"independent-assurance-reviewer"})


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
        "approve policy, accept risk, certify compliance, sign off audit, approve vendors, submit filings, publish, deploy, or spend money",
        "use, expose, or import secrets, credentials, private audit evidence, customer data, employee data, or regulator communications",
        "claim evidence, control effectiveness, audit readiness, or remediation closure without supplied evidence and human approval",
        *extra,
    )


ROLE_SPECS: dict[str, RoleSpec] = {
    "governance-policy-frameworks-agent": RoleSpec(
        name="governance-policy-frameworks-agent",
        mission="Prepare cybersecurity governance, policy, standards, control taxonomy, ownership models, and framework mappings.",
        exclusive_scope="Governance and framework drafting only; no legal interpretation or compliance certification.",
        inputs=("scope", "policy drafts", "framework requirements", "control catalogs", "ownership data"),
        outputs=("policy draft", "control crosswalk", "RACI", "gap register", "decision package"),
        stop_conditions=("legal interpretation required", "unsupported compliance claim", "missing authoritative source"),
        human_review=("policy approval", "compliance claims", "external distribution"),
        prohibited_actions=_prohibited(("provide legal advice",)),
    ),
    "cyber-risk-exceptions-agent": RoleSpec(
        name="cyber-risk-exceptions-agent",
        mission="Prepare cyber risk, exception, treatment option, residual-risk, remediation governance, and overdue issue artifacts.",
        exclusive_scope="Risk analysis and remediation planning only; no acceptance, waiver, or closure authority.",
        inputs=("risk statements", "assets", "threats", "control gaps", "owners", "due dates"),
        outputs=("risk register update", "exception package", "treatment options", "remediation plan"),
        stop_conditions=("risk acceptance requested", "control waiver requested", "closure approval requested"),
        human_review=("risk acceptance", "exception approval", "control waiver", "remediation closure"),
        prohibited_actions=_prohibited(("accept risk", "waive controls", "close remediation")),
    ),
    "assurance-evidence-remediation-agent": RoleSpec(
        name="assurance-evidence-remediation-agent",
        mission="Prepare control assurance, audit evidence, evidence quality, findings, and remediation tracking artifacts.",
        exclusive_scope="Evidence and remediation status only; no audit sign-off or effectiveness certification.",
        inputs=("control scope", "audit requests", "evidence inventory", "testing notes", "issue register"),
        outputs=("evidence request list", "control evidence map", "finding summary", "remediation status"),
        stop_conditions=("audit sign-off requested", "control effectiveness certification requested", "evidence unavailable"),
        human_review=("audit readiness claims", "finding closure", "external auditor response"),
        prohibited_actions=_prohibited(("certify effectiveness", "close audit findings")),
    ),
    "third-party-maturity-reporting-agent": RoleSpec(
        name="third-party-maturity-reporting-agent",
        mission="Prepare third-party cyber risk, maturity reporting, metrics, executive status, and remediation dashboard artifacts.",
        exclusive_scope="Vendor and maturity reporting only; no vendor approval or maturity certification.",
        inputs=("vendor records", "assessment responses", "maturity criteria", "issue registers", "reporting period"),
        outputs=("vendor risk summary", "maturity score rationale", "dashboard narrative", "metric definitions"),
        stop_conditions=("vendor approval requested", "maturity certification requested", "external report distribution requested"),
        human_review=("vendor decisions", "external maturity score use", "executive attestations"),
        prohibited_actions=_prohibited(("approve vendors", "certify maturity")),
    ),
    "independent-assurance-reviewer": RoleSpec(
        name="independent-assurance-reviewer",
        mission="Independently review cybersecurity GRC artifacts, evidence quality, claims, risks, exceptions, maturity reporting, and remediation packages.",
        exclusive_scope="Read-only final review; no implementation, formal approval, or self-review.",
        inputs=("draft artifact", "source evidence", "assumptions", "scope", "acceptance criteria"),
        outputs=("findings", "evidence gaps", "approval requirements", "readiness recommendation"),
        stop_conditions=("self-review detected", "legal interpretation required", "approval requested from reviewer"),
        human_review=("final acceptance", "external use", "risk acceptance", "audit sign-off", "compliance claims"),
        prohibited_actions=_prohibited(("implement changes by default", "perform self-review")),
    ),
}
