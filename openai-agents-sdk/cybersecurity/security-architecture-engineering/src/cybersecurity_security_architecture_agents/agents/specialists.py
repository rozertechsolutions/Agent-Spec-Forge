from __future__ import annotations

from typing import Any

from cybersecurity_security_architecture_agents.agents.definitions import ROLE_SPECS
from cybersecurity_security_architecture_agents.config import SecurityArchitectureConfig


def instructions_for_role(name: str) -> str:
    spec = ROLE_SPECS[name]
    return "\n".join(
        (
            f"Role: {spec.name}",
            f"Native classification: {spec.native_classification}",
            f"Mission: {spec.mission}",
            f"Exclusive scope: {spec.exclusive_scope}",
            "Inputs: " + ", ".join(spec.inputs),
            "Outputs: " + ", ".join(spec.outputs),
            "Stop conditions: " + ", ".join(spec.stop_conditions),
            "Human review: " + ", ".join(spec.human_review),
            "Prohibited actions: " + "; ".join(spec.prohibited_actions),
            "Return references, title, scope, owner, reviewer, approver, dates, source, assumptions, evidence, assets, status, severity, confidence, limitations, dependencies, actions, residual risk, human decisions, approval needs, and completion criteria.",
        )
    )


def build_specialist_agent(name: str, config: SecurityArchitectureConfig | None = None) -> Any:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("Install the declared openai-agents dependency to build SDK agents.") from exc

    resolved = config or SecurityArchitectureConfig.from_env()
    kwargs: dict[str, Any] = {
        "name": name,
        "instructions": instructions_for_role(name),
    }
    if resolved.model:
        kwargs["model"] = resolved.model
    return Agent(**kwargs)


def build_all_specialists(config: SecurityArchitectureConfig | None = None) -> dict[str, Any]:
    return {name: build_specialist_agent(name, config) for name in ROLE_SPECS}

