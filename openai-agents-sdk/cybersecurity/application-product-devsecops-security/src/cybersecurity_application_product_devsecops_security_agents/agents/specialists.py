from __future__ import annotations

from .definitions import ROLE_SPECS, RoleSpec


def list_specialists() -> tuple[RoleSpec, ...]:
    return tuple(ROLE_SPECS.values())


def get_specialist(name: str) -> RoleSpec:
    return ROLE_SPECS[name]
