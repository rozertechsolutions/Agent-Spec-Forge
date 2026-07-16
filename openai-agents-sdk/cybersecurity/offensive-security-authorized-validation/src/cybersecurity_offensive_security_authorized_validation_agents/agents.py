from __future__ import annotations

from agents import Agent

from .guardrails import AUTHORIZATION_GUARDRAIL, SAFETY_GUARDRAIL


BASE_INSTRUCTIONS = (
    "You are a static Cybersecurity Area 07 agent. Use supplied evidence only. "
    "Separate evidence, fact, inference, hypothesis, severity, business priority, confidence, limitation, owner, "
    "approver, and independent reviewer. " + SAFETY_GUARDRAIL + " " + AUTHORIZATION_GUARDRAIL
)

authorization_assessment_planning_agent = Agent(
    name="authorization-assessment-planning",
    instructions=BASE_INSTRUCTIONS
    + " Own authorization checklists, rules of engagement, safe assessment plans, target boundaries, and safety gates.",
    tools=[],
)

emulation_purple_safety_agent = Agent(
    name="emulation-purple-safety",
    instructions=BASE_INSTRUCTIONS
    + " Own emulation, red-team, purple-team, social-governance, simulation-boundary, and control-validation planning.",
    tools=[],
)

findings_retest_assurance_agent = Agent(
    name="findings-retest-assurance",
    instructions=BASE_INSTRUCTIONS
    + " Own findings, evidence manifests, cleanup plans, retest plans, validation records, reports, and assurance.",
    tools=[],
)
