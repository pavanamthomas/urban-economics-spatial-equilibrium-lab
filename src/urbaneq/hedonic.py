"""Hedonic school-quality regression is not MWTP when amenities sort (UE-H-03).

Constructed: true willingness to pay for test scores is 0. Parks
have MWTP 1 and are correlated with scores. OLS of price on scores
is the park loading, not school quality.
"""

from __future__ import annotations

import numpy as np


def hedonic_ovb_demo(seed: int = 7) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    n = 400
    park = rng.normal(0.0, 1.0, n)
    scores = 0.8 * park + rng.normal(0.0, 0.4, n)
    # true: price = 1.0 * park + noise. Score coefficient is 0.
    price = 1.0 * park + rng.normal(0.0, 0.1, n)
    # OLS price on scores (no park control)
    x = np.column_stack([np.ones(n), scores])
    beta = np.linalg.lstsq(x, price, rcond=None)[0]
    x2 = np.column_stack([np.ones(n), scores, park])
    beta2 = np.linalg.lstsq(x2, price, rcond=None)[0]
    return {
        "ols_score_omitted_park": float(beta[1]),
        "ols_score_with_park": float(beta2[1]),
        "ols_park": float(beta2[2]),
    }
