import os
import pytest

def test_no_hardcoded_publication_results():
    """Ensure no hardcoded publication numbers exist in runtime evaluation scripts."""
    pattern_a = "v_full" + "_sr = 0.81"
    pattern_b = "0.03125"
    active_dir = "research-next/ieee_bigdata_2026"
    for root, dirs, files in os.walk(active_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("test_"):
                path = os.path.join(root, f)
                with open(path, "r") as fp:
                    content = fp.read()
                    assert pattern_a not in content, f"Hardcoded result pattern in {path}"
