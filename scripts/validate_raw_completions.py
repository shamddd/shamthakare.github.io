#!/usr/bin/env python3
"""
Strengthened Raw Completion Validator for StateShift Phase 8
Author: Sham Satish Thakare
"""

import os, sys, json, argparse

def validate_raw_dir(raw_dir, expected_total=112000, allow_partial=False):
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
                if allow_partial:
                    print(f"PARTIAL VALIDATION NOTICE: Missing file {fname} (allowed under --allow-partial)")
                    continue
                else:
                    print(f"VALIDATION FAILED: Missing expected file {fpath}")
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
                    
                    # Validate required fields
                    required_fields = ['problem_id', 'arm', 'checkpoint', 'rollout_index', 'raw_completion', 'parsed_answer', 'verifier_result', 'empirical_status']
                    for field in required_fields:
                        if field not in data:
                            print(f"VALIDATION FAILED: Missing required field '{field}' in {fname} line {line_idx+1}")
                            return False
                    
                    # Validate arm & checkpoint alignment
                    if data['arm'] != arm:
                        print(f"VALIDATION FAILED: Arm mismatch in {fname} line {line_idx+1}: {data['arm']} != {arm}")
                        return False
                    if data['checkpoint'] != ckpt:
                        print(f"VALIDATION FAILED: Checkpoint mismatch in {fname} line {line_idx+1}: {data['checkpoint']} != {ckpt}")
                        return False
                    
                    # Reject synthetic test fixtures
                    if data.get('empirical_status') != 'RAW_MODEL_INFERENCE':
                        print(f"VALIDATION FAILED: Non-empirical status '{data.get('empirical_status')}' in {fname} line {line_idx+1}")
                        return False

                    # Validate non-empty completion
                    if not str(data['raw_completion']).strip():
                        print(f"VALIDATION FAILED: Empty raw_completion in {fname} line {line_idx+1}")
                        return False
                    
                    key = f"{data['problem_id']}_{data['arm']}_{data['checkpoint']}_k{data['rollout_index']}"
                    if key in unique_keys:
                        print(f"VALIDATION FAILED: Duplicate rollout key '{key}' in {fname} line {line_idx+1}")
                        return False
                    unique_keys.add(key)
                    rows.append(data)
            
            if not allow_partial and len(rows) != 8000:
                print(f"VALIDATION FAILED: File {fname} contains {len(rows)} rows, expected 8,000!")
                return False
            total_rows += len(rows)

    if not allow_partial and total_rows != expected_total:
        print(f"VALIDATION FAILED: Total rows {total_rows} != expected {expected_total}")
        return False

    print(f"VALIDATION SUCCESSFUL! Verified {total_rows} physical raw completion records (allow_partial={allow_partial}).")
    return True

def main():
    parser = argparse.ArgumentParser(description="StateShift Raw Completion Validator")
    parser.add_argument("raw_dir", nargs="?", default="artifacts/stateshift_v3_real/raw")
    parser.add_argument("--allow-partial", action="store_true", help="Allow partial file coverage for resume checks")
    args = parser.parse_args()

    success = validate_raw_dir(args.raw_dir, allow_partial=args.allow_partial)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
