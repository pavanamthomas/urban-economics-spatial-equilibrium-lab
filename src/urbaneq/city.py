"""Closed versus open city after an amenity shock (UE-H-01).

Amenity A is virtual income: full income y = w + χA, Cobb-Douglas
u = log(x) + log(h) so h = y/(2R). Housing supply H^s = S0 + S1 R,
S1 > 0.

Closed: N fixed, R and u* endogenous. Amenity raises both R and u*.
Open: u* pinned at the pre-shock closed utility. Amenity raises R
by more, raises N, and leaves u* unchanged. Landowners take the
rent bill. 'Rents rise and residents are better off in both models'
is false.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

W = 1.0
N_CLOSED = 1.0
S0 = 0.2
S1 = 0.5
CHI = 1.0
A0 = 0.0
A1 = 0.2


def housing_demand(R: float, w: float, amenity: float, chi: float = CHI) -> float:
    return (w + chi * amenity) / (2.0 * R)


def housing_supply(R: float, s0: float = S0, s1: float = S1) -> float:
    return s0 + s1 * R


def utility(R: float, w: float, amenity: float, chi: float = CHI) -> float:
    y = w + chi * amenity
    h = y / (2.0 * R)
    x = y / 2.0
    return math.log(x) + math.log(h)


def closed_rent(N: float, w: float, amenity: float, s0: float = S0, s1: float = S1, chi: float = CHI) -> float:
    y = w + chi * amenity
    k = N * y / 2.0
    disc = s0**2 + 4.0 * s1 * k
    return (-s0 + math.sqrt(disc)) / (2.0 * s1)


def open_rent(w: float, amenity: float, u_bar: float, chi: float = CHI) -> float:
    y = w + chi * amenity
    return math.exp(2.0 * math.log(y / 2.0) - u_bar)


def rent_bill(R: float, s0: float = S0, s1: float = S1) -> float:
    return R * housing_supply(R, s0, s1)


def population(R: float, w: float, amenity: float, s0: float = S0, s1: float = S1, chi: float = CHI) -> float:
    return housing_supply(R, s0, s1) / housing_demand(R, w, amenity, chi)


@dataclass(frozen=True)
class CitySnapshot:
    amenity: float
    rent: float
    utility: float
    population: float
    rent_bill: float


@dataclass(frozen=True)
class AmenityShock:
    closed_before: CitySnapshot
    closed_after: CitySnapshot
    open_before: CitySnapshot
    open_after: CitySnapshot


def _snap(R: float, amenity: float, N: float) -> CitySnapshot:
    return CitySnapshot(
        amenity=amenity,
        rent=R,
        utility=utility(R, W, amenity),
        population=N,
        rent_bill=rent_bill(R),
    )


def amenity_shock() -> AmenityShock:
    r_c0 = closed_rent(N_CLOSED, W, A0)
    r_c1 = closed_rent(N_CLOSED, W, A1)
    u_bar = utility(r_c0, W, A0)
    r_o0 = open_rent(W, A0, u_bar)
    r_o1 = open_rent(W, A1, u_bar)
    return AmenityShock(
        closed_before=_snap(r_c0, A0, N_CLOSED),
        closed_after=_snap(r_c1, A1, N_CLOSED),
        open_before=_snap(r_o0, A0, population(r_o0, W, A0)),
        open_after=_snap(r_o1, A1, population(r_o1, W, A1)),
    )
