#!/usr/bin/env python3
"""
Phase 2 Stage C0.4 True Byte SHA-256 Automated Validation Suite
"""

import os, json, hashlib, pandas as pd, re

def run_tests():
    print("==========================================================================")
    print("STATESHIFT PHASE 2 STAGE C0.4 TRUE BYTE SHA-256 TEST SUITE")
    print("==========================================================================")
    
    pilot_dir = "research-next/stateshift/18_natural_recovery_pilot"
    ledger_path = os.path.join(pilot_dir, "36_TRUE_BYTE_SHA256_RECOMPUTATION.csv")
    
    # 1. Verify 64-char hex format and no X+X duplication
    df = pd.read_csv(ledger_path)
    hex_pattern = re.compile(r'^[0-9a-f]{64}$')
    
    for idx, row in df.iterrows():
        pri_sha = str(row["primary_sha256_actual"]).strip()
        pil_sha = str(row["pilot_sha256_actual"]).strip()
        
        assert hex_pattern.match(pri_sha), f"primary_sha256 invalid: {pri_sha}"
        assert hex_pattern.match(pil_sha), f"pilot_sha256 invalid: {pil_sha}"
        
        # Check no X+X duplication
        assert pri_sha[:32] != pri_sha[32:], f"primary_sha256 is duplicated 32-char string: {pri_sha}"
        assert pil_sha[:32] != pil_sha[32:], f"pilot_sha256 is duplicated 32-char string: {pil_sha}"
        
    print("Test 1: True 64-Char Hex SHA-256 Formatting & Non-Duplication -> PASSED")
    
    # 2. Verify single cached object classification
    assert set(df["provenance_type"].unique()) == {"SINGLE_CACHED_OBJECT_REFERENCED_BY_BOTH_RUNS"}
    print("Test 2: Single Cached Object Reference Classification -> PASSED")
    
    # 3. Raw results hash check
    raw_path = os.path.join(pilot_dir, "06_PILOT_RAW_RESULTS.jsonl")
    with open(raw_path, "rb") as f:
        raw_sha = hashlib.sha256(f.read()).hexdigest()
    assert raw_sha == "6519e56730b4eef2c985325a4632798bc9bb85851c4a7f4ad5c95e001328d479", "Raw pilot data altered!"
    print("Test 3: Pilot Raw Results Hash Verification -> PASSED")
    
    print("==========================================================================")
    print("ALL 3 STAGE C0.4 AUTOMATED TESTS PASSED 100% CLEAN!")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_tests()
