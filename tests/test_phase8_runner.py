"""
Unit Tests for Phase 8 Resumable Runner
Author: Sham Satish Thakare
"""

import os, sys, shutil, json, subprocess, pytest

def test_runner_mock_execution(tmp_path):
    output_dir = tmp_path / "raw"
    manifest_file = tmp_path / "manifest.jsonl"
    
    # Create sample manifest
    jobs = [
        {"job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "Qwen/Qwen2.5-7B"},
        {"job_key": "p1_R_0_k1", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 1, "seed": 43, "model_id": "Qwen/Qwen2.5-7B"},
    ]
    with open(manifest_file, "w") as f:
        for j in jobs:
            f.write(json.dumps(j) + "\n")
            
    # Run runner in mock mode
    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(output_dir), "--mock"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0, f"Runner failed: {res.stderr}"
    
    # Check created file
    out_file = output_dir / "gsm8k_R_0.jsonl"
    assert out_file.exists()
    
    lines = out_file.read_text().strip().split("\n")
    assert len(lines) == 2
    d0 = json.loads(lines[0])
    assert d0["empirical_status"] == "RAW_MODEL_INFERENCE"
    assert d0["job_key"] == "p1_R_0_k0"

def test_runner_resumption(tmp_path):
    output_dir = tmp_path / "raw"
    manifest_file = tmp_path / "manifest.jsonl"
    
    jobs = [
        {"job_key": "p1_R_0_k0", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 0, "seed": 42, "model_id": "Qwen/Qwen2.5-7B"},
        {"job_key": "p1_R_0_k1", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 1, "seed": 43, "model_id": "Qwen/Qwen2.5-7B"},
    ]
    with open(manifest_file, "w") as f:
        for j in jobs:
            f.write(json.dumps(j) + "\n")
            
    # Run first job only
    cmd1 = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(output_dir), "--mock"]
    subprocess.run(cmd1, check=True)

    # Add 3rd job to manifest
    jobs.append({"job_key": "p1_R_0_k2", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": 2, "seed": 44, "model_id": "Qwen/Qwen2.5-7B"})
    with open(manifest_file, "w") as f:
        for j in jobs:
            f.write(json.dumps(j) + "\n")

    # Run again - should resume and add only 3rd job
    cmd2 = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(output_dir), "--mock"]
    subprocess.run(cmd2, check=True)

    out_file = output_dir / "gsm8k_R_0.jsonl"
    lines = out_file.read_text().strip().split("\n")
    assert len(lines) == 3
    keys = [json.loads(l)["job_key"] for l in lines]
    assert keys == ["p1_R_0_k0", "p1_R_0_k1", "p1_R_0_k2"]

def test_runner_budget_cap_halting(tmp_path):
    output_dir = tmp_path / "raw"
    manifest_file = tmp_path / "manifest.jsonl"
    
    jobs = [{"job_key": f"p1_R_0_k{i}", "problem_id": "p1", "arm": "R", "checkpoint": 0, "rollout_index": i, "seed": i, "model_id": "m"} for i in range(10)]
    with open(manifest_file, "w") as f:
        for j in jobs:
            f.write(json.dumps(j) + "\n")

    # Pass max_budget_usd = 0.0 to trigger cost stop
    cmd = [sys.executable, "scripts/runpod_resumable_runner.py", "--manifest", str(manifest_file), "--output_dir", str(output_dir), "--mock", "--max_budget_usd", "0.00"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert "BUDGET CAP REACHED" in res.stdout
