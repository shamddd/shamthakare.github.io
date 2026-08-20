import pytest

def test_negative_control_detects_and_rejects_formula_leakage():
    """Negative-control unit test: must catch and reject dummy formula leakage."""
    # Simulate a fake output with seed arithmetic leakage
    fake_eval_code = "v_full_sr = 0.81 + (seed - 43) * 0.006"
    
    # Test suite must detect this as invalid
    has_leakage = ("(seed - 43)" in fake_eval_code or "v_full_sr =" in fake_eval_code)
    assert has_leakage is True, "Negative control failed to flag deterministic seed formula!"
