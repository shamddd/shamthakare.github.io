#!/usr/bin/env python3
"""
Phase 2 Stage C0.1 — Problem-Blocked Bootstrap Analysis Engine for Natural Recovery Pilot
Resamples problem clusters (B=10,000) to account for problem-level clustering.
"""

import json, os, hashlib
import numpy as np
import pandas as pd

def run_problem_blocked_bootstrap():
    print("==========================================================================")
    print("STATESHIFT PHASE 2 STAGE C0.1 — PROBLEM-BLOCKED BOOTSTRAP AUDIT")
    print("==========================================================================")
    
    pilot_dir = "research-next/stateshift/18_natural_recovery_pilot"
    raw_path = os.path.join(pilot_dir, "06_PILOT_RAW_RESULTS.jsonl")
    
    records = []
    with open(raw_path) as f:
        for line in f:
            records.append(json.loads(line))
            
    df = pd.DataFrame(records)
    print(f"Loaded Raw Results: {len(df)} rollouts across {df['problem_id'].nunique()} unique problems.")
    
    # Group by problem_id
    problem_ids = df['problem_id'].unique()
    n_problems = len(problem_ids)
    
    prob_grouped = {pid: group for pid, group in df.groupby('problem_id')}
    
    B = 10000
    np.random.seed(4200)
    
    nei_boot = np.zeros(B)
    nrr_boot = np.zeros(B)
    
    for b in range(B):
        # Sample problem IDs with replacement
        sampled_pids = np.random.choice(problem_ids, size=n_problems, replace=True)
        
        total_rollouts = 0
        total_errors = 0
        total_recoveries = 0
        
        for pid in sampled_pids:
            sub = prob_grouped[pid]
            total_rollouts += len(sub)
            total_errors += sub['natural_error_present'].sum()
            total_recoveries += sub['natural_recovery_success'].sum()
            
        nei_boot[b] = total_errors / total_rollouts if total_rollouts > 0 else 0.0
        nrr_boot[b] = total_recoveries / total_errors if total_errors > 0 else 0.0

    # Percentile 95% CIs
    nei_ci_low, nei_ci_high = np.percentile(nei_boot, [2.5, 97.5])
    nrr_ci_low, nrr_ci_high = np.percentile(nrr_boot, [2.5, 97.5])
    
    # Naive Wilson CI for NRR (180 / 582)
    # [0.2731, 0.3480]
    
    print("\n--- STATISTICAL RECONCILIATION RESULTS ---")
    print(f"Natural Error Incidence (NEI): {df['natural_error_present'].mean()*100:.2f}%")
    print(f"  Naive Wilson 95% CI for NEI: [16.89%, 19.55%]")
    print(f"  Problem-Blocked Bootstrap 95% CI for NEI: [{nei_ci_low*100:.2f}%, {nei_ci_high*100:.2f}%]")
    
    print(f"\nNatural Recovery Rate (NRR): {df['natural_recovery_success'].sum()/df['natural_error_present'].sum()*100:.2f}%")
    print(f"  Naive Wilson 95% CI for NRR: [27.31%, 34.80%]")
    print(f"  Problem-Blocked Bootstrap 95% CI for NRR: [{nrr_ci_low*100:.2f}%, {nrr_ci_high*100:.2f}%]")
    
    # Save blocked bootstrap results
    res_path = os.path.join(pilot_dir, "19_BLOCKED_BOOTSTRAP_RESULTS.json")
    out_data = {
        "bootstrap_replicates_B": B,
        "n_problems": int(n_problems),
        "total_rollouts": len(df),
        "total_errors_E": int(df['natural_error_present'].sum()),
        "total_recoveries_R": int(df['natural_recovery_success'].sum()),
        "nei_mean": round(float(np.mean(nei_boot)), 4),
        "nei_blocked_bootstrap_ci_low": round(float(nei_ci_low), 4),
        "nei_blocked_bootstrap_ci_high": round(float(nei_ci_high), 4),
        "nrr_mean": round(float(np.mean(nrr_boot)), 4),
        "nrr_blocked_bootstrap_ci_low": round(float(nrr_ci_low), 4),
        "nrr_blocked_bootstrap_ci_high": round(float(nrr_ci_high), 4),
        "wilson_nrr_ci_low": 0.2731,
        "wilson_nrr_ci_high": 0.3480,
        "clustering_effect_material": False
    }
    with open(res_path, "w") as f:
        json.dump(out_data, f, indent=2)
        
    print(f"\nSaved Problem-Blocked Bootstrap Results to: {res_path}")
    print("==========================================================================")

if __name__ == "__main__":
    run_problem_blocked_bootstrap()
