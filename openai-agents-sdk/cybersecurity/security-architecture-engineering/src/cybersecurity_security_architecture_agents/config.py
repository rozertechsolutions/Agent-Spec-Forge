from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True, slots=True)
class SecurityArchitectureConfig:
    """Runtime configuration that does not require API access during import."""

    model: str | None
    tracing_disabled: bool

    @classmethod
    def from_env(cls) -> "SecurityArchitectureConfig":
        disabled = os.getenv("OPENAI_AGENTS_DISABLE_TRACING", "1").strip().lower()
        return cls(
            model=os.getenv("OPENAI_AGENTS_MODEL") or None,
            tracing_disabled=disabled in {"1", "true", "yes", "on"},
        )

