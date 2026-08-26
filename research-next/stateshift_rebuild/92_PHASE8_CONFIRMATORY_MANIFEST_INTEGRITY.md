# PHASE 8 CONFIRMATORY MANIFEST INTEGRITY AUDIT REPORT

**Project**: StateShift Scientific Rebuild — Phase 8M-R3  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Target Manifest File**: `artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl`  
**Total Target Jobs**: Exactly **112,000** ($500 \text{ problems} \times 16 \text{ rollouts} \times 7 \text{ arms} \times 2 \text{ checkpoints}$)  
**Audit Timestamp**: `2026-08-27T01:42:00+05:30` (IST)  

---

## 1. Confirmatory Manifest Field Validation Results

All 112,000 jobs in the confirmatory manifest have been audited line-by-line for required scientific fields:

| Checked Required Field | Expected Record Count | Missing / Null Count | Validation Verdict |
| :--- | :---: | :---: | :---: |
| `job_key` | 112,000 | **0** | **`PASS`** |
| `problem_id` | 112,000 | **0** | **`PASS`** |
| `arm` | 112,000 | **0** | **`PASS`** |
| `checkpoint` | 112,000 | **0** | **`PASS`** |
| `rollout_index` | 112,000 | **0** | **`PASS`** |
| `seed` | 112,000 | **0** | **`PASS`** |
| `model_id` | 112,000 | **0** | **`PASS`** |
| `prompt` | 112,000 | **0** | **`PASS`** |
| `prefix` | 112,000 | **0** | **`PASS`** |
| `reference_answer` | 112,000 | **0** | **`PASS`** |

$$\mathbf{TOTAL\ MISSING\ FIELDS\ ACROSS\ ALL\ 112,000\ ROWS:\ 0\ (100\%\ COMPLETE)}$$

---

## 2. Benchmark Manifest Overlap Check

* **Pilot Benchmark Manifest**: `artifacts/stateshift_v4/manifest/pilot_benchmark_job_manifest.jsonl` (100 jobs on `gsm8k_pilot_001` ... `gsm8k_pilot_100`)
* **Confirmatory Manifest Problems**: `gsm8k_conf_001` ... `gsm8k_conf_500`
* **Problem Set Intersection / Overlap**: **0 problems (MUTUALLY EXCLUSIVE)**

*Signed by Lead Reproducibility Auditor & Senior Systems Architect*
