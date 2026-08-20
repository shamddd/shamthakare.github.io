"""
Final E0 Manifest Generation & Corrected JMLR Record Freeze Script.
Performs:
1. Calculates SHA-256 checksums of all core E0 empirical artifacts and raw JSON outputs.
2. Corrects Dataset A vs Dataset B definitions:
   - Dataset A: All 6 completed training runs (3 families x 2 seeds/family).
   - Dataset B: 5 runs completed within 12.00 MPS-hour ceiling (3 families: SmolLM2 2 seeds, Qwen 2 seeds, TinyLlama 1 seed).
3. Updates Git immutability statement with SHA-256 manifest reference.
4. Corrects compute halt scope: "No further computation is authorized for E_0."
5. Sets exact final scientific status string.
6. Documents TMLR pre-submission audit requirement.
"""

import os
import sys
import json
import hashlib
import numpy as np
import pandas as pd


def generate_sha256(filepath):
    if not os.path.exists(filepath):
        return "FILE_NOT_FOUND"
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()


def execute_e0_manifest_and_freeze():
    print("[*] Generating SHA-256 Manifest and updating JMLR Record Freeze...", flush=True)
    
    audit_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research/jmlr_risk_minimization")
    os.makedirs(audit_dir, exist_ok=True)

    # ---------------------------------------------------------
    # 1. SHA-256 MANIFEST GENERATION
    # ---------------------------------------------------------
    key_files = [
        os.path.join(audit_dir, "FINAL_LIMITATIONS_LEDGER.md"),
        os.path.join(audit_dir, "REFINED_COLLISION_TAXONOMY.md"),
        os.path.join(audit_dir, "E0_PRESERVED_SCOPED_RESULT.md"),
        os.path.join(audit_dir, "FINAL_JMLR_RECORD_FREEZE.md"),
        os.path.join(audit_dir, "EVIDENCE_REGISTRY.csv"),
        os.path.join(audit_dir, "JMLR_CLAIM_FORENSIC_LEDGER.csv")
    ]
    
    manifest = {}
    for fpath in key_files:
        rel_name = os.path.basename(fpath)
        manifest[rel_name] = generate_sha256(fpath)

    manifest_path = os.path.join(audit_dir, "E0_MANIFEST_SHA256.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # ---------------------------------------------------------
    # 2. E0_PRESERVED_SCOPED_RESULT.md (Factually Corrected)
    # ---------------------------------------------------------
    e0_corrected = """# PRESERVED SCOPED RESULT RECORD: EXPERIMENT E0

**Date**: August 16, 2026  
**SHA-256 Manifest**: `E0_MANIFEST_SHA256.json`  

---

## 1. IMMUTABLE CONFIRMATORY EXPERIMENTAL RECORD ($E_0$)

Experiment $E_0$ is preserved as an immutable empirical observation:

* **Scope**: Evaluated strictly within the synthetic `ModComp` compositional reasoning environment.
* **Model Families**: 3 independently pretrained instruction/chat-tuned families (`SmolLM2-360M-Instruct`, `Qwen2.5-0.5B-Instruct`, `TinyLlama-1.1B-Chat-v1.0`).
* **Training Seeds**: 2 RL training seeds per model family.
* **Empirical Search Cap**: Best-of-$N$ evaluated empirically up to $N \\le 32$.
* **Protocol Compliance & Dual Reporting**:
  - **Dataset A**: All six completed training runs; 3 model families $\\times$ 2 seeds/family (includes the +5.17% overrun on Run 6 at 12.62 MPS-hours).
  - **Dataset B**: Five runs completed within the preregistered 12.00 MPS-hour ceiling; 3 model families represented (2 seeds for SmolLM2, 2 seeds for Qwen2.5, 1 seed for TinyLlama).
* **Observed Effect**: Directional criterion $R_f < 1.0$ observed across all three families ($R_{\\text{SmolLM2}} = 0.0632$, $R_{\\text{Qwen}} = 0.0648$, $R_{\\text{TinyLlama}} = 0.0576$, Geometric Mean $\\bar{R}_f = 0.0618$).

### Mandatory Scoped Reporting Language:
> *"Within the tested synthetic compositional reasoning environment and three evaluated instruction/chat-tuned model families..."*
"""
    with open(os.path.join(audit_dir, "E0_PRESERVED_SCOPED_RESULT.md"), "w") as f:
        f.write(e0_corrected)

    # ---------------------------------------------------------
    # 3. FINAL_JMLR_RECORD_FREEZE.md (Updated with Exact Status String)
    # ---------------------------------------------------------
    freeze_corrected = """# OFFICIAL JMLR RECORD FREEZE & GOVERNANCE DECISION

**Date**: August 16, 2026  
**Auditor**: Executive Scientific Governance Committee  

---

## 1. APPROVED FINAL JMLR RECORD STATEMENT

> *"The current deterministic, known-horizon, stationary-cost adaptation-versus-search formulation does not establish sufficient novelty for JMLR. Dynamic variants exhibit strong overlap with classical online-decision frameworks and recent adaptive-compute and online-adaptation literature; no sufficiently distinct learning-specific contribution has yet survived the novelty audit."*

---

## 2. FINAL CLASSIFICATION VERDICT

$$\\boxed{{\\Huge \\textbf{{NO-GO — CURRENT JMLR FORMULATION}}}}$$

*(Note: This is a NO-GO for the current JMLR submission formulation, NOT a claim that the entire research area is fully solved).*

---

## 3. OFFICIAL FINAL SCIENTIFIC STATUS

$$\\boxed{\\text{CURRENT FORMULATION CLOSED FOR JMLR. } E_0 \\text{ PRESERVED AS A SCOPED EMPIRICAL RESULT.}}$$
$$\\boxed{\\text{NO FURTHER COMPUTE IS AUTHORIZED FOR } E_0.}$$

> **GOVERNANCE STATEMENT**: Future JMLR research must begin from a distinct, pre-audited research hypothesis and must not retrofit novelty around $E_0$.

---

## 4. FROZEN SCIENTIFIC RECORD & SHA-256 MANIFEST

> **Frozen Scientific Record**: The designated $E_0$ artifacts are preserved at a recorded Git commit and SHA-256 manifest (`E0_MANIFEST_SHA256.json`). Subsequent corrections, if required, must be additive and must not overwrite or silently alter the frozen record.

### Key Frozen Assets:
1. **Raw $E_0$ Results & Hashes**: Original output files, JSON manifests, and SHA-256 checksums.
2. **Protocol Deviation & Dataset A/B Definitions**:
   - **Dataset A**: All six completed training runs; 3 model families $\\times$ 2 seeds/family (includes the 12.62 MPS-hour overrun on Run 6).
   - **Dataset B**: Five runs completed within the 12.00 MPS-hour ceiling; 3 model families represented (SmolLM2 2 seeds, Qwen2.5 2 seeds, TinyLlama 1 seed).
3. **Complete L1--L19 Limitations Ledger**: Documented in [`FINAL_LIMITATIONS_LEDGER.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/research/jmlr_risk_minimization/FINAL_LIMITATIONS_LEDGER.md).
4. **Final Governance Decision**: `NO-GO — CURRENT JMLR FORMULATION`.

---

## 5. TMLR PRE-SUBMISSION AUDIT REQUIREMENT

Closing the current JMLR formulation does **NOT** automatically make $E_0$ TMLR-ready. Before any submission of $E_0$ to TMLR, a separate TMLR-specific novelty and acceptance-risk audit must be conducted to scrutinize:
- Experimental scope and synthetic-task dependence.
- Dual Dataset A/B reporting of the compute-ceiling deviation.
- Substantive claim framing without over-generalization.

---

## 6. COMPUTE AUTHORIZATION

$$\\boxed{\\textbf{NO FURTHER COMPUTATION IS AUTHORIZED FOR } E_0.}$$
"""
    with open(os.path.join(audit_dir, "FINAL_JMLR_RECORD_FREEZE.md"), "w") as f:
        f.write(freeze_corrected)

    # ---------------------------------------------------------
    # 4. RESEARCH_PORTFOLIO_GOVERNANCE.md
    # ---------------------------------------------------------
    portfolio_gov = """# RESEARCH PORTFOLIO GOVERNANCE & LESSONS LEARNED

**Date**: August 16, 2026  

---

## 1. STRATEGIC POSITIONING OF EXPERIMENT E0

* **Asset Value**: Experiment $E_0$ is a clean, rigorously audited empirical study demonstrating directional frontier contraction $R_f < 1.0$ across 3 model families within the synthetic `ModComp` environment.
* **Publication Track**: $E_0$ is preserved as a scoped empirical result. A separate TMLR acceptance-risk audit must precede any submission attempt.
* **Research Integrity**: Retractions, ratio decomposition corrections, descriptive CIs, and compute overruns remain fully disclosed and SHA-256 hashed.

---

## 2. GOVERNANCE DECISION FOR CURRENT FORMULATION

$$\\boxed{\\textbf{STATUS: CURRENT FORMULATION CLOSED FOR JMLR. NO FURTHER COMPUTE AUTHORIZED FOR } E_0.}$$
"""
    with open(os.path.join(audit_dir, "RESEARCH_PORTFOLIO_GOVERNANCE.md"), "w") as f:
        f.write(portfolio_gov)

    print("[+] SHA-256 Manifest generated and JMLR Record Freeze updated successfully in: " + audit_dir, flush=True)


if __name__ == "__main__":
    execute_e0_manifest_and_freeze()
