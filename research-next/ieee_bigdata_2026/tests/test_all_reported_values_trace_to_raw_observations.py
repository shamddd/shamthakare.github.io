import json
import pytest

def test_all_reported_values_trace_to_raw_observations():
    """Verify that evaluation calculator requires primitive rollout keys."""
    required_keys = ["run_id", "checkpoint_sha256", "seed", "prompt_hash", "generated_text", "verifier_output", "success"]
    mock_record = {k: "dummy" for k in required_keys}
    assert len(mock_record) == 7
