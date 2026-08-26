#!/usr/bin/env python3
"""
Provenance Manifest Generator for StateShift Phase 8
Author: Sham Satish Thakare
"""

import os, sys, json, hashlib, datetime, subprocess

def get_git_sha():
    try:
        return subprocess.check_output('git rev-parse HEAD', shell=True, text=True).strip()
    except Exception:
        return 'UNKNOWN'

def main():
    manifest = {
        'git_commit_sha': get_git_sha(),
        'base_model': 'Qwen/Qwen2.5-7B',
        'post_trained_model': 'UWNSL/Qwen2.5-7B-deepscaler',
        'target_dataset': 'GSM8K_Test',
        'N_problems': 500,
        'K_depth': 16,
        'arms': ['R', 'C', 'S', 'A1', 'A2', 'P', 'D'],
        'expected_total_rollouts': 112000,
        'provenance_generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    
    out_path = 'research-next/stateshift_rebuild/90_CONFIRMATORY_PROVENANCE_MANIFEST.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(f"Provenance manifest written to {out_path}")

if __name__ == "__main__":
    main()
