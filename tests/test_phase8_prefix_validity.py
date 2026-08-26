"""
Ecological Validity & Prefix Confound Unit Tests for Phase 8 Engine
Author: Sham Satish Thakare
"""

import os, sys, json, re, pytest

def test_no_explicit_error_labels():
    manifest_path = "artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl"
    forbidden_words = ["!=", "(Error in calculation)", "incorrect", "wrong", "invalid", "mistake", "error"]
    
    with open(manifest_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if not line.strip():
                continue
            data = json.loads(line)
            prefix = data["prefix"].lower()
            for word in forbidden_words:
                assert word.lower() not in prefix, f"Forbidden error label '{word}' found in job {data['job_key']}: {prefix}"

def test_r_internal_expression_consistency():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            prob = json.loads(line)
            r_pref = prob["prefixes"]["R"]
            assert "<<" not in r_pref, f"Internal annotation '<<' found in R prefix for {prob['problem_id']}"
            assert ">>" not in r_pref, f"Internal annotation '>>' found in R prefix for {prob['problem_id']}"

def test_a1_is_plausible_math_error():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            prob = json.loads(line)
            a1_pref = prob["prefixes"]["A1"]
            assert "!=" not in a1_pref, f"Explicit inequality '!=' found in A1 prefix for {prob['problem_id']}"
            assert "error" not in a1_pref.lower(), f"Word 'error' found in A1 prefix for {prob['problem_id']}"

def test_no_arm_identity_leakage():
    manifest_path = "artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl"
    arm_pattern = re.compile(r'\barm\s+(r|c|s|a1|a2|p|d)\b', re.IGNORECASE)
    with open(manifest_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            prefix = data["prefix"]
            assert not arm_pattern.search(prefix), f"Arm label leaked into prefix in {data['job_key']}: {prefix}"

def test_a2_p_donor_traceability():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 500
    for idx, prob in enumerate(rows):
        next_prob = rows[(idx + 1) % 500]
        # P prefix should match next problem's clean C prefix
        assert prob["prefixes"]["P"] == next_prob["prefixes"]["C"]

def test_requirements_exactly_pinned():
    req_path = "requirements-phase8-runpod.txt"
    assert os.path.exists(req_path)
    with open(req_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    for line in lines:
        assert "==" in line, f"Requirement '{line}' is not strictly pinned with '=='"
        assert ">=" not in line, f"Requirement '{line}' contains loose '>=' operator"
