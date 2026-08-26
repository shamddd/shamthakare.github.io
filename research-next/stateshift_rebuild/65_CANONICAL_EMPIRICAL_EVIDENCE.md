# CANONICAL EMPIRICAL EVIDENCE MANIFEST

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Verification Date**: `2026-08-27T00:17:00+05:30` (IST)  

---

## 1. Verified Raw Empirical Evidence (Established Baseline)

Only the following data are physically verified from raw byte-level model rollout storage:

### A. Study A Endpoint Interaction Dataset
* **File Path**: `artifacts/endpoint/controlled_endpoint_outcomes.csv` ($2,366,349$ bytes)
* **SHA-256 Hash**: `49549bbd73349bb0e1879603bdbeb04c4a8617ab85d0b31323cfeb188a5c6139`
* **Raw Model Generations**: **$29,056$ empirical rollouts** ($N=454, K=16$, Arms R & C at $t=0, 256$)
* **Primary Interaction Contrast ($\Gamma_{256}$)**: **$+0.1176$** ($95\%$ Problem-Blocked Bootstrap CI $[+0.0955, +0.1400]$, $p < 0.0001$)
* **Strict Subgroup ($\Gamma_{256,\text{Strict}}$)**: **$+0.1160$** ($N_{\text{Strict}}=388$, $95\%$ CI $[+0.0913, +0.1408]$)

### B. Study A Trajectory Dataset
* **File Path**: `artifacts/trajectory/intermediate_rollouts.jsonl` ($1,643,568$ bytes)
* **SHA-256 Hash**: `26a9c82989486d35f7b5dd172a9410222c3affb647bd253575f2f706f3ebe979`
* **Raw Model Generations**: **$7,264$ empirical rollouts** ($N=454, K=2$, Arms R & C at $t=32, 96, 160, 224$)
* **Earliest Contrast ($\Gamma_{32}$)**: **$+0.0333$** ($95\%$ Multiplicity CI $[+0.0011, +0.0655]$)

### C. Study B Natural Recovery Dataset
* **File Path**: `artifacts/natural_recovery/natural_error_episodes.csv` ($44,577$ bytes)
* **Raw Model Generations**: **$3,200$ unprompted empirical rollouts** ($N=200, K=16$ at $t=256$)
* **Natural Error Incidence ($\text{NEI}$)**: **$18.19\%$** ($582 / 3200$ rollouts)
* **Conditional Natural Recovery Rate ($\text{NRR}$)**: **$30.93\%$** ($180 / 582$ error episodes, $95\%$ CI $[27.19\%, 34.82\%]$)

---

## 2. Explicit List of Unestablished / Non-Empirical Claims

The following claims are **NOT EMPIRICALLY ESTABLISHED** and represent historical diagnostic simulation artifacts:
* Arms S (Shuffled), A1 (Same-Problem Alt Error), A2 (Other-Problem Error), P (Valid Irrelevant Math), and D (Direct Benchmark) as empirical model rollouts.
* 56,896 prospective raw model generations.
* GATE 6A prospective confirmation.

*Signed by Lead Statistician & Scientific Integrity Auditor*
