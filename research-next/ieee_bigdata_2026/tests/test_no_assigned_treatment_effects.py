import os
import pytest

CANONICAL_BANNED_KEYWORDS = {
    "expected_effect", "expected_delta", "expected_score", "expected_result",
    "target_effect", "assigned_effect", "mock_score", "synthetic_score",
    "preset_score", "preset_effect", "treatment_table", "effect_table"
}

def test_no_assigned_treatment_effects():
    """Scan active code using single canonical immutable set of banned keywords."""
    active_dir = "research-next/ieee_bigdata_2026"
    for root, dirs, files in os.walk(active_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("test_"):
                path = os.path.join(root, f)
                with open(path, "r") as fp:
                    content = fp.read()
                    for kw in CANONICAL_BANNED_KEYWORDS:
                        assert kw not in content, f"Hardcoded effect keyword '{kw}' found in {path}"
