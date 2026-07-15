from __future__ import annotations

from typing import Any

from cybersecurity_grc_agents.agents.definitions import ROLE_SPECS
from cybersecurity_grc_agents.config import GrcAgentsConfig


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
            "Return evidence status, assumptions, approval requirements, blockers, and limitations. Do not fabricate evidence or approve formal claims.",
        )
    )


def build_specialist_agent(name: str, config: GrcAgentsConfig | None = None) -> Any:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("Install the declared openai-agents dependency to build SDK agents.") from exc

    resolved = config or GrcAgentsConfig.from_env()
    kwargs: dict[str, Any] = {
        "name": name,
        "instructions": instructions_for_role(name),
    }
    if resolved.model:
        kwargs["model"] = resolved.model
    return Agent(**kwargs)


def build_all_specialists(config: GrcAgentsConfig | None = None) -> dict[str, Any]:
    return {name: build_specialist_agent(name, config) for name in ROLE_SPECS}
