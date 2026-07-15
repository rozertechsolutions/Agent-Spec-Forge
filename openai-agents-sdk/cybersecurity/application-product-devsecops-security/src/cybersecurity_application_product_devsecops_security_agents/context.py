from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AppSecContext:
    scope: str
    owner: str
    reviewer: str
    approver: str
    source_provenance: tuple[str, ...]
    assumptions: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()

    def approval_required(self) -> bool:
        return bool(self.approver.strip())
