"""Place-based jobs versus stayers (UE-E-01).

Ten jobs appear. Six are filled by in-migrants, four by incumbents.
The place's employment rises by 10. Incumbent employment rises by 4.
Capitalisation into land is a third object: it can be positive even
if stayer wages do not move.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlaceProgram:
    incumbents: int
    new_jobs: int
    filled_by_migrants: int
    land_rent_before: float
    land_rent_after: float

    @property
    def filled_by_incumbents(self) -> int:
        return self.new_jobs - self.filled_by_migrants

    @property
    def place_employment_change(self) -> int:
        return self.new_jobs

    @property
    def stayer_employment_change(self) -> int:
        return self.filled_by_incumbents


def place_demo() -> PlaceProgram:
    return PlaceProgram(
        incumbents=100,
        new_jobs=10,
        filled_by_migrants=6,
        land_rent_before=1.0,
        land_rent_after=1.15,
    )
