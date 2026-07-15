from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
import re


SECRET_PATTERNS = (
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY"),
    re.compile(
        r"\b("
        + "|".join(("api[_-]?" + "key", "pass" + "word", "tok" + "en", "sec" + "ret"))
        + r")\b\s*[:=]",
        re.IGNORECASE,
    ),
)

PROHIBITED_ACTIONS = (
    "accept risk",
    "waive control",
    "certify compliance",
    "approve architecture",
    "publish",
    "deploy",
    "configure live",
    "operate production",
)


@dataclass(frozen=True, slots=True)
class SecurityFinding:
    message: str
    blocked: bool


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def validate_user_text(text: str) -> tuple[SecurityFinding, ...]:
    findings: list[SecurityFinding] = []
    lowered = text.lower()
    if contains_secret(text):
        findings.append(SecurityFinding("Input appears to contain protected material.", True))
    for action in PROHIBITED_ACTIONS:
        if action in lowered:
            findings.append(SecurityFinding(f"Action requires human authority: {action}.", True))
    return tuple(findings)


def validate_relative_project_path(path: str) -> tuple[SecurityFinding, ...]:
    parsed = PurePosixPath(path)
    findings: list[SecurityFinding] = []
    if parsed.is_absolute() or ".." in parsed.parts:
        findings.append(SecurityFinding("Path must stay inside the reviewed project root.", True))
    if parsed.name in {".env", "credentials.json"} or parsed.suffix in {".pem", ".key"}:
        findings.append(SecurityFinding("Path appears to target protected credential material.", True))
    return tuple(findings)

