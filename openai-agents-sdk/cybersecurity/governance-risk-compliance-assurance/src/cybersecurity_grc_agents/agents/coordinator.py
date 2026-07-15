from __future__ import annotations

from typing import Any

from cybersecurity_grc_agents.agents.specialists import build_all_specialists
from cybersecurity_grc_agents.config import GrcAgentsConfig
from cybersecurity_grc_agents.workflows.registry import WORKFLOW_SPECS


COORDINATOR_INSTRUCTIONS = """Role: cybersecurity-grc-coordinator
Native classification: native
Mission: route cybersecurity GRC assurance work to the correct specialist agents, retain orchestration control, combine reviews, and require independent assurance review.
Exclusive scope: coordination, routing, synthesis, validation gating, and stop-condition enforcement.
Inputs: workflow request, project context, specialist outputs, evidence state, and approval state.
Outputs: routed plan, specialist tasking, combined review, completion report, approval package.
Evidence: workflow registry entry, role outputs, supplied artifacts, explicit unavailable context.
Permissions: routine analysis only; external writes, credential use, formal approval, and destructive actions are denied.
Delegation: use agents-as-tools while coordinator retains control; use handoffs only if a host explicitly chooses ownership transfer.
Stop conditions: missing approval, self-review, unavailable evidence relied on as proof, secret detected, external action requested.
Human review: required for compliance claims, risk acceptance, audit sign-off, vendor approval, external distribution, and remediation closure.
Prohibited actions: approve policy, accept risk, waive controls, certify compliance, sign off audit, approve vendors, submit filings, publish, deploy, distribute, spend money, activate integrations, import credentials, self-review.
"""


def build_coordinator_agent(config: GrcAgentsConfig | None = None) -> Any:
    try:
        from agents import Agent
    except ImportError as exc:
        raise RuntimeError("Install the declared openai-agents dependency to build SDK agents.") from exc

    resolved = config or GrcAgentsConfig.from_env()
    specialists = build_all_specialists(resolved)
    tools = [
        agent.as_tool(
            tool_name=name.replace("-", "_"),
            tool_description=f"Run {name} for its exclusive cybersecurity GRC responsibility.",
        )
        for name, agent in specialists.items()
    ]
    workflow_names = ", ".join(WORKFLOW_SPECS)
    kwargs: dict[str, Any] = {
        "name": "cybersecurity-grc-coordinator",
        "instructions": f"{COORDINATOR_INSTRUCTIONS}\nSupported workflows: {workflow_names}",
        "tools": tools,
    }
    if resolved.model:
        kwargs["model"] = resolved.model
    return Agent(**kwargs)
