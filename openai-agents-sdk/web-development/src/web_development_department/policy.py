"""Static safety policy. This module performs no external actions."""

from __future__ import annotations

SENSITIVE_ACTIONS = frozenset({
    "authentication", "authorization", "secret_access", "sensitive_data",
    "database_migration", "dependency_change", "third_party_script",
    "tracking", "production_change", "deployment", "publication",
    "billing", "signing", "submission", "git_mutation", "destructive_action",
})

PROHIBITED_AUTOMATIC_ACTIONS = frozenset({
    "execute_command", "install_dependency", "git_mutation", "deploy",
    "publish", "authenticate", "expose_secret", "spend", "sign", "submit",
    "destructive_action",
})


def requires_human_approval(action: str) -> bool:
    """Return True when an action must pause for explicit human approval."""
    return action.strip().lower() in SENSITIVE_ACTIONS or action.strip().lower() in PROHIBITED_AUTOMATIC_ACTIONS
