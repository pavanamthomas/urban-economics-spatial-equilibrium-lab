from __future__ import annotations

import pytest

from urbaneq.city import amenity_shock


def test_closed_amenity_raises_rent_and_utility() -> None:
    s = amenity_shock()
    assert s.closed_after.rent > s.closed_before.rent
    assert s.closed_after.utility > s.closed_before.utility
    assert s.closed_after.population == s.closed_before.population
    assert s.closed_before.rent_bill == pytest.approx(0.5)
    assert s.closed_after.rent_bill == pytest.approx(0.6)


def test_open_amenity_capitalises_into_rent_not_utility() -> None:
    s = amenity_shock()
    assert s.open_after.rent > s.open_before.rent
    assert s.open_after.utility == pytest.approx(s.open_before.utility, abs=1e-12)
    assert s.open_after.population > s.open_before.population


def test_open_rent_increase_exceeds_closed() -> None:
    s = amenity_shock()
    d_open = s.open_after.rent - s.open_before.rent
    d_closed = s.closed_after.rent - s.closed_before.rent
    assert d_open > d_closed > 0
    assert d_open == pytest.approx(0.3607, abs=5e-4)
    assert d_closed == pytest.approx(0.0937, abs=5e-4)


def test_open_and_closed_start_at_the_same_point() -> None:
    s = amenity_shock()
    assert s.open_before.rent == pytest.approx(s.closed_before.rent)
    assert s.open_before.population == pytest.approx(1.0)
