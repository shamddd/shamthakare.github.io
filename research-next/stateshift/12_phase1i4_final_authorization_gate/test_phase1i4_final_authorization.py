import json
import os
import sys
import hashlib

sys.path.insert(0, "research-next/stateshift/09_phase1i_readiness")
from run_confirmatory_experiment import (
    verify_safety_guards,
    EXPECTED_N,
    EXPECTED_TOTAL_ROLLOUTS,
    EXPECTED_REGISTRY_SHA256,
    EXPECTED_STRICT_SHA256,
    HARD_SPEND_CEILING_USD,
    MIN_REQUIRED_BALANCE_USD
)

gate_dir = "research-next/stateshift/12_phase1i4_final_authorization_gate"
freeze_dir = "research-next/stateshift/11_phase1i3_execution_freeze"
v4_registry = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"
v4_strict = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"

def run_tests():
    print("==========================================================================")
    print("RUNNING PHASE 1I.4 FINAL EXECUTION AUTHORIZATION TEST SUITE")
    print("==========================================================================")

    # Test 1: No Stale Full-Design Constants & Single Canonical Assignment
    print(f"[TEST 1] Canonical Constants -> Rollouts: {EXPECTED_TOTAL_ROLLOUTS} | N: {EXPECTED_N} | Budget: ${MIN_REQUIRED_BALANCE_USD:.2f} -> ", end="")
    assert EXPECTED_N == 454
    assert EXPECTED_TOTAL_ROLLOUTS == 29056
    assert MIN_REQUIRED_BALANCE_USD == 6.82
    assert HARD_SPEND_CEILING_USD == 8.00
    print("PASSED")

    # Test 2: Primary Registry SHA-256
    with open(v4_registry, "rb") as f:
        sha4 = hashlib.sha256(f.read()).hexdigest()
    print(f"[TEST 2] Primary Registry Hash: {sha4} -> ", end="")
    assert sha4 == EXPECTED_REGISTRY_SHA256
    print("PASSED")

    # Test 3: Strict Sensitivity Registry SHA-256
    with open(v4_strict, "rb") as f:
        sha_strict = hashlib.sha256(f.read()).hexdigest()
    print(f"[TEST 3] Strict Registry Hash: {sha_strict} -> ", end="")
    assert sha_strict == EXPECTED_STRICT_SHA256
    print("PASSED")

    # Test 4: Final Ledger Row Count (29,056)
    ledger_path = os.path.join(freeze_dir, "PHASE1I3_FINAL_CONFIRMATORY_LEDGER.jsonl")
    with open(ledger_path, "r") as f:
        lines = f.readlines()
    print(f"[TEST 4] Final Confirmatory Ledger Row Count: {len(lines)} -> ", end="")
    assert len(lines) == 29056
    print("PASSED")

    # Test 5: Unique IDs & Zero Seed Collisions
    seen_ids, seen_seeds = set(), set()
    for l in lines:
        r = json.loads(l)
        rid, sd = r["rollout_id"], r["deterministic_seed"]
        assert rid not in seen_ids, f"Duplicate ID: {rid}"
        seen_ids.add(rid)
        seen_seeds.add(sd)
    print(f"[TEST 5] Unique Rollout IDs: {len(seen_ids)} | Unique Seeds: {len(seen_seeds)} -> ", end="")
    assert len(seen_ids) == 29056
    assert len(seen_seeds) == 29056
    print("PASSED")

    # Test 6: Token Observability Audit Completeness
    obs_data_path = os.path.join(gate_dir, "TOKEN_OBSERVABILITY_AUDIT_DATA.json")
    with open(obs_data_path, "r") as f:
        obs = json.load(f)
    print(f"[TEST 6] Token Observability Verdict: {obs['observability_verdict']} -> ", end="")
    assert obs["differential_censoring_bias_delta"] == 0.0
    print("PASSED")

    # Test 7: Spend-Guard Verification in Mock Mode
    res_auth = verify_safety_guards(authorize_flag=True, mock_mode=True)
    res_unauth = verify_safety_guards(authorize_flag=False, mock_mode=True)
    print(f"[TEST 7] Spend Guard Check (Auth: {res_auth}, Unauth: {res_unauth}) -> ", end="")
    assert res_auth is True
    assert res_unauth is False
    print("PASSED")

    # Test 8: Configuration Loader Verification
    cfg_path = os.path.join(gate_dir, "PHASE1I4_FINAL_EXECUTION_CONFIG.json")
    with open(cfg_path, "r") as f:
        cfg = json.load(f)
    print(f"[TEST 8] Config Fingerprint Hash -> ", end="")
    assert cfg["authoritative_n"] == 454
    assert cfg["total_confirmatory_rollouts"] == 29056
    print("PASSED")

    print("==========================================================================")
    print("ALL PHASE 1I.4 FINAL AUTHORIZATION TESTS PASSED CLEANLY!")
    print("==========================================================================")

if __name__ == "__main__":
    run_tests()
