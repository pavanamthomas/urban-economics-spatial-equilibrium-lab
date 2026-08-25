# Urban economics and spatial-equilibrium laboratory

A city-wide amenity that raises willingness to pay is not a gift to mobile residents. In a closed city, population is fixed: rents rise and *u\** rises. In an open city, *u\** is pinned by the outside option: in-migration bids up rents until the utility gain is capitalised into land. The commentator who says "rents rise and residents are better off in both models" has one true clause in the closed city and the wrong residual claimant in the open city.

This repository implements that split, then the objects that sit next to it in the assessment corpus: the Alonso–Muth–Mills envelope *R'(d) = −t/q*, Roback *(w, R)* cells, housing-supply incidence, place-based jobs versus stayers, Tiebout's conditions as a set, and a constructed hedonic omitted-variable. It is self-directed mechanism analysis. It is not a census, a zoning consultancy, or a place-based evaluation.

Dr. Pavanam Thomas · [pavanamthomas](https://github.com/pavanamthomas) · thomaspavanam@gmail.com
MIT License · Copyright 2026

The assessment corpus [economics-finance-assessment-benchmark-lab](https://github.com/pavanamthomas/economics-finance-assessment-benchmark-lab) keys this identity as `UE-H-01`. This laboratory is the balance of the two models. Related identification work lives in [econometrics-causal-inference-lab](https://github.com/pavanamthomas/econometrics-causal-inference-lab), which does not contain an open-city pin.

## The object, the miss, and the check

Amenity as virtual income, *A*: 0 → 0.2. *w* = 1, *N* closed = 1, *Hˢ* = 0.2 + 0.5 *R*.

| Rule | *R* | *u* | *N* | Rent bill |
| --- | ---: | ---: | ---: | ---: |
| Closed, *A* = 0 | 0.820 | −1.188 | 1 | 0.50 |
| Closed, *A* = 0.2 | 0.914 | −0.931 | 1 | 0.60 |
| Open, *A* = 0 | 0.820 | −1.188 | 1 | 0.50 |
| Open, *A* = 0.2 | 1.181 | −1.188 | 1.555 | 0.93 |

Closed: *dR* ≈ +0.094, *du* > 0. Open: *dR* ≈ +0.361, *du* = 0, population rises. Open *dR* exceeds closed *dR*.

`python examples/inspect_flagship.py` reprints the table. `FLAGSHIP_CASE_STUDY.md` is the write-up. `urbaneq.distractors` is the 10-option key.

## What would make that table wrong

- Treating the Cobb-Douglas housing *exponent* as the amenity. Then *u* can fall when *A* rises — a preference change, not quality of life. That calibration is in `FAILURES_AND_CORRECTIONS.md`.
- Perfectly elastic housing (*S1 → ∞*). Then closed *dR* shrinks and the open-city capitalisation has to work through quantity.
- An outside option that moves with the city's amenity. Then the open-city pin is not a pin.

## Layout

```
src/urbaneq/    bid-rent, open/closed city, Roback, incidence, place-based, Tiebout, hedonic OVB
tests/
examples/inspect_flagship.py
FLAGSHIP_CASE_STUDY.md
INTERVIEW_GUIDE.md
FAILURES_AND_CORRECTIONS.md
```

## Install and checks

Python 3.11+:

```bash
pip install -e ".[dev]"
pytest -q
python examples/inspect_flagship.py
```

## Integrity

Constructed cities. Not ACS, not a Saiz instrument, not a school-district hedonic. No planning job, no mayoral client, no identified treatment effect on a real place.
