from __future__ import annotations

from dataclasses import dataclass


BLOCKED_ACTIONS: tuple[str, ...] = (
    "run build",
    "run test",
    "run scanner",
    "install package",
    "deploy",
    "approve release",
    "accept risk",
    "disclose issue",
    "close finding",
)


@dataclass(frozen=True, slots=True)
class GuardrailDecision:
    allowed: bool
    reason: str


def evaluate_request(request_text: str) -> GuardrailDecision:
    normalized = request_text.lower()
    for phrase in BLOCKED_ACTIONS:
        if phrase in normalized:
            return GuardrailDecision(False, f"Blocked static-only boundary: {phrase}")
    return GuardrailDecision(True, "Request remains within advisory static review boundaries.")
