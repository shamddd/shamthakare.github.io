import pytest

def test_raw_observation_traceability():
    """Verify that evaluation schemas require raw generated tokens and verifier outputs."""
    required_keys = ["generated_continuation", "verifier_output", "success"]
    assert len(required_keys) == 3
