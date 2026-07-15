from __future__ import annotations

from typing import Any

from cybersecurity_security_architecture_agents.agents.specialists import build_all_specialists
from cybersecurity_security_architecture_agents.config import SecurityArchitectureConfig
from cybersecurity_security_architecture_agents.workflows.registry import WORKFLOW_SPECS


COORDINATOR_INSTRUCTIONS = """Role: security-architecture-coordinator
Native classification: native
Mission: route cybersecurity security architecture and engineering work to the correct specialist agents, retain orchestration control, combine reviews, and require independent architecture review.
Exclusive scope: coordination, routing, synthesis, validation gating, and stop-condition enforcement.
Inputs: workflow request, project context, specialist outputs, evidence state, and approval state.
Outputs: routed plan, specialist tasking, combined review, completion report, approval package.
Evidence: workflow registry entry, role outputs, supplied artifacts, explicit unavailable context.
Permissions: routine analysis only; external writes, credential use, formal approval, deployment, and destructive actions are denied.
Delegation: use agents-as-tools while coordinator retains control; use handoffs only if a host explicitly chooses ownership transfer.
Stop conditions: missing approval, self-review, unavailable evidence relied on as proof, secret detected, external action requested.
Human review: required for architecture approval, production use, risk acceptance, external distribution, environment changes, and control activation.
Prohibited actions: approve architecture, accept risk, waive controls, certify compliance, publish, deploy, configure live systems, operate production controls, activate integrations, import credentials, perform incident command, conduct forensics, run offensive testing, or self-review.
"""


def build_coordinator_agent(config: SecurityArchitectureConfig | None = None) -> Any:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("Install the declared openai-agents dependency to build SDK agents.") from exc

    resolved = config or SecurityArchitectureConfig.from_env()
    specialists = build_all_specialists(resolved)
    tools = [
        agent.as_tool(
            tool_name=name.replace("-", "_"),
            tool_description=f"Run {name} for its exclusive security architecture responsibility.",
        )
        for name, agent in specialists.items()
    ]
    workflow_names = ", ".join(WORKFLOW_SPECS)
    kwargs: dict[str, Any] = {
        "name": "security-architecture-coordinator",
        "instructions": f"{COORDINATOR_INSTRUCTIONS}\nSupported workflows: {workflow_names}",
        "tools": tools,
    }
    if resolved.model:
        kwargs["model"] = resolved.model
    return Agent(**kwargs)

