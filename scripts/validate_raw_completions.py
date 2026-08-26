#!/usr/bin/env python3
"""
Raw Completion Validation Script for StateShift Phase 8
Author: Sham Satish Thakare
"""

import os, sys, json, hashlib

def validate_raw_dir(raw_dir, expected_total=112000):
    if not os.path.exists(raw_dir):
        print(f"VALIDATION FAILED: Raw directory {raw_dir} does not exist!")
        return False

    arms = ['R', 'C', 'S', 'A1', 'A2', 'P', 'D']
    checkpoints = [0, 256]
    
    total_rows = 0
    unique_keys = set()
    
    for arm in arms:
        for ckpt in checkpoints:
            fname = f"gsm8k_{arm}_{ckpt}.jsonl"
            fpath = os.path.join(raw_dir, fname)
            if not os.path.exists(fpath):
                print(f"VALIDATION FAILED: Missing file {fpath}")
                return False
            
            rows = []
            with open(fpath, 'r', encoding='utf-8') as f:
                for line_idx, line in enumerate(f):
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                    except Exception as e:
                        print(f"VALIDATION FAILED: Malformed JSON in {fname} line {line_idx+1}: {e}")
                        return False
                    
                    # Validate fields
                    for field in ['problem_id', 'arm', 'checkpoint', 'rollout_index', 'raw_completion', 'parsed_answer', 'verifier_result']:
                        if field not in data:
                            print(f"VALIDATION FAILED: Missing field {field} in {fname} line {line_idx+1}")
                            return False
                    
                    # Check empty completion
                    if not str(data['raw_completion']).strip():
                        print(f"VALIDATION FAILED: Empty raw_completion in {fname} line {line_idx+1}")
                        return False

                    # Check empirical status
                    if data.get('empirical_status') == 'SYNTHETIC_TEST_FIXTURE':
                        print(f"VALIDATION FAILED: File {fname} contains SYNTHETIC_TEST_FIXTURE records!")
                        return False
                    
                    key = f"{data['problem_id']}_{data['arm']}_{data['checkpoint']}_k{data['rollout_index']}"
                    if key in unique_keys:
                        print(f"VALIDATION FAILED: Duplicate rollout key {key}")
                        return False
                    unique_keys.add(key)
                    rows.append(data)
            
            if len(rows) != 8000:
                print(f"VALIDATION FAILED: File {fname} contains {len(rows)} rows, expected 8,000!")
                return False
            total_rows += len(rows)

    if total_rows != expected_total:
        print(f"VALIDATION FAILED: Total rows {total_rows} != expected {expected_total}")
        return False

    print(f"VALIDATION SUCCESSFUL! All {total_rows} physical raw completion records verified cleanly.")
    return True

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "artifacts/stateshift_v3_real/raw"
    success = validate_raw_dir(target_dir)
    sys.exit(0 if success else 1)
