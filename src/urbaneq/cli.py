"""Print the open/closed amenity table."""

from __future__ import annotations

from urbaneq.bidrent import mill_demo
from urbaneq.city import amenity_shock


def main() -> int:
    s = amenity_shock()
    print("Amenity as virtual income, A: 0 → 0.2. w=1, N_closed=1, H^s=0.2+0.5 R.")
    print()
    print("CLOSED (N fixed)")
    print(f"  R {s.closed_before.rent:.6f} → {s.closed_after.rent:.6f}   "
          f"dR={s.closed_after.rent - s.closed_before.rent:+.6f}")
    print(f"  u {s.closed_before.utility:.6f} → {s.closed_after.utility:.6f}   "
          f"du={s.closed_after.utility - s.closed_before.utility:+.6f}")
    print(f"  rent bill {s.closed_before.rent_bill:.4f} → {s.closed_after.rent_bill:.4f}")
    print()
    print("OPEN (u pinned at pre-shock closed u)")
    print(f"  R {s.open_before.rent:.6f} → {s.open_after.rent:.6f}   "
          f"dR={s.open_after.rent - s.open_before.rent:+.6f}")
    print(f"  u {s.open_before.utility:.6f} → {s.open_after.utility:.6f}   "
          f"du={s.open_after.utility - s.open_before.utility:+.6f}")
    print(f"  N {s.open_before.population:.6f} → {s.open_after.population:.6f}")
    print(f"  rent bill {s.open_before.rent_bill:.4f} → {s.open_after.rent_bill:.4f}")
    print()
    city = mill_demo()
    print(f"AMM envelope: t={city.commute_per_distance}, q={city.lot_size}, "
          f"R'(d)={city.slope:.4f}")
    print("Open dR exceeds closed dR. Open du is 0. The commentator's 'both' is false.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
