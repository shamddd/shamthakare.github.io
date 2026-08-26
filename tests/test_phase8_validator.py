"""
Unit Tests for Phase 8 Raw Completion Validator
Author: Sham Satish Thakare
"""

import os, sys, json, subprocess, pytest
from scripts.validate_raw_completions import validate_raw_dir

def test_validator_rejects_synthetic_fixture(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    
    # Create fake fixture with empirical_status = SYNTHETIC_TEST_FIXTURE
    fname = raw_dir / "gsm8k_R_0.jsonl"
    record = {
        "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0,
        "raw_completion": "Step 1...", "parsed_answer": "42", "verifier_result": 1,
        "empirical_status": "SYNTHETIC_TEST_FIXTURE"
    }
    fname.write_text(json.dumps(record) + "\n")
    
    assert not validate_raw_dir(str(raw_dir), allow_partial=True)

def test_validator_accepts_valid_empirical_records(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    
    fname = raw_dir / "gsm8k_R_0.jsonl"
    record = {
        "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0,
        "raw_completion": "Step 1: Reasoning... \\boxed{42}", "parsed_answer": "42", "verifier_result": 1,
        "empirical_status": "RAW_MODEL_INFERENCE"
    }
    fname.write_text(json.dumps(record) + "\n")
    
    assert validate_raw_dir(str(raw_dir), allow_partial=True)

def test_validator_rejects_duplicate_rollout_keys(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    
    fname = raw_dir / "gsm8k_R_0.jsonl"
    record = {
        "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0,
        "raw_completion": "Step 1...", "parsed_answer": "42", "verifier_result": 1,
        "empirical_status": "RAW_MODEL_INFERENCE"
    }
    # Write duplicate line
    fname.write_text(json.dumps(record) + "\n" + json.dumps(record) + "\n")
    
    assert not validate_raw_dir(str(raw_dir), allow_partial=True)
