from __future__ import annotations

from cybersecurity_grc_agents.policies.security import validate_relative_project_path, validate_user_text


def validate_user_input(text: str) -> tuple[str, ...]:
    return tuple(finding.message for finding in validate_user_text(text) if finding.blocked)


def validate_requested_path(path: str) -> tuple[str, ...]:
    return tuple(finding.message for finding in validate_relative_project_path(path) if finding.blocked)
