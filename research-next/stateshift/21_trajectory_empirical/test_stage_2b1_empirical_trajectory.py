#!/usr/bin/env python3
"""
Phase 2B.1 Empirical Trajectory Automated Validation Suite
"""

import os, json, hashlib, pandas as pd

def run_tests():
    print("==========================================================================")
    print("STATESHIFT PHASE 2B.1 EMPIRICAL TRAJECTORY TEST SUITE")
    print("==========================================================================")
    
    emp_dir = "research-next/stateshift/21_trajectory_empirical"
    raw_path = os.path.join(emp_dir, "04_RAW_RESULTS.jsonl")
    
    # 1. Check raw rollouts record count == 8,172
    lines = 0
    with open(raw_path) as f:
        for line in f:
            lines += 1
    assert lines == 8172, f"Expected 8172 raw rollouts, found {lines}"
    print("Test 1: 8,172 Raw Rollout Record Count -> PASSED")
    
    # 2. Check Raw Data SHA256 matches 05_RAW_RESULTS.sha256
    with open(raw_path, "rb") as f:
        actual_sha = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.join(emp_dir, "05_RAW_RESULTS.sha256")) as f:
        stored_sha = f.read().split()[0]
    assert actual_sha == stored_sha, f"SHA mismatch: {actual_sha} vs {stored_sha}"
    print("Test 2: Raw Results SHA-256 Integrity Verification -> PASSED")
    
    # 3. Check 5-Point Vector in 10_EMPIRICAL_TRAJECTORY_ANALYSIS.md
    df_contrast = pd.read_csv(os.path.join(emp_dir, "07_TRAJECTORY_CONTRAST_RESULTS.csv"))
    gamma_64 = df_contrast[df_contrast["checkpoint"] == 64]["gamma_t"].values[0]
    gamma_128 = df_contrast[df_contrast["checkpoint"] == 128]["gamma_t"].values[0]
    gamma_192 = df_contrast[df_contrast["checkpoint"] == 192]["gamma_t"].values[0]
    
    assert gamma_64 > 0 and gamma_128 > 0 and gamma_192 > 0, "Intermediate Gammas not positive!"
    print("Test 3: Intermediate Contrast Positivity Verification -> PASSED")
    
    print("==========================================================================")
    print("ALL STAGE 2B.1 AUTOMATED TESTS PASSED 100% CLEAN!")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_tests()
