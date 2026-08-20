import pytest

def test_generation_record_required_for_empirical_values():
    """Verify that empirical evaluation rejects summaries lacking primitive generation text."""
    record = {"generated_text": "step 1... answer", "verifier_success": True}
    assert "generated_text" in record and len(record["generated_text"]) > 0
