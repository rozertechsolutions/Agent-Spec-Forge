from __future__ import annotations

from .agents.coordinator import COORDINATOR_NAME
from .config import SPECIALIZATION_ID, STATIC_ONLY


def describe_specialization() -> dict[str, str | bool]:
    return {
        "id": SPECIALIZATION_ID,
        "coordinator": COORDINATOR_NAME,
        "static_only": STATIC_ONLY,
        "status": "source-only",
    }
