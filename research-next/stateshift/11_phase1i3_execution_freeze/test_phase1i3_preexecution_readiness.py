import json
import os
import hashlib
import unittest

freeze_dir = "research-next/stateshift/11_phase1i3_execution_freeze"
v4_registry = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"
v4_strict = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"

def run_tests():
    print("==========================================================================")
    print("RUNNING PHASE 1I.3 PRE-EXECUTION READINESS AUTOMATED TEST SUITE")
    print("==========================================================================")

    # Test 1: Authoritative Primary Registry (N=454)
    with open(v4_registry, "rb") as f:
        bytes4 = f.read()
    sha4 = hashlib.sha256(bytes4).hexdigest()
    data4 = json.loads(bytes4)
    print(f"[TEST 1] Primary Registry Count: {len(data4)} | SHA-256: {sha4} -> ", end="")
    assert len(data4) == 454
    assert sha4 == "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478"
    print("PASSED")

    # Test 2: Strict Sensitivity Registry (N=388)
    with open(v4_strict, "rb") as f:
        bytes_strict = f.read()
    sha_strict = hashlib.sha256(bytes_strict).hexdigest()
    data_strict = json.loads(bytes_strict)
    print(f"[TEST 2] Strict Registry Count: {len(data_strict)} | SHA-256: {sha_strict} -> ", end="")
    assert len(data_strict) == 388
    assert sha_strict == "667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227"
    print("PASSED")

    # Test 3: Final Ledger Row Count (Exact 29,056)
    ledger_path = os.path.join(freeze_dir, "PHASE1I3_FINAL_CONFIRMATORY_LEDGER.jsonl")
    with open(ledger_path, "r") as f:
        lines = f.readlines()
    print(f"[TEST 3] Final Confirmatory Ledger Count: {len(lines)} records (Expected: 29056) -> ", end="")
    assert len(lines) == 29056
    print("PASSED")

    # Test 4: Unique IDs, Checkpoint Set {0, 256}, and Zero Seed Collisions
    seen_ids = set()
    seen_seeds = set()
    seen_ckpts = set()
    for line in lines:
        r = json.loads(line)
        rid = r["rollout_id"]
        sd = r["deterministic_seed"]
        ckpt = r["checkpoint_t"]
        assert rid not in seen_ids, f"Duplicate ID: {rid}"
        seen_ids.add(rid)
        seen_seeds.add(sd)
        seen_ckpts.add(ckpt)
    
    print(f"[TEST 4] Checkpoints Set: {sorted(list(seen_ckpts))} | Unique IDs: {len(seen_ids)} | Unique Seeds: {len(seen_seeds)} -> ", end="")
    assert sorted(list(seen_ckpts)) == [0, 256]
    assert len(seen_ids) == 29056
    assert len(seen_seeds) == 29056
    print("PASSED")

    # Test 5: Estimand Formulation Invariant
    est_path = os.path.join(freeze_dir, "PHASE1I3_FINAL_PRIMARY_PROTOCOL.md")
    with open(est_path, "r") as f:
        est_text = f.read()
    print(f"[TEST 5] Primary Estimand Gamma_256 Formulation -> ", end="")
    assert "Gamma_256" in est_text or r"\Gamma_{256}" in est_text
    assert "0" in est_text and "256" in est_text
    print("PASSED")

    # Test 6: Cost Safety Guard ($8.00 Ceiling)
    guard_path = os.path.join(freeze_dir, "PHASE1I3_FINAL_COST_AND_SPEND_GUARD.md")
    with open(guard_path, "r") as f:
        guard_text = f.read()
    print(f"[TEST 6] Hard Project Spend Ceiling Guard ($8.00) -> ", end="")
    assert "$8.00 USD" in guard_text
    print("PASSED")

    print("==========================================================================")
    print("ALL PHASE 1I.3 PRE-EXECUTION READINESS TESTS PASSED CLEANLY!")
    print("==========================================================================")

if __name__ == "__main__":
    run_tests()
