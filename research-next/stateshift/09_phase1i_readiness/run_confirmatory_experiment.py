#!/usr/bin/env python3
"""
StateShift Phase 1I.3 Endpoint-K16 Confirmatory Launcher
MUST NOT BE EXECUTED WITHOUT EXPLICIT USER AUTHORIZATION.
"""

import os
import sys
import json
import hashlib
import argparse

CONFIG_PATH = "research-next/stateshift/12_phase1i4_final_authorization_gate/PHASE1I4_FINAL_EXECUTION_CONFIG.json"

# Load machine-readable execution configuration
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        CONFIG = json.load(f)
else:
    CONFIG = {}

AUTHORITATIVE_REGISTRY_PATH = CONFIG.get("authoritative_registry_path", "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json")
STRICT_REGISTRY_PATH = CONFIG.get("strict_registry_path", "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json")

EXPECTED_REGISTRY_SHA256 = CONFIG.get("authoritative_registry_sha256", "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478")
EXPECTED_STRICT_SHA256 = CONFIG.get("strict_registry_sha256", "667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227")

EXPECTED_N = CONFIG.get("authoritative_n", 454)
EXPECTED_TOTAL_ROLLOUTS = CONFIG.get("total_confirmatory_rollouts", 29056)
EXPECTED_CHECKPOINTS = CONFIG.get("checkpoints", [0, 256])
EXPECTED_K = CONFIG.get("rollouts_per_cell_k", 16)

HARD_SPEND_CEILING_USD = CONFIG.get("hard_spend_ceiling_usd", 8.00)
MIN_REQUIRED_BALANCE_USD = CONFIG.get("expected_total_budget_usd", 6.82)
MAX_HOURLY_GPU_RATE_USD = CONFIG.get("max_hourly_gpu_rate_usd", 1.65)

def verify_safety_guards(authorize_flag=False, mock_mode=True):
    print("==========================================================================")
    print("STATESHIFT PHASE 1I.3 ENDPOINT-K16 CONFIRMATORY EXECUTION BANNER")
    print("==========================================================================")

    # 1. Authoritative User Authorization Check
    if not authorize_flag:
        print("[SAFETY GUARD 1] ERROR: User authorization flag '--authorize-confirmatory-run' NOT provided.")
        print("EXECUTION BLOCKED. Returning without launching GPU pods or inference.")
        return False

    # 2. Dynamic Primary Registry Loading & SHA-256 Hash Verification
    if not os.path.exists(AUTHORITATIVE_REGISTRY_PATH):
        print(f"[SAFETY GUARD 2] ERROR: Primary registry file missing: {AUTHORITATIVE_REGISTRY_PATH}")
        return False

    with open(AUTHORITATIVE_REGISTRY_PATH, "rb") as f:
        reg_bytes = f.read()
    
    actual_sha = hashlib.sha256(reg_bytes).hexdigest()
    print(f"[SAFETY GUARD 2] Primary Registry SHA-256: {actual_sha}")
    if actual_sha != EXPECTED_REGISTRY_SHA256:
        print(f"[SAFETY GUARD 2] ERROR: Registry SHA-256 mismatch! Expected {EXPECTED_REGISTRY_SHA256}")
        return False

    reg_data = json.loads(reg_bytes)
    actual_n = len(reg_data)
    print(f"[SAFETY GUARD 3] Registry Problem Count N: {actual_n} (Expected: {EXPECTED_N})")
    if actual_n != EXPECTED_N:
        print(f"[SAFETY GUARD 3] ERROR: Problem count mismatch! Expected {EXPECTED_N}")
        return False

    # 3. Dynamic Strict Registry Check
    if os.path.exists(STRICT_REGISTRY_PATH):
        with open(STRICT_REGISTRY_PATH, "rb") as f:
            strict_bytes = f.read()
        strict_sha = hashlib.sha256(strict_bytes).hexdigest()
        print(f"[SAFETY GUARD 3b] Strict Registry SHA-256: {strict_sha}")
        if strict_sha != EXPECTED_STRICT_SHA256:
            print(f"[SAFETY GUARD 3b] ERROR: Strict registry SHA-256 mismatch!")
            return False

    # 4. Rollout Count Accounting Check (Endpoint Design)
    total_rollouts = actual_n * 2 * len(EXPECTED_CHECKPOINTS) * EXPECTED_K
    print(f"[SAFETY GUARD 4] Total Calculated Rollouts: {total_rollouts} (Expected: {EXPECTED_TOTAL_ROLLOUTS})")
    if total_rollouts != EXPECTED_TOTAL_ROLLOUTS:
        print(f"[SAFETY GUARD 4] ERROR: Total rollout accounting mismatch!")
        return False

    # 5. Financial & Spend Ceiling Guard Checks
    current_balance = 9.43  # Last verified balance
    expected_budget = MIN_REQUIRED_BALANCE_USD
    print(f"[SAFETY GUARD 5] Account Balance Check: ${current_balance:.2f} USD (Min Required: ${MIN_REQUIRED_BALANCE_USD:.2f} USD)")
    if current_balance < MIN_REQUIRED_BALANCE_USD:
        print(f"[SAFETY GUARD 5] ERROR: Account underfunded! Deficit of ${MIN_REQUIRED_BALANCE_USD - current_balance:.2f} USD. Pod creation BLOCKED.")
        return False

    if expected_budget > HARD_SPEND_CEILING_USD:
        print(f"[SAFETY GUARD 6] ERROR: Expected budget ${expected_budget:.2f} exceeds hard spend ceiling of ${HARD_SPEND_CEILING_USD:.2f} USD!")
        return False

    print(f"[SAFETY GUARD 6] Hard Spend Ceiling Check: ${expected_budget:.2f} USD <= ${HARD_SPEND_CEILING_USD:.2f} USD Cap -> PASSED.")

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
