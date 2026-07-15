from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"
    NOT_RATED = "not-rated"


class WorkflowState(str, Enum):
    PLANNED = "planned"
    BLOCKED = "blocked"
    NEEDS_APPROVAL = "needs-approval"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class AppSecFinding:
    title: str
    scope: str
    assets: tuple[str, ...]
    evidence: tuple[str, ...]
    severity: Severity
    confidence: str
    actions: tuple[str, ...]
    residual_risk: str
    approval_state: str


@dataclass(frozen=True, slots=True)
class WorkflowResult:
    workflow: str
    state: WorkflowState
    owner: str
    reviewers: tuple[str, ...]
    findings: tuple[AppSecFinding, ...] = ()
    human_decisions: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()

    def independent_reviewers(self) -> tuple[str, ...]:
        return tuple(reviewer for reviewer in self.reviewers if reviewer != self.owner)
