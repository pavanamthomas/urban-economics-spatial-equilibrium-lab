# Failures and corrections

## 1. Housing exponent treated as the amenity

**What failed.** A first calibration used *u = log(x) + a log(h)* and moved *a* from 1 to 1.2 as "cleaner air." Closed-city utility *fell*. Open-city rents *fell*. That is a preference-weight change, not quality of life.

**How it was detected.** `amenity_shock` printed *du < 0* in the closed city, which contradicts the item key.

**Repair.** Amenity as virtual income *y = w + χA*. Closed *du > 0*, closed *dR > 0*, open *du = 0*, open *dR* larger.

**Regression.** `test_closed_amenity_raises_rent_and_utility`, `test_open_amenity_capitalises_into_rent_not_utility`.

## 2. Closed-city rents claimed impossible because *N* is fixed

**What failed.** A distractor leaked into a derivation: "population fixed ⇒ housing demand fixed ⇒ *R* fixed."

**How it was detected.** Virtual income raises *h(R, y)*. The quadratic for *R* moves. Rent bill 0.50 → 0.60 is *Ny/2*, not a numerical accident.

**Repair.** `test_closed_amenity_raises_rent_and_utility` and the rent-bill pin.

**Regression.** Same.

## 3. Wage ranking treated as a productivity ranking

**What failed.** Sorting the Roback atlas by *w* put the disamenity city above the amenity city and called that "productivity."

**How it was detected.** `ranked_by_wage` returns `[productivity, disamenity, amenity]`. The productivity *cell* is high *w* and high *R* together (`UE-E-02`).

**Repair.** Keep the wage sort as a negative control.

**Regression.** `test_roback_cells_are_not_a_wage_ranking`.
