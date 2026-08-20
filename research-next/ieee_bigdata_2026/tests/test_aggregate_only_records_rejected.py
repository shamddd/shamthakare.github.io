import pytest

def run_empirical_analysis(record):
    required_keys = {"checkpoint_sha256", "generated_text", "verifier_raw_output", "primitive_success"}
    missing = required_keys - set(record.keys())
    if missing:
        raise ValueError(f"Missing required primitive observation keys: {missing}")
    return True

def test_aggregate_only_records_rejected():
    """Verify that aggregate-only records lacking primitive observations raise ValueError."""
    aggregate_only_record = {"v_full": 0.81, "v_prefix": 0.53}
    with pytest.raises(ValueError):
        run_empirical_analysis(aggregate_only_record)
        
    valid_primitive_record = {
        "checkpoint_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "generated_text": "step 1... answer",
        "verifier_raw_output": {"status": "passed"},
        "primitive_success": True
    }
    assert run_empirical_analysis(valid_primitive_record) is True
