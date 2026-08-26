#!/usr/bin/env python3
"""
RunPod GPU Budget & Cost Guard for StateShift Phase 8
Author: Sham Satish Thakare
"""

import sys, time

def check_budget(elapsed_seconds, rate_per_hour_usd=1.69, max_budget_usd=15.0):
    elapsed_hours = elapsed_seconds / 3600.0
    accumulated_cost = elapsed_hours * rate_per_hour_usd
    print(f"Elapsed Time: {elapsed_hours:.2f} hours | Accumulated Cost: ${accumulated_cost:.2f} / ${max_budget_usd:.2f}")
    if accumulated_cost >= max_budget_usd:
        print(f"BUDGET THRESHOLD EXCEEDED (${accumulated_cost:.2f} >= ${max_budget_usd:.2f})! STOPPING INFERENCE.")
        return False
    return True

if __name__ == "__main__":
    elapsed = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    budget_ok = check_budget(elapsed)
    sys.exit(0 if budget_ok else 1)
