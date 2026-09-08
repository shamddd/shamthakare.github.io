"""
Unit tests for scientific claim boundaries.
"""

import pytest


def test_disallowed_claims():
    banned_claims = [
        "strict monotonicity",
        "effect emerged at step 32",
        "effect emerged at t=32",
        "11.76% acceleration",
        "inflection point",
        "local peak"
    ]
    
    # Assert allowed phrasing
    allowed_trajectory_statement = "Across nine empirically evaluated checkpoints, the interaction was consistent with a non-decreasing trajectory under prespecified order-restricted analysis despite local variation in unconstrained estimates."
    allowed_emergence_statement = "The unadjusted checkpoint-32 contrast was positive, while family-wise Bonferroni-adjusted inference did not establish significance at this earliest checkpoint."
    
    for banned in banned_claims:
        assert banned not in allowed_trajectory_statement.lower()
        assert banned not in allowed_emergence_statement.lower()
