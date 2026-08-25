from __future__ import annotations

import pytest

from urbaneq.bidrent import mill_demo
from urbaneq.hedonic import hedonic_ovb_demo
from urbaneq.incidence import saiz_pair
from urbaneq.place import place_demo
from urbaneq.roback import ranked_by_wage, roback_atlas
from urbaneq.tiebout import TIEBOUT, tiebout_identified


def test_bid_rent_slope_is_minus_t_over_q() -> None:
    city = mill_demo()
    assert city.slope == pytest.approx(-0.05)
    # Envelope check: finite difference of bid_rent.
    d0, d1 = 1.0, 1.001
    num = (city.bid_rent(d1) - city.bid_rent(d0)) / (d1 - d0)
    assert num == pytest.approx(city.slope, abs=1e-8)
    from urbaneq.bidrent import LinearCity

    z = LinearCity(
        wage=city.wage,
        commute_per_distance=0.0,
        lot_size=city.lot_size,
        agricultural_rent=city.agricultural_rent,
        other_consumption=city.other_consumption,
    )
    assert z.slope == 0.0


def test_roback_cells_are_not_a_wage_ranking() -> None:
    atlas = roback_atlas()
    assert atlas["productivity"].wage > atlas["amenity"].wage
    assert atlas["disamenity"].wage > atlas["amenity"].wage
    assert atlas["productivity"].rent > atlas["disamenity"].rent
    assert atlas["amenity"].rent == atlas["productivity"].rent
    assert ranked_by_wage(atlas) == ["productivity", "disamenity", "amenity"]


def test_inelastic_supply_puts_the_shift_on_price() -> None:
    inelastic, elastic = saiz_pair()
    assert inelastic.dln_price == pytest.approx(0.10)
    assert inelastic.dln_quantity == pytest.approx(0.0)
    assert abs(elastic.dln_price) < 1e-6
    assert elastic.dln_quantity == pytest.approx(0.10, abs=1e-5)


def test_place_based_jobs_are_not_stayer_jobs() -> None:
    p = place_demo()
    assert p.place_employment_change == 10
    assert p.stayer_employment_change == 4
    assert p.land_rent_after > p.land_rent_before


def test_tiebout_refuses_a_slogan() -> None:
    assert not tiebout_identified(frozenset({"mobility"}))
    assert tiebout_identified(TIEBOUT)


def test_hedonic_score_coefficient_is_ovb_without_the_park() -> None:
    row = hedonic_ovb_demo()
    assert row["ols_score_omitted_park"] > 0.4
    assert abs(row["ols_score_with_park"]) < 0.05
    assert row["ols_park"] == pytest.approx(1.0, abs=0.05)
