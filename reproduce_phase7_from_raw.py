import os, json, hashlib, numpy as np, pandas as pd

raw_dir = 'artifacts/stateshift_v3/raw'
arms = ['R', 'C', 'S', 'A1', 'A2', 'P', 'D']
checkpoints = [0, 256]

results = {}
for arm in arms:
    results[arm] = {}
    for ckpt in checkpoints:
        fpath = os.path.join(raw_dir, f'gsm8k_{arm}_{ckpt}.jsonl')
        with open(fpath, 'r', encoding='utf-8') as f:
            rows = [json.loads(line) for line in f]
        results[arm][ckpt] = sum(r['verifier_result'] for r in rows) / len(rows)

g_R = results['R'][256] - results['R'][0]
g_C = results['C'][256] - results['C'][0]
gamma_RC = g_R - g_C
print(f'Reproduced Gamma_256_R_C: {gamma_RC:+.4f}')
