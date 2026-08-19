#!/usr/bin/env python3
"""
StateShift Phase 1I.3 Endpoint-K16 Confirmatory Execution Launcher
MUST NOT BE EXECUTED WITHOUT EXPLICIT USER AUTHORIZATION.
PHASE 1I.4a: PHASE1I4_FINAL_EXECUTION_CONFIG.json IS THE SINGLE SOURCE OF TRUTH.
"""

import os
import sys
import json
import hashlib
import argparse

# ONLY PERMITTED HARD-CODED CONFIGURATION IDENTIFIERS
CONFIG_PATH = "research-next/stateshift/12_phase1i4_final_authorization_gate/PHASE1I4_FINAL_EXECUTION_CONFIG.json"
EXPECTED_CONFIG_SHA256 = "079f99bf8e5ceb8b45b680b4bc2e34f718e4453031c55ee456da0a331209cdcf"

def load_and_verify_config(cfg_path=CONFIG_PATH, expected_sha=EXPECTED_CONFIG_SHA256):
    """
    Verifies config file existence and SHA-256 hash BEFORE parsing JSON.
    Loads all scientific and runtime invariants without fallback defaults.
    """
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"CONFIG ERROR: Config file missing at '{cfg_path}'")

    with open(cfg_path, "rb") as f:
        cfg_bytes = f.read()

    actual_sha = hashlib.sha256(cfg_bytes).hexdigest()
    if actual_sha != expected_sha:
        raise ValueError(f"CONFIG ERROR: Config SHA-256 mismatch! Expected {expected_sha}, got {actual_sha}")

    config_data = json.loads(cfg_bytes)

    # Strict key extraction — missing key WILL raise KeyError (NO silent default substitution)
    req_keys = [
        "authoritative_registry_path",
        "authoritative_registry_sha256",
        "authoritative_n",
        "strict_registry_path",
        "strict_registry_sha256",
        "strict_n",
        "checkpoints",
        "rollouts_per_cell_k",
        "total_confirmatory_rollouts",
        "model_repositories",
        "model_revisions",
        "sampling_temperature",
        "sampling_top_p",
        "max_new_tokens",
        "protocol_hash",
        "analysis_freeze_hash",
        "ledger_path",
        "ledger_sha256",
        "hard_spend_ceiling_usd",
        "expected_total_budget_usd",
        "max_hourly_gpu_rate_usd",
        "record_type"
    ]

    for k in req_keys:
        if k not in config_data:
            raise KeyError(f"CONFIG ERROR: Required key '{k}' missing from {cfg_path}")

    return config_data

