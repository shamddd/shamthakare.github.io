import pytest

def ingest_analysis_record(record, mode="empirical"):
    if mode == "empirical":
        if record.get("record_type") == "mock_fixture":
            raise ValueError("Mock fixture record rejected in empirical analysis mode!")
    return True

def test_mock_records_blocked_from_empirical_analysis():
    """Verify that records tagged record_type='mock_fixture' are strictly rejected in empirical mode."""
    mock_record = {"record_type": "mock_fixture", "v_s": 0.85}
    empirical_record = {"record_type": "empirical", "primitive_success": True}
    
    with pytest.raises(ValueError):
        ingest_analysis_record(mock_record, mode="empirical")
        
    assert ingest_analysis_record(mock_record, mode="testing") is True
    assert ingest_analysis_record(empirical_record, mode="empirical") is True
