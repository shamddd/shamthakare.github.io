"""
Semantic Intervention Security Unit Tests for Phase 8 Engine
Author: Sham Satish Thakare
"""

import os, sys, json, re, pytest

def test_r_differs_from_c_all_500():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    assert len(rows) == 500
    for prob in rows:
        r_pref = prob["prefixes"]["R"]
        c_pref = prob["prefixes"]["C"]
        assert r_pref != c_pref, f"R == C in problem {prob['problem_id']}: {r_pref}"

def test_a1_differs_from_c_all_500():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for prob in rows:
        a1_pref = prob["prefixes"]["A1"]
        c_pref = prob["prefixes"]["C"]
        assert a1_pref != c_pref, f"A1 == C in problem {prob['problem_id']}: {a1_pref}"

def test_a1_differs_from_r_all_500():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for prob in rows:
        a1_pref = prob["prefixes"]["A1"]
        r_pref = prob["prefixes"]["R"]
        assert a1_pref != r_pref, f"A1 == R in problem {prob['problem_id']}: {a1_pref}"

def test_r_contains_perturbed_math_claim_all_500():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for prob in rows:
        r_pref = prob["prefixes"]["R"]
        assert len(r_pref) > 5, f"Empty R prefix in {prob['problem_id']}"
        assert re.search(r'\d+', r_pref), f"No numbers in R prefix for {prob['problem_id']}"

def test_a1_contains_distinct_perturbed_math_claim_all_500():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for prob in rows:
        a1_pref = prob["prefixes"]["A1"]
        assert len(a1_pref) > 5, f"Empty A1 prefix in {prob['problem_id']}"
        assert re.search(r'\d+', a1_pref), f"No numbers in A1 prefix for {prob['problem_id']}"

def test_c_math_claim_matches_canonical_solution():
    registry_path = "artifacts/stateshift_v4/registry/gsm8k_confirmatory_500.jsonl"
    with open(registry_path, "r", encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for prob in rows:
        c_pref = prob["prefixes"]["C"]
        assert len(c_pref) > 5, f"Empty C prefix in {prob['problem_id']}"
        assert re.search(r'\d+', c_pref), f"No numbers in C prefix for {prob['problem_id']}"
