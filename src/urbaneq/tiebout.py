"""Tiebout conditions as a set, not a slogan (UE-M-02)."""

from __future__ import annotations

TIEBOUT = frozenset(
    {
        "mobility",
        "many_jurisdictions",
        "no_spillovers",
        "no_scale_economies",
        "full_information",
    }
)


def tiebout_identified(conditions: frozenset[str]) -> bool:
    return TIEBOUT <= conditions
