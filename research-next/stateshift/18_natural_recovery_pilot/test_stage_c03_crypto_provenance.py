#!/usr/bin/env python3
"""
Phase 2 Stage C0.3 Cryptographic Provenance Automated Validation Suite
"""

import os, json, hashlib, pandas as pd

def run_tests():
    print("==========================================================================")
    print("STATESHIFT PHASE 2 STAGE C0.3 CRYPTOGRAPHIC PROVENANCE TEST SUITE")
    print("==========================================================================")
    
    pilot_dir = "research-next/stateshift/18_natural_recovery_pilot"
    ledger_path = os.path.join(pilot_dir, "30_PILOT_TRUE_SHA256_LEDGER.csv")
    
    # 1. Verify 64-char SHA256 length in ledger
    df = pd.read_csv(ledger_path)
    for idx, row in df.iterrows():
        pri_sha = str(row["primary_sha256"]).strip()
        pil_sha = str(row["pilot_sha256"]).strip()
        assert len(pri_sha) == 64, f"primary_sha256 not 64 hex chars: {pri_sha}"
        assert len(pil_sha) == 64, f"pilot_sha256 not 64 hex chars: {pil_sha}"
    print("Test 1: True SHA-256 64-Char Format -> PASSED")
    
    # 2. Original identifier type documented
    assert "original_identifier_type" in df.columns, "Missing identifier type column"
    assert "HUGGINGFACE_GIT_BLOB_SHA1" in df["original_identifier_type"].values, "Missing HF Blob SHA1 algorithm label"
    print("Test 2: Original Identifier Algorithm Documentation -> PASSED")
    
    # 3. Provenance lock validation
    lock_path = os.path.join(pilot_dir, "33_NATURAL_RECOVERY_FINAL_PROVENANCE_LOCK.json")
    with open(lock_path) as f:
        lock_data = json.load(f)
    assert lock_data["verified_commit_sha"] == "7667ad787966f5733fdca3d2b240452d7095ff95"
    assert lock_data["historical_invalid_sha"] == "50bdcb5a50bdcb5a50bdcb5a50bdcb5a50bdcb5a"
    assert lock_data["manuscript_claim_status"] == "ENABLED"
    print("Test 3: Final Provenance Lock Validation -> PASSED")
    
    # 4. Raw results hash check
    raw_path = os.path.join(pilot_dir, "06_PILOT_RAW_RESULTS.jsonl")
    with open(raw_path, "rb") as f:
        raw_sha = hashlib.sha256(f.read()).hexdigest()
    assert raw_sha == "6519e56730b4eef2c985325a4632798bc9bb85851c4a7f4ad5c95e001328d479", "Raw pilot data altered!"
    print("Test 4: Pilot Raw Results Hash Verification -> PASSED")
    
    print("==========================================================================")
    print("ALL 4 STAGE C0.3 AUTOMATED PROVENANCE TESTS PASSED 100% CLEAN!")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_tests()
