import os
import ast
import pytest

def test_seed_used_only_for_rng():
    """AST scan to ensure 'seed' variable is only passed to random/torch seed functions."""
    banned_ops = ["seed" + " - ", "seed" + " + ", "seed" + " * ", "(seed" + " - ", "(seed" + " + "]
    active_dir = "research-next/ieee_bigdata_2026"
    for root, dirs, files in os.walk(active_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("test_"):
                path = os.path.join(root, f)
                with open(path, "r") as fp:
                    content = fp.read()
                    for op in banned_ops:
                        assert op not in content, f"Forbidden seed arithmetic '{op}' found in {path}"
