"""Explicit entry point. Running it requires the caller to configure SDK authentication."""

from __future__ import annotations

from agents import Runner

from .department import web_development_lead


async def run_web_development_request(request: str):
    """Run a text-only department workflow with no configured tools."""
    if not request.strip():
        raise ValueError("request must not be empty")
    return await Runner.run(web_development_lead, request)
