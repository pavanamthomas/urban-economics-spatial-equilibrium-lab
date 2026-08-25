# Flagship case: amenity shock, two residual claimants

## The city

Spaceless housing market. Full income *y = w + χA* with *χ* = 1, *w* = 1. Cobb-Douglas *u = log(x) + log(h)* ⇒ *h = y/(2R)*. Supply *Hˢ = 0.2 + 0.5 R*. Closed city: *N* = 1. Open city: *u* pinned at the pre-shock closed utility.

Amenity *A*: 0 → 0.2. That is virtual income, not a change in the housing exponent.

## What the code returns

```
CLOSED (N fixed)
  R 0.819804 → 0.913553   dR=+0.093749
  u -1.187604 → -0.931237   du=+0.256367
  rent bill 0.5000 → 0.6000

OPEN (u pinned at pre-shock closed u)
  R 0.819804 → 1.180518   dR=+0.360714
  u -1.187604 → -1.187604   du=+0.000000
  N 1.000000 → 1.554857
  rent bill 0.5000 → 0.9329
```

Closed: incumbents are better off; rents rise with their WTP; rent bill = *Ny/2*, so 0.50 → 0.60 exactly. Open: mobile residents are not better off; population rises; landowners' rent bill rises by more than the closed increment.

A commentator who says "rents rise and residents are better off" in both models has described the closed city and then applied it to the open city.

## Independent check

Open-city equilibrium is *u(R, A, w) = ū*. *dA > 0* with *ū* fixed requires *dR > 0* to hold the equality. Closed city has no such equality. The rent-bill identity *R Hˢ = Ny/2* is independent of solving the quadratic for *R*.

## Envelope sitting next to the table

*t* = 0.1, *q* = 2 ⇒ *R'(d) = −0.05*. Finite difference of `bid_rent` agrees. *t* = 0 ⇒ slope 0. Distant land is cheaper because commuting eats the budget (`UE-M-01`).

## Assessment implication

If the stem does not name open versus closed, "residents are better off" and "landowners capture the amenity" are both defensible. `UE-H-01` names both models. Owner-occupiers mix the two residual claimants; that is a distractor, not a second key.
