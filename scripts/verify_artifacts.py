#!/usr/bin/env python3
"""
Artifact Verification Script.
Asserts regenerated values against frozen scientific source of truth.
"""

import sys, os, pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.reproduce_analysis import reproduce_endpoint, reproduce_trajectory, reproduce_natural_recovery


def main():
    print("VERIFYING STATESHIFT PUBLICATION ARTIFACTS...")
    
    # 1. Endpoint Check
    ep = reproduce_endpoint()
    assert abs(ep["gamma_256"] - 0.1176) < 1e-4, f"Gamma_256 mismatch: {ep['gamma_256']} != 0.1176"
    assert abs(ep["strict_gamma_256"] - 0.1160) < 1e-4, f"Strict Gamma_256 mismatch: {ep['strict_gamma_256']} != 0.1160"
    
    # 2. Trajectory Check
    df_traj, eval_order = reproduce_trajectory()
    gammas = df_traj["gamma_t"].tolist()
    expected_gammas = [0.0000, 0.0333, 0.0337, 0.0774, 0.0748, 0.0598, 0.0976, 0.0950, 0.1176]
    for g, eg in zip(gammas, expected_gammas):
        assert abs(g - eg) < 1e-4, f"Gamma_t mismatch: {g} != {eg}"
        
    assert eval_order["is_order_restricted_supported"] == True, "Order-restricted consistency check failed!"
    
    # 3. Natural Recovery Check
    nr = reproduce_natural_recovery()
    assert abs(nr["nei"] - 18.19) < 0.05, f"NEI mismatch: {nr['nei']} != 18.19"
    assert abs(nr["nrr"] - 30.93) < 0.05, f"NRR mismatch: {nr['nrr']} != 30.93"
    
    print("\nALL ARTIFACT VERIFICATION ASSERTIONS PASSED (100% MATCH TO FROZEN RESULTS).")


if __name__ == "__main__":
    main()
