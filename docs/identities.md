# Identities used as tests

| Object | Statement | Test |
| --- | --- | --- |
| Closed amenity | *dR > 0*, *du > 0*, rent bill 0.50 → 0.60 | `test_closed_amenity_raises_rent_and_utility` |
| Open amenity | *du = 0*, *dN > 0*, *dR > 0* | `test_open_amenity_capitalises_into_rent_not_utility` |
| Comparison | open *dR* > closed *dR* ≈ 0.094 vs 0.361 | `test_open_rent_increase_exceeds_closed` |
| Bid-rent | *R'(d) = −t/q = −0.05*; *t=0* ⇒ 0 | `test_bid_rent_slope_is_minus_t_over_q` |
| Roback | wage ranking ≠ productivity ranking | `test_roback_cells_are_not_a_wage_ranking` |
| Incidence | *e_s=0* ⇒ *d ln P = d ln D* | `test_inelastic_supply_puts_the_shift_on_price` |
| Place-based | +10 jobs ≠ +4 stayers | `test_place_based_jobs_are_not_stayer_jobs` |
| Tiebout | mobility alone is not the theorem | `test_tiebout_refuses_a_slogan` |
| Hedonic | score OLS is park OVB | `test_hedonic_score_coefficient_is_ovb_without_the_park` |
| Distractors | A–J, one `CORRECT_KEY` | `test_distractors_are_ten_letters_one_key` |
