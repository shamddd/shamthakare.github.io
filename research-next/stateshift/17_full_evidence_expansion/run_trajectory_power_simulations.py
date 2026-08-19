#!/usr/bin/env python3
"""
Phase 2 Stage A — Trajectory Power Analysis Monte Carlo Simulation Engine
Runs B=10,000 simulation replicates per candidate K across 10 trajectory scenarios.
"""

import numpy as np
import pandas as pd
import json, os

np.random.seed(42)

K_candidates = [16, 24, 32, 48, 64]
N_problems = 454
checkpoints = [0, 32, 64, 96, 128, 160, 192, 224, 256]
n_ckpts = len(checkpoints)
B_reps = 10000

# Base standard deviation per problem contrast Y_i at K repeats
# Var(Y_bar_R - Y_bar_C) = (p_R(1-p_R) + p_C(1-p_C)) / K
# Around p ~ 0.5, p(1-p) ~ 0.25 -> Var ~ 0.5/K -> SD_problem ~ sqrt(0.5/K)
# For N=454, SE_Gamma = sqrt(Var_problem / N) = sqrt(0.5 / (N * K))

# 10 Scenarios:
scenarios = {
    "A_strictly_increasing": np.linspace(0.0, 0.1176, 9),
    "B_early_plateau": np.array([0.0, 0.05, 0.09, 0.11, 0.115, 0.116, 0.117, 0.1175, 0.1176]),
    "C_late_emergence": np.array([0.0, 0.005, 0.01, 0.015, 0.02, 0.04, 0.07, 0.095, 0.1176]),
    "D_hump_shaped": np.array([0.0, 0.04, 0.09, 0.14, 0.16, 0.15, 0.13, 0.12, 0.1176]),
    "E_increase_then_decline": np.array([0.0, 0.05, 0.10, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02]),
    "F_local_max": np.array([0.0, 0.03, 0.07, 0.12, 0.09, 0.10, 0.11, 0.115, 0.1176]),
    "G_local_min": np.array([0.0, 0.04, 0.03, 0.02, 0.05, 0.08, 0.10, 0.11, 0.1176]),
    "H_two_stage": np.array([0.0, 0.04, 0.045, 0.05, 0.052, 0.09, 0.11, 0.115, 0.1176]),
    "I_flat_null": np.zeros(9),
    "J_noisy_monotonic": np.array([0.0, 0.015, 0.028, 0.045, 0.060, 0.072, 0.088, 0.102, 0.1176])
}

results = []

for K in K_candidates:
    se_point = np.sqrt(0.5 / (N_problems * K))
    
    # 7 intermediate checkpoints evaluate 7 x 2 x K x 454 = 6,356 * K rollouts
    total_rollouts_intermediate = 7 * 2 * K * N_problems
    gpu_hours = total_rollouts_intermediate / 8116.0  # throughput ~ 8,116 rollouts/hr
    cost_usd = gpu_hours * 1.59  # $1.59/hr A100 rate
    
    for sc_name, true_vector in scenarios.items():
        # Monte Carlo Simulation of estimated Gamma_t vectors
        # Shape: (B_reps, 9)
        noise = np.random.normal(0.0, se_point, size=(B_reps, 9))
        noise[:, 0] = 0.0  # Gamma_0 = 0 fixed
        sim_gamma = true_vector + noise
        
        # Pointwise CI width (1.96 * 2 * se)
        ci_width = 2 * 1.96 * se_point
        
        # Monotonicity check (diffs >= -0.005)
        diffs = sim_gamma[:, 1:] - sim_gamma[:, :-1]
        is_monotonic = np.all(diffs >= -0.005, axis=1)
        
        monotonicity_detect_rate = np.mean(is_monotonic)
        
        # False reversal check (diffs < -0.02)
        has_reversal = np.any(diffs < -0.02, axis=1)
        reversal_rate = np.mean(has_reversal)
        
        results.append({
            "K": K,
            "scenario": sc_name,
            "se_gamma_t": round(se_point, 4),
            "ci_width_95": round(ci_width, 4),
            "monotonicity_rate": round(float(monotonicity_detect_rate), 4),
            "reversal_rate": round(float(reversal_rate), 4),
            "rollouts_intermediate": total_rollouts_intermediate,
            "gpu_hours": round(gpu_hours, 2),
            "cost_usd": round(cost_usd, 2)
        })

df_res = pd.DataFrame(results)

out_path = "research-next/stateshift/17_full_evidence_expansion/trajectory_power_simulations.csv"
df_res.to_csv(out_path, index=False)
print("Simulation complete. Saved to:", out_path)

# Summary table per K for scenario A (strictly increasing)
df_sc_a = df_res[df_res["scenario"] == "A_strictly_increasing"]
print("\nPower Summary for Scenario A (Strictly Increasing):")
print(df_sc_a[["K", "se_gamma_t", "ci_width_95", "monotonicity_rate", "reversal_rate", "cost_usd"]].to_string(index=False))
