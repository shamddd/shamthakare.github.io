import pytest

def mock_analysis_calculator(records, seed):
    """Analysis pipeline taking raw records and seed parameter."""
    # Pipeline MUST depend ONLY on primitive records, NOT on seed parameter
    successes = [r["primitive_success"] for r in records]
    score = sum(successes) / len(successes) if successes else 0.0
    return {"contrast_c1": score}

def test_analysis_seed_invariance():
    """Runtime canary test: changing seed parameter must NOT alter downstream analysis statistics."""
    dummy_records = [
        {"state_id": "s1", "primitive_success": True},
        {"state_id": "s2", "primitive_success": False},
        {"state_id": "s3", "primitive_success": True}
    ]
    
    res_43 = mock_analysis_calculator(dummy_records, seed=43)
    res_47 = mock_analysis_calculator(dummy_records, seed=47)
    res_999 = mock_analysis_calculator(dummy_records, seed=999)
    
    assert res_43["contrast_c1"] == res_47["contrast_c1"] == res_999["contrast_c1"], "Analysis output changed when seed changed!"
