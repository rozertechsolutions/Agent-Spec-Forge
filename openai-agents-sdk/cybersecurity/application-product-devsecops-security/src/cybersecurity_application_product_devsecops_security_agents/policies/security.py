from __future__ import annotations

PROHIBITED_ACTIONS: tuple[str, ...] = (
    "runtime execution",
    "build execution",
    "test execution",
    "scanner execution",
    "package installation",
    "pipeline activation",
    "deployment",
    "active probing",
    "release approval",
    "risk acceptance",
    "public disclosure",
)

REQUIRED_OUTPUT_FIELDS: tuple[str, ...] = (
    "reference",
    "title",
    "scope",
    "owner",
    "reviewer",
    "approver",
    "dates",
    "source provenance",
    "assumptions",
    "evidence",
    "assets",
    "status",
    "severity",
    "confidence",
    "limitations",
    "dependencies",
    "actions",
    "residual risk",
    "human decisions",
    "approval state",
    "completion criteria",
)
