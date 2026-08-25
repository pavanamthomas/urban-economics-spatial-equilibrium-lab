"""Alonso–Muth–Mills envelope: R'(d) = −t / q(d).

Fixed lot size q makes the slope constant. Distant land is cheaper
because commuting eats the budget, not because the dirt is inferior.
If t = 0 the gradient is zero even if 'views' differ, which they
do not in this model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LinearCity:
    wage: float
    commute_per_distance: float
    lot_size: float
    agricultural_rent: float
    other_consumption: float = 0.0

    @property
    def slope(self) -> float:
        return -self.commute_per_distance / self.lot_size

    def bid_rent(self, d: float) -> float:
        leftover = self.wage - self.other_consumption - self.commute_per_distance * d
        return leftover / self.lot_size

    def edge(self) -> float:
        """Distance where R(d) = R_ag."""
        return (
            self.wage
            - self.other_consumption
            - self.agricultural_rent * self.lot_size
        ) / self.commute_per_distance


def mill_demo() -> LinearCity:
    """t = 0.1, q = 2 ⇒ R'(d) = −0.05."""
    return LinearCity(
        wage=10.0,
        commute_per_distance=0.1,
        lot_size=2.0,
        agricultural_rent=1.0,
        other_consumption=4.0,
    )
