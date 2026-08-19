#!/usr/bin/env python3
"""
Phase 2B.2 Protocol Comparability & Forensics Test Suite
"""

import os, json, pandas as pd

def run_tests():
    print("==========================================================================")
    print("STATESHIFT PHASE 2B.2 PROTOCOL COMPARABILITY TEST SUITE")
    print("==========================================================================")
    
    emp_dir = "research-next/stateshift/21_trajectory_empirical"
    forensic_csv = os.path.join(emp_dir, "18_TOKEN_LENGTH_FORENSICS.csv")
    
    # 1. Check token length forensics
    df_f = pd.read_csv(forensic_csv)
    max_tok = int(df_f[df_f["metric_name"] == "max_generated_tokens"]["empirical_value"].values[0])
    over_512 = int(df_f[df_f["metric_name"] == "rollouts_exceeding_512_tokens"]["empirical_value"].values[0])
    
    assert max_tok <= 512, f"Max tokens {max_tok} exceeds 512 boundary!"
    assert over_512 == 0, f"Over 512 rollouts count {over_512} is not zero!"
    print("Test 1: Token Length Forensics (Max Tokens <= 512) -> PASSED")
    
    # 2. Check Decision File
    dec_file = os.path.join(emp_dir, "20_TRAJECTORY_MANUSCRIPT_ENABLEMENT_DECISION.md")
    assert os.path.exists(dec_file), "Decision file missing"
    print("Test 2: Manuscript Enablement Decision File -> PASSED")
    
    print("==========================================================================")
    print("ALL STAGE 2B.2 AUTOMATED TESTS PASSED 100% CLEAN!")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_tests()
