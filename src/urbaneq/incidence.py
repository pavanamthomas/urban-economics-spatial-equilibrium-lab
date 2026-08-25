"""Housing-demand shock incidence (UE-H-02, UE-E-03).

Log-linear: d ln Q^d = d ln D − e_d d ln P, d ln Q^s = e_s d ln P.
Clearing: d ln P = d ln D / (e_s + e_d), d ln Q = e_s d ln P.

Inelastic supply (e_s = 0): the whole shift is price. Perfectly
elastic: the whole shift is quantity. An urban wage premium is not
a worker surplus when housing is inelastic: landowners collect.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Incidence:
    e_s: float
    e_d: float
    dln_demand: float

    @property
    def dln_price(self) -> float:
        return self.dln_demand / (self.e_s + self.e_d)

    @property
    def dln_quantity(self) -> float:
        return self.e_s * self.dln_price


def saiz_pair() -> tuple[Incidence, Incidence]:
    shift = 0.10
    inelastic = Incidence(e_s=0.0, e_d=1.0, dln_demand=shift)
    elastic = Incidence(e_s=1e6, e_d=1.0, dln_demand=shift)
    return inelastic, elastic
