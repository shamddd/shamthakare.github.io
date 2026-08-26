# PHASE 7 GENUINE PROSPECTIVE EXPERIMENTAL PROTOCOL (FROZEN)

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Protocol Version**: `v4.0-phase7-gsm8k-confirmatory`  
**Target Dataset**: `GSM8K_Test` ($N_{\text{new}} = 500$ untouched problems)  
**Model Lineage**: `Qwen/Qwen2.5-7B` ($t=0$) vs `UWNSL/Qwen2.5-7B-deepscaler` ($t=256$)  
**Rollout Depth**: $K = 16$ rollouts per arm cell per problem  
**Intervention Arms**: 7 Arms ($R, C, S, A_1, A_2, P, D$)  
**Total Confirmatory Rollouts**: $500 \times 16 \times 7 \times 2 = \mathbf{112,000\ empirical\ rollouts}$  

---

## 1. Frozen Primary Research Question & Estimand

* **Primary Research Question**:
  > *"Does ordinary reasoning-oriented RL post-training produce a disproportionate improvement in continuation from problem-matched invalid reasoning context relative to matched valid and alternative contextual controls?"*

* **Primary Estimand ($\Gamma_{256}^{R:C}$)**:

$$\Gamma_{256}^{R:C} = (p_{R,256} - p_{R,0}) - (p_{C,256} - p_{C,0})$$

---

## 2. Cryptographic Hash Provenance Manifest

| Protocol Artifact | File Path | SHA-256 Checksum Hash |
| :--- | :--- | :--- |
| **New Dataset Registry** | `artifacts/stateshift_v3/provenance/gsm8k_untouched_registry.json` | `f892019a4b82...` |
| **Protocol Specification** | `research-next/stateshift_rebuild/69_PHASE7_PROSPECTIVE_PROTOCOL.md` | `b9102c841a90...` |

*Signed by Principal Investigator & Lead Statistician*
