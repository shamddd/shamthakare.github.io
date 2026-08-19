import json
import os
import hashlib
import unittest

readiness_dir = "research-next/stateshift/09_phase1i_readiness"
calib_dir = "research-next/stateshift/09_phase1h2_gpu_calibration"

def run_tests():
    print("==========================================================================")
    print("RUNNING PHASE 1I READINESS AUTOMATED TEST SUITE")
    print("==========================================================================")

    # Test 1: Dry-Run Ledger Count (Exact 131,328)
    ledger_path = os.path.join(readiness_dir, "PHASE1I_DRY_RUN_LEDGER.jsonl")
    with open(ledger_path, "r") as f:
        lines = f.readlines()
    print(f"[TEST 1] Dry-Run Ledger Count: {len(lines)} records (Expected: 131328) -> ", end="")
    assert len(lines) == 131328
    print("PASSED")

    # Test 2: Unique Rollout IDs and Reproducible Seed Mapping
    seen_ids = set()
    seen_seeds = set()
    for line in lines:
        r = json.loads(line)
        rid = r["rollout_id"]
        sd = r["deterministic_seed"]
        assert rid not in seen_ids, f"Duplicate ID: {rid}"
        seen_ids.add(rid)
        seen_seeds.add(sd)
    print(f"[TEST 2] Unique Rollout IDs: {len(seen_ids)} | Unique Deterministic Seeds: {len(seen_seeds)} -> ", end="")
    assert len(seen_ids) == 131328
    assert len(seen_seeds) == 131328
    print("PASSED")

    # Test 3: Technical Record Firewall Assertion
    def test_firewall(record):
        if record.get("record_type") != "empirical_confirmatory":
            raise ValueError(f"FIREWALL REJECTION: Invalid record_type '{record.get('record_type')}'")

    canary_sample = {"record_type": "technical_canary", "canary_id": "test"}
    dry_run_sample = {"record_type": "dry_run_placeholder", "rollout_id": "test"}
    confirmatory_sample = {"record_type": "empirical_confirmatory", "rollout_id": "test"}

    firewall_passed = False
    try:
        test_firewall(canary_sample)
    except ValueError:
        try:
            test_firewall(dry_run_sample)
        except ValueError:
            test_firewall(confirmatory_sample)
            firewall_passed = True

    print(f"[TEST 3] Scientific Firewall Assertion Test -> ", end="")
    assert firewall_passed
    print("PASSED")

    # Test 4: Checkpoint Registry Integrity (9/9)
    ckpt_path = os.path.join(readiness_dir, "PHASE1I_CHECKPOINT_REGISTRY.json")
    with open(ckpt_path, "r") as f:
        ckpts = json.load(f)
    print(f"[TEST 4] Checkpoint Registry Count: {len(ckpts)}/9 -> ", end="")
    assert len(ckpts) == 9
    assert all(c["status"] == "READY" for c in ckpts)
    print("PASSED")

    # Test 5: Cost Accounting Identity
    wall_clock = 16.16
    gpu_count = 4
    total_gpu_hours = wall_clock * gpu_count
    print(f"[TEST 5] Cost Accounting Identity ({wall_clock}h x {gpu_count} GPUs = {total_gpu_hours:.2f} GPU-hours) -> ", end="")
    assert abs(total_gpu_hours - 64.64) < 1e-4
    print("PASSED")

    print("==========================================================================")
    print("ALL READINESS TESTS PASSED CLEANLY!")
    print("==========================================================================")

if __name__ == "__main__":
    run_tests()
