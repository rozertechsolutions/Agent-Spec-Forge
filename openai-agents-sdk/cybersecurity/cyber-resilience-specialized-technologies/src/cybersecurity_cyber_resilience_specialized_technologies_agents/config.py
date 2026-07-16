from __future__ import annotations

SPECIALIZATION_ID = "cybersecurity.cyber-resilience-specialized-technologies"
STATIC_ONLY = True
EXTERNAL_INTEGRATIONS_ENABLED = False
TOOLS_ENABLED = False
PRODUCTION_ACTIONS_ENABLED = False
HUMAN_DECISIONS: tuple[str, ...] = (
    "business continuity",
    "safety decision",
    "legal position",
    "regulatory interpretation",
    "production action",
    "cryptographic change",
    "supplier decision",
    "investment",
    "residual risk acceptance",
    "critical closure",
)
