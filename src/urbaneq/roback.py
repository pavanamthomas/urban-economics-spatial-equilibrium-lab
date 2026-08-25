"""Roback cells: wages *and* rents, not wages alone (UE-E-02).

Mobile workers, unit housing: u = w − R + a = ū.
Then w = ū + R − a.
"""

from __future__ import annotations

from dataclasses import dataclass

U_BAR = 1.0


@dataclass(frozen=True)
class RobackCity:
    name: str
    amenity: float
    rent: float
    kind: str

    @property
    def wage(self) -> float:
        return U_BAR + self.rent - self.amenity


def roback_atlas() -> dict[str, RobackCity]:
    return {
        "productivity": RobackCity("P", amenity=0.0, rent=1.0, kind="productivity"),
        "amenity": RobackCity("A", amenity=0.5, rent=1.0, kind="amenity"),
        "disamenity": RobackCity("D", amenity=-0.4, rent=0.3, kind="disamenity"),
    }


def ranked_by_wage(atlas: dict[str, RobackCity] | None = None) -> list[str]:
    atlas = atlas or roback_atlas()
    return [c.kind for c in sorted(atlas.values(), key=lambda c: c.wage, reverse=True)]
