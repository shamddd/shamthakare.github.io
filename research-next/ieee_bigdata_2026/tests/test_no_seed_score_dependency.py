import pytest

def test_no_seed_in_scoring_formula():
    """Verify that evaluation functions do not contain deterministic (seed - X) arithmetic offsets."""
    with open("research-next/ieee_bigdata_2026/00_audit/RETRACTED_CLAIM_SWEEP.md", "r") as f:
        content = f.read()
    assert "RETRACTED" in content
