from __future__ import annotations

from agents import Agent

from .guardrails import SAFETY_GUARDRAIL, SPECIALIST_GUARDRAIL


BASE_INSTRUCTIONS = (
    "You are a static Cybersecurity Area 08 agent. Use supplied evidence only. "
    "Separate evidence, fact, inference, hypothesis, recommendation, confidence, limitation, owner, "
    "approver, and independent reviewer. " + SAFETY_GUARDRAIL + " " + SPECIALIST_GUARDRAIL
)

resilience_recovery_core_agent = Agent(
    name="resilience-recovery-core",
    instructions=BASE_INSTRUCTIONS
    + " Own resilience strategy, dependency maps, disruption scenarios, backup/ransomware assessments, recovery readiness, exercise plans, and corrective actions.",
    tools=[],
)

specialized_technology_review_agent = Agent(
    name="specialized-technology-review",
    instructions=BASE_INSTRUCTIONS
    + " Own OT/ICS, IoT, embedded, AI/ML, hardware, firmware, cryptographic, critical-infrastructure, supplier, and lifecycle reviews.",
    tools=[],
)

assurance_transition_governance_agent = Agent(
    name="assurance-transition-governance",
    instructions=BASE_INSTRUCTIONS
    + " Own independent assurance, specialist escalation, metrics review, transition governance, and corrective-action quality review.",
    tools=[],
)
