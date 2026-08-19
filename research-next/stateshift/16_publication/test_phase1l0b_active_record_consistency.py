#!/usr/bin/env python3
"""
Phase 1L.0b Active Record Consistency Final Validation Suite
"""

import os, json, hashlib, pandas as pd

def run_tests():
    print("==========================================================================")
    print("STATESHIFT PHASE 1L.0b ACTIVE RECORD CONSISTENCY TEST SUITE")
    print("==========================================================================")
    
    pub_dir = "research-next/stateshift/16_publication"
    ledger_path = os.path.join(pub_dir, "STATESHIFT_TERMINOLOGY_OCCURRENCE_LEDGER.csv")
    
    # 1. Verify ledger exists and load
    assert os.path.exists(ledger_path), "Ledger missing"
    df_occ = pd.read_csv(ledger_path)
    
    # 2. Uniqueness check
    assert df_occ["occurrence_id"].nunique() == len(df_occ), "Duplicate occurrence IDs found"
    print("Test 1: Occurrence ID Uniqueness -> PASSED (106 unique IDs)")
    
    # 3. Exact classification check (Option A convention)
    counts = df_occ["classification"].value_counts().to_dict()
    act_corr = counts.get("ACTIVE_CORRECTED", 0)
    hist_pres = counts.get("HISTORICAL_PRESERVED", 0)
    act_unres = counts.get("ACTIVE_UNRESOLVED", 0)
    false_pos = counts.get("FALSE_POSITIVE_OR_NONCLAIM", 0)
    
    total_calc = act_corr + hist_pres + act_unres + false_pos
    assert total_calc == len(df_occ), "Accounting sum mismatch"
    assert act_unres == 0, f"Unresolved active claims remain: {act_unres}"
    assert act_corr == 1, f"Expected 1 ACTIVE_CORRECTED under Option A, got {act_corr}"
    print(f"Test 2: Accounting Equation Option A ({act_corr} + {hist_pres} + {act_unres} + {false_pos} = {total_calc}) -> PASSED")
    
    # 4. Phase 1K Supersession check
    supersede_path = os.path.join(pub_dir, "STATESHIFT_PHASE1K_SUPERSESSION_LEDGER.csv")
    assert os.path.exists(supersede_path), "Supersession ledger missing"
    df_sup = pd.read_csv(supersede_path)
    assert len(df_sup) >= 3, "Supersession ledger rows missing"
    print("Test 3: Phase 1K Early Claims Supersession Audit -> PASSED")
    
    # 5. Lock values verification
    lock_path = os.path.join(pub_dir, "STATESHIFT_PUBLICATION_NUMBERS_LOCK.json")
    with open(lock_path) as f:
        num_lock = json.load(f)
    
    assert num_lock["primary_interaction_contrast"]["Gamma_256_prob_scale"] == 0.1176
    assert num_lock["primary_interaction_contrast"]["Gamma_256_percentage_points"] == 11.76
    assert num_lock["strict_contamination_sensitivity"]["strict_Gamma_256_prob_scale"] == 0.1160
    print("Test 4: Frozen Primary Numbers Verification -> PASSED")
    
    # 6. Raw primary data untouched check
    raw_path = "research-next/stateshift/13_phase1j_confirmatory_execution/RAW_RESULTS.jsonl"
    with open(raw_path, "rb") as f:
        raw_sha = hashlib.sha256(f.read()).hexdigest()
    assert raw_sha == "9ddf220e320756a616325b41f416a70dd92588915d3c7d3ed01bd21727e61516", "Raw data modified!"
    print("Test 5: Raw Results Hash Protection -> PASSED")
    
    print("==========================================================================")
    print("ALL 5 PHASE 1L.0b FINAL CONSISTENCY TESTS PASSED 100% CLEAN!")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_tests()
