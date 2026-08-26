# PHASE 5 PROSPECTIVE EXPERIMENTAL PROTOCOL (FROZEN)

**Project**: StateShift Scientific Rebuild — Phase 5  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Protocol Version**: `v2.0-confirmatory`  
**Git Safety Anchor**: `51ca0a71d50fbdd673eb5d594bf987678fd304dc`  
**Freeze Tag**: `stateshift-v2-protocol-frozen`  
**Freeze Timestamp**: `2026-08-26 23:45 UTC`  

---

## 1. Frozen Primary Research Question & Estimand

* **Primary Research Question**:
  > *"Does reinforcement learning post-training produce a recovery-specific capability beyond ordinary improvements in reasoning accuracy?"*

* **Primary Hypothesis ($H_0$ vs $H_1$)**:
  * $H_0: \Gamma_{256}^{\text{spec}} \le 0$
  * $H_1: \Gamma_{256}^{\text{spec}} > 0$ (Two-sided significance test at $\alpha = 0.05$)

* **Primary Estimand ($\Gamma_t^{\text{spec}}$)**:

$$\Gamma_t^{\text{spec}} = (p_{R,t} - p_{R,0}) - (p_{C,t} - p_{C,0})$$

---

## 2. Experimental Specifications

* **Model Lineage**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_X` (Base: `Qwen/Qwen2.5-7B`).
* **Checkpoints**: $t \in \{0, 32, 96, 160, 256\}$ (5 discrete checkpoints for optimal capability trajectory resolution).
* **Sample Size**: $N = 454$ decontaminated `MATH-500` problems.
* **Rollout Depth**: $K = 16$ rollouts per arm/cell per problem ($7,264$ rollouts per arm across $t=0, 256$).
* **Intervention Arms**:
  1. `Arm R` — Recovery (Invalid intermediate step prefix)
  2. `Arm C` — Matched Control (Valid intermediate step prefix)
  3. `Arm S` — Shuffled Reasoning (Linguistically matched reordered step)
  4. `Arm I` — Irrelevant English Prose (Length-matched neutral prose)
  5. `Arm A` — Alternate Math Error (Problem-unrelated math error)
  6. `Arm D` — Direct Decoding (Zero-prefix unprompted benchmark baseline)

---

## 3. Cryptographic Provenance Manifest

| Artifact File | Expected Path | SHA-256 Checksum Hash |
| :--- | :--- | :--- |
| **Problem Partition Registry** | `artifacts/provenance/confirmatory_problem_registry.json` | `5e8f492b...` |
| **Controlled Endpoint Outcomes** | `artifacts/endpoint/controlled_endpoint_outcomes.csv` | `9b3a127f...` |
| **Nine-Checkpoint Trajectory** | `artifacts/trajectory/nine_checkpoint_trajectory.csv` | `1c7e841a...` |
| **Natural Recovery Episodes** | `artifacts/natural_recovery/natural_recovery_episodes.csv` | `4f9d205c...` |

*Signed by Principal Investigator & Scientific Integrity Auditor*
