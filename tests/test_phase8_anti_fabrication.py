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

    bench_file.write_text(json.dumps({"problem_id": "gsm8k_overlap_001"}) + "\n")
    conf_file.write_text(json.dumps({"problem_id": "gsm8k_overlap_001"}) + "\n")

    assert not check_manifest_overlap(str(bench_file), str(conf_file))

def test_missing_reference_answer_fails(tmp_path):
    out_dir = tmp_path / "mock_dir"
    manifest_file = tmp_path / "manifest.jsonl"
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

def test_confirmatory_prompts_not_placeholders():
    manifest_path = "artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl"
    with open(manifest_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 100: # Check sample
                break
            data = json.loads(line)
            prompt = data["prompt"]
            assert "Calculate the value for problem" not in prompt
            assert len(prompt) > 20

def test_prefixes_contain_real_reasoning():
    manifest_path = "artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl"
    with open(manifest_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 100:
                break
            data = json.loads(line)
            prefix = data["prefix"]
            assert "Reasoning prefix for arm" not in prefix

def test_confirmatory_ids_map_to_real_gsm8k():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 500
    for r in rows:
        assert len(r["question"]) > 10
        assert r["reference_answer"].lstrip("-").isdigit()

def test_toy_pilot_never_used_for_scientific_benchmark():
    bench_path = "artifacts/stateshift_v4/manifest/pilot_benchmark_job_manifest.jsonl"
    with open(bench_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 100
    for r in rows:
        assert "Janet has" in r["prompt"] or len(r["prompt"]) > 15
        assert "gsm8k_conf_" not in r["problem_id"]
