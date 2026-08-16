import json, os, numpy as np

raw_file = "/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026/09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl"
records = [json.loads(line) for line in open(raw_file) if line.strip()]
grouped = {}
for r in records:
    k = (r["problem_id"], r["recovery_or_control"], r["policy_id"])
    grouped.setdefault(k, []).append(1 if r["primitive_success"] else 0)

cell_means = {k: np.mean(v) for k, v in grouped.items()}
problems = sorted(list(set(r["problem_id"] for r in records)))

diff_rec, diff_con = [], []
for pid in problems:
    sr_i = cell_means.get((pid, "RECOVERY", "Qwen/Qwen2.5-Math-1.5B-Instruct"), 0.0)
    sr_b = cell_means.get((pid, "RECOVERY", "Qwen/Qwen2.5-Math-1.5B"), 0.0)
    sc_i = cell_means.get((pid, "CONTROL", "Qwen/Qwen2.5-Math-1.5B-Instruct"), 0.0)
    sc_b = cell_means.get((pid, "CONTROL", "Qwen/Qwen2.5-Math-1.5B"), 0.0)
    diff_rec.append(sr_i - sr_b)
    diff_con.append(sc_i - sc_b)

d_rec = np.mean(diff_rec) - np.mean(diff_con)
assert abs(d_rec - -0.11000000000000004) < 1e-6, "Independent analysis mismatch!"
print("[+] Independent reconstruction audit passed 100%.")
