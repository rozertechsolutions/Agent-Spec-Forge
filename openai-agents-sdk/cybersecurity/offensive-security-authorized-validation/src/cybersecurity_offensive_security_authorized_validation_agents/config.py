from __future__ import annotations

SPECIALIZATION_ID = "cybersecurity.offensive-security-authorized-validation"
STATIC_ONLY = True
EXTERNAL_INTEGRATIONS_ENABLED = False
TOOLS_ENABLED = False
ACTIVE_TESTING_ENABLED = False
HUMAN_DECISIONS: tuple[str, ...] = (
    "authorization",
    "scope change",
    "high impact method",
    "legal position",
    "privacy position",
    "social governance approval",
    "publication",
    "risk acceptance",
    "cleanup confirmation",
    "retest closure",
    "critical finding closure",
)
