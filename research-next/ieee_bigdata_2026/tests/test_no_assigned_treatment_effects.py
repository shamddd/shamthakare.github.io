import os
import pytest

def test_no_assigned_treatment_effects():
    """Scan active code for hardcoded expected treatment effect assignments."""
    banned_keywords = ["expected_" + "effect", "expected_" + "delta", "expected_" + "score", "target_" + "effect"]
    active_dir = "research-next/ieee_bigdata_2026"
    for root, dirs, files in os.walk(active_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("test_"):
                path = os.path.join(root, f)
                with open(path, "r") as fp:
                    content = fp.read()
                    for kw in banned_keywords:
                        assert kw not in content, f"Hardcoded effect keyword '{kw}' found in {path}"