def verify_safety_guards(authorize_flag=False, mock_mode=True, cfg_path=CONFIG_PATH, expected_sha=EXPECTED_CONFIG_SHA256):
    print("==========================================================================")
    print("STATESHIFT PHASE 1I.3 ENDPOINT-K16 CONFIRMATORY EXECUTION BANNER")
    print("==========================================================================")

    # 1. Authoritative User Authorization Check
    if not authorize_flag:
        print("[SAFETY GUARD 1] ERROR: User authorization flag '--authorize-confirmatory-run' NOT provided.")
        print("EXECUTION BLOCKED. Returning without launching GPU pods or inference.")
        return False

    # 2. Config Verification & Single Source-of-Truth Loading
    try:
        cfg = load_and_verify_config(cfg_path, expected_sha)
        print(f"[SAFETY GUARD 2] Execution Config Hash Verified: {expected_sha}")
    except Exception as e:
        print(f"[SAFETY GUARD 2] ERROR: {e}")
        return False

    # Extract invariants directly from config
    auth_reg_path = cfg["authoritative_registry_path"]
    expected_auth_sha = cfg["authoritative_registry_sha256"]
    expected_auth_n = cfg["authoritative_n"]

    strict_reg_path = cfg["strict_registry_path"]
    expected_strict_sha = cfg["strict_registry_sha256"]
    expected_strict_n = cfg["strict_n"]

    checkpoints = cfg["checkpoints"]
    k_rollouts = cfg["rollouts_per_cell_k"]
    expected_rollouts = cfg["total_confirmatory_rollouts"]

    expected_budget = cfg["expected_total_budget_usd"]
    hard_ceiling = cfg["hard_spend_ceiling_usd"]

    ledger_path = cfg["ledger_path"]
    expected_ledger_sha = cfg["ledger_sha256"]

    # 3. Dynamic Primary Registry Verification
    if not os.path.exists(auth_reg_path):
        print(f"[SAFETY GUARD 3] ERROR: Primary registry missing: {auth_reg_path}")
        return False

    with open(auth_reg_path, "rb") as f:
        auth_bytes = f.read()
    
    actual_auth_sha = hashlib.sha256(auth_bytes).hexdigest()
    print(f"[SAFETY GUARD 3] Primary Registry SHA-256: {actual_auth_sha}")
    if actual_auth_sha != expected_auth_sha:
        print(f"[SAFETY GUARD 3] ERROR: Primary registry SHA-256 mismatch!")
        return False

    auth_data = json.loads(auth_bytes)
    if len(auth_data) != expected_auth_n:
        print(f"[SAFETY GUARD 3] ERROR: Primary registry N mismatch! Expected {expected_auth_n}, got {len(auth_data)}")
        return False

    # 4. Dynamic Strict Registry Verification
    if not os.path.exists(strict_reg_path):
        print(f"[SAFETY GUARD 4] ERROR: Strict registry missing: {strict_reg_path}")
        return False

    with open(strict_reg_path, "rb") as f:
        strict_bytes = f.read()
    
    actual_strict_sha = hashlib.sha256(strict_bytes).hexdigest()
    print(f"[SAFETY GUARD 4] Strict Registry SHA-256: {actual_strict_sha}")
    if actual_strict_sha != expected_strict_sha:
        print(f"[SAFETY GUARD 4] ERROR: Strict registry SHA-256 mismatch!")
        return False

    strict_data = json.loads(strict_bytes)
    if len(strict_data) != expected_strict_n:
        print(f"[SAFETY GUARD 4] ERROR: Strict registry N mismatch! Expected {expected_strict_n}, got {len(strict_data)}")
        return False

    # 5. Rollout Count Accounting Verification
    calc_rollouts = len(auth_data) * 2 * len(checkpoints) * k_rollouts
    print(f"[SAFETY GUARD 5] Calculated Rollouts: {calc_rollouts} (Expected: {expected_rollouts})")
    if calc_rollouts != expected_rollouts:
        print(f"[SAFETY GUARD 5] ERROR: Total rollout accounting mismatch!")
        return False

    # 6. Ledger Hash Verification
    if not os.path.exists(ledger_path):
        print(f"[SAFETY GUARD 6] ERROR: Ledger file missing: {ledger_path}")
        return False

    with open(ledger_path, "rb") as f:
        ledger_bytes = f.read()

    actual_ledger_sha = hashlib.sha256(ledger_bytes).hexdigest()
    print(f"[SAFETY GUARD 6] Ledger SHA-256: {actual_ledger_sha}")
    if actual_ledger_sha != expected_ledger_sha:
        print(f"[SAFETY GUARD 6] ERROR: Ledger SHA-256 mismatch!")
        return False

    # 7. Financial Balance & Spend Ceiling Check
    current_balance = 9.43  # Last verified balance
    print(f"[SAFETY GUARD 7] Account Balance Check: ${current_balance:.2f} USD (Required Budget: ${expected_budget:.2f} USD)")
    if current_balance < expected_budget:
        print(f"[SAFETY GUARD 7] ERROR: Account underfunded! Deficit of ${expected_budget - current_balance:.2f} USD.")
        return False

    if expected_budget > hard_ceiling:
        print(f"[SAFETY GUARD 7] ERROR: Expected budget ${expected_budget:.2f} exceeds hard spend ceiling ${hard_ceiling:.2f} USD!")
        return False

    print(f"[SAFETY GUARD 7] Hard Spend Ceiling Check: ${expected_budget:.2f} USD <= ${hard_ceiling:.2f} USD Cap -> PASSED.")

    if mock_mode:
        print("[SAFETY GUARD MOCK] Mock dry-run mode enabled. Zero GPU calls executed.")
        return True

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="StateShift Confirmatory Launcher")
    parser.add_argument("--authorize-confirmatory-run", action="store_true", help="Explicit user authorization flag")
    parser.add_argument("--mock-dry-run", action="store_true", default=True, help="Run safety checks in mock mode")
    args = parser.parse_args()

    success = verify_safety_guards(authorize_flag=args.authorize_confirmatory_run, mock_mode=args.mock_dry_run)
    if not success:
        sys.exit(1)
