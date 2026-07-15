from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import PurePath


class GrcDomain(str, Enum):
    GOVERNANCE_POLICY = "governance-policy"
    CYBER_RISK = "cyber-risk"
    ASSURANCE_EVIDENCE = "assurance-evidence"
    THIRD_PARTY_MATURITY = "third-party-maturity"
    INDEPENDENT_REVIEW = "independent-review"


class EvidenceState(str, Enum):
    SUPPLIED = "supplied"
    UNAVAILABLE = "unavailable"
    STALE = "stale"
    INFERRED = "inferred"
    NOT_APPLICABLE = "not-applicable"


@dataclass(frozen=True, slots=True)
class GrcProjectContext:
    project_root: PurePath
    domains: frozenset[GrcDomain]
    evidence_states: frozenset[EvidenceState] = field(default_factory=frozenset)
    constraints: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()

    def supports(self, domain: GrcDomain) -> bool:
        return domain in self.domains


@dataclass(frozen=True, slots=True)
class WorkflowRequest:
    workflow: str
    objective: str
    domains: frozenset[GrcDomain]
    project_context: GrcProjectContext
    human_approvals: frozenset[str] = field(default_factory=frozenset)
    cancellation_requested: bool = False

    def requires_domain(self, domain: GrcDomain) -> bool:
        return domain in self.domains
