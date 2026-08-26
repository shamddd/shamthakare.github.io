"""
Anti-Fabrication & Security Unit Tests for Phase 8 Engine
Author: Sham Satish Thakare
"""

import os, sys, json, subprocess, pytest
from scripts.runpod_resumable_runner import parse_boxed_answer, verify_answer, SCIENTIFIC_PROTOCOL_SHA, EXECUTION_CODE_SHA

def test_mock_never_marked_raw(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m"
    }) + "\n")

    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir), "--mock"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0

    out_file = out_dir / "gsm8k_R_0.jsonl"
    data = json.loads(out_file.read_text().strip())
    assert data["empirical_status"] == "MOCK_BACKEND"
    assert data["empirical_status"] != "RAW_MODEL_INFERENCE"

def test_real_mode_requires_cuda(tmp_path):
    out_dir = tmp_path / "real_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m"
    }) + "\n")

    # Real mode without GPU should fail closed
    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode != 0
    assert "FAIL-CLOSED" in res.stdout or "FAIL-CLOSED" in res.stderr

def test_mock_real_directories_separated(tmp_path):
    real_dir = tmp_path / "stateshift_v3_real" / "raw"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m"
    }) + "\n")

    # Mock mode forbidden from outputting to real directory
    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(real_dir), "--mock"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode != 0
    assert "FAIL-CLOSED" in res.stdout

def test_verifier_uses_reference_answer():
    assert parse_boxed_answer("Answer is \\boxed{42}.") == "42"
    assert parse_boxed_answer("No box here.") == ""
    assert verify_answer("42", "42") == 1
    assert verify_answer("99", "42") == 0
    assert verify_answer("3 + 5", "8") == 1

def test_execution_sha_pinned():
    assert SCIENTIFIC_PROTOCOL_SHA == "750039aa76bcd197ca7abf4fd91f202260914afb"
    assert len(EXECUTION_CODE_SHA) >= 7
