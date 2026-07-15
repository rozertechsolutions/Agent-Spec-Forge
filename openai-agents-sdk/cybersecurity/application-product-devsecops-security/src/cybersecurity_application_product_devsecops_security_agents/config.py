from __future__ import annotations

SPECIALIZATION_ID = "cybersecurity.application-product-devsecops-security"
STATIC_ONLY = True
EXTERNAL_INTEGRATIONS_ENABLED = False

HUMAN_DECISIONS: tuple[str, ...] = (
    "release approval",
    "deployment approval",
    "exception approval",
    "risk acceptance",
    "public disclosure",
    "finding closure",
)
