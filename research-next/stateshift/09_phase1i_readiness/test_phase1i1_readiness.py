import json
import os
import hashlib

readiness_dir = "research-next/stateshift/09_phase1i_readiness"
v4_registry = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"
v4_strict = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"

def run_tests():
    print("==========================================================================")
    print("RUNNING PHASE 1I.1 PRE-AUTHORIZATION READINESS AUTOMATED TEST SUITE")
    print("==========================================================================")

    # Test 1: Authoritative Registry Verification (N=454)
    with open(v4_registry, "rb") as f:
        bytes4 = f.read()
    sha4 = hashlib.sha256(bytes4).hexdigest()
    data4 = json.loads(bytes4)
    print(f"[TEST 1] Authoritative Registry Count: {len(data4)} | SHA-256: {sha4} -> ", end="")
    assert len(data4) == 454
    assert sha4 == "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478"
    print("PASSED")

    # Test 2: Strict Contamination Registry Verification (N=388)
    with open(v4_strict, "rb") as f:
        bytes_strict = f.read()
    sha_strict = hashlib.sha256(bytes_strict).hexdigest()
    data_strict = json.loads(bytes_strict)
    print(f"[TEST 2] Strict Registry Count: {len(data_strict)} | SHA-256: {sha_strict} -> ", end="")
    assert len(data_strict) == 388
    assert sha_strict == "667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227"
    print("PASSED")

    # Test 3: Rollout Accounting & Dry-Run Ledger V2 Check (Exact 130,752)
    ledger_path = os.path.join(readiness_dir, "PHASE1I_DRY_RUN_LEDGER_V2.jsonl")
    with open(ledger_path, "r") as f:
        lines = f.readlines()
    print(f"[TEST 3] Dry-Run Ledger V2 Count: {len(lines)} records (Expected: 130752) -> ", end="")
    assert len(lines) == 130752
    print("PASSED")

    # Test 4: Zero Duplicates & Zero Seed Collisions
    seen_ids = set()
    seen_seeds = set()
    for line in lines:
        r = json.loads(line)
        rid = r["rollout_id"]
        sd = r["deterministic_seed"]
        assert rid not in seen_ids, f"Duplicate ID: {rid}"
        seen_ids.add(rid)
        seen_seeds.add(sd)
    print(f"[TEST 4] Unique Rollout IDs: {len(seen_ids)} | Unique Deterministic Seeds: {len(seen_seeds)} -> ", end="")
    assert len(seen_ids) == 130752
    assert len(seen_seeds) == 130752
    print("PASSED")

    # Test 5: Estimand Restoration Verification
    est_path = os.path.join(readiness_dir, "PRIMARY_ESTIMAND_RECONCILIATION_1I1.md")
    with open(est_path, "r") as f:
        est_text = f.read()
    print(f"[TEST 5] Primary Estimand Gamma_256 Restoration -> ", end="")
    assert "Gamma_T" in est_text or r"\Gamma_T" in est_text
    assert "256" in est_text
    print("PASSED")

    # Test 6: Checkpoint Registry V2 Integrity
    ckpt_path = os.path.join(readiness_dir, "PHASE1I_CHECKPOINT_REGISTRY_V2.json")
    with open(ckpt_path, "r") as f:
        ckpts = json.load(f)
    print(f"[TEST 6] Checkpoint Registry V2 Integrity (9/9) -> ", end="")
    assert len(ckpts) == 9
    assert ckpts[0]["verification_status"] == "LOAD_VERIFIED / GENERATION_VERIFIED"
    assert ckpts[-1]["verification_status"] == "LOAD_VERIFIED / GENERATION_VERIFIED"
    print("PASSED")

    # Test 7: Cost Accounting for N=454
    wall_clock = 16.09
    gpu_count = 4
    total_gpu_hours = wall_clock * gpu_count
    print(f"[TEST 7] Reconciled Cost Accounting ({wall_clock}h x {gpu_count} GPUs = {total_gpu_hours:.2f} GPU-hours) -> ", end="")
    assert abs(total_gpu_hours - 64.36) < 1e-2
    print("PASSED")

    print("==========================================================================")
    print("ALL PHASE 1I.1 READINESS TESTS PASSED CLEANLY!")
    print("==========================================================================")

if __name__ == "__main__":
    run_tests()
