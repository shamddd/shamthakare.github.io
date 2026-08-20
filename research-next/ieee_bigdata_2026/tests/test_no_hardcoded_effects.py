import pytest

def test_no_hardcoded_effects():
    """Ensure no hardcoded publication effect sizes exist in active evaluation code."""
    target_pattern = "v_full" + "_sr = 0.81"
    active_script = "research/prelude_v1/pilots/ieee_phase11_execution.py"
    with open(active_script, "r") as f:
        text = f.read()
    assert target_pattern not in text
