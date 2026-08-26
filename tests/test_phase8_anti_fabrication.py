"""
Anti-Fabrication & Security Unit Tests for Phase 8 Engine
Author: Sham Satish Thakare
"""

import os, sys, json, subprocess, pytest
from scripts.runpod_resumable_runner import parse_boxed_answer, verify_answer, check_manifest_overlap, SCIENTIFIC_PROTOCOL_SHA

def test_mock_never_marked_raw(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m", "reference_answer": "42"
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
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m", "reference_answer": "42"
    }) + "\n")

    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode != 0
    assert "FAIL-CLOSED" in res.stdout or "FAIL-CLOSED" in res.stderr

def test_mock_real_directories_separated(tmp_path):
    real_dir = tmp_path / "stateshift_v3_real" / "raw"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m", "reference_answer": "42"
    }) + "\n")

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

def test_benchmark_confirmatory_overlap_fails(tmp_path):
    bench_file = tmp_path / "bench.jsonl"
    conf_file = tmp_path / "conf.jsonl"

    # Write overlapping problem ID
    bench_file.write_text(json.dumps({"problem_id": "gsm8k_overlap_001"}) + "\n")
    conf_file.write_text(json.dumps({"problem_id": "gsm8k_overlap_001"}) + "\n")

    assert not check_manifest_overlap(str(bench_file), str(conf_file))

def test_missing_reference_answer_fails(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    # Missing reference_answer field
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "m"
    }) + "\n")

    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir), "--mock"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode != 0
    assert "FAIL-CLOSED" in res.stdout

def test_manifest_seed_reaches_sampling_params(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    manifest_file.write_text(json.dumps({
        "job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 1337, "model_id": "m", "reference_answer": "42"
    }) + "\n")

    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir), "--mock"]
    subprocess.run(cmd, check=True)

    out_file = out_dir / "gsm8k_R_0.jsonl"
    data = json.loads(out_file.read_text().strip())
    assert data["seed"] == 1337
    assert data["effective_generation_seed"] == 1337

def test_different_rollout_seeds_are_distinct(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
    j1 = {"job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 1000, "model_id": "m", "reference_answer": "42"}
    j2 = {"job_key": "p1_R_0_k1", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 1, "seed": 1001, "model_id": "m", "reference_answer": "42"}
    manifest_file.write_text(json.dumps(j1) + "\n" + json.dumps(j2) + "\n")

    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(out_dir), "--mock"]
    subprocess.run(cmd, check=True)

    out_file = out_dir / "gsm8k_R_0.jsonl"
    lines = out_file.read_text().strip().split("\n")
    seeds = [json.loads(l)["effective_generation_seed"] for l in lines]
    assert seeds == [1000, 1001]
