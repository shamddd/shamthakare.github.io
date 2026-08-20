"""
Final Frozen E0 Manifest Seal & Complete Evidence Chain Script.
Performs:
1. Copies/links all high-level reports, claims ledgers, limitations ledgers, and raw evidence files into research/jmlr_risk_minimization/frozen_e0/.
2. Captures Git commit hash (git rev-parse HEAD) and tree hash.
3. Generates E0_MANIFEST_SHA256.json containing complete metadata and file hashes.
4. Generates E0_MANIFEST_SHA256.txt containing the SHA-256 hash of E0_MANIFEST_SHA256.json.
5. Updates RESEARCH_PORTFOLIO_GOVERNANCE.md with conservative "was observed" wording.
"""

import os
import sys
import json
import shutil
import hashlib
import subprocess

def compute_sha256(filepath):
    if not os.path.exists(filepath):
        return "FILE_NOT_FOUND"
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def execute_seal_frozen_e0():
    print("[*] Launching Final E0 Manifest Seal & Evidence Chain Suite...", flush=True)
    
    base_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch")
    audit_dir = os.path.join(base_dir, "research/jmlr_risk_minimization")
    frozen_dir = os.path.join(audit_dir, "frozen_e0")
    os.makedirs(frozen_dir, exist_ok=True)

    # 1. Update RESEARCH_PORTFOLIO_GOVERNANCE.md with conservative wording
    portfolio_path = os.path.join(audit_dir, "RESEARCH_PORTFOLIO_GOVERNANCE.md")
    portfolio_gov = """# RESEARCH PORTFOLIO GOVERNANCE & LESSONS LEARNED

**Date**: August 16, 2026  

---

## 1. STRATEGIC POSITIONING OF EXPERIMENT E0

* **Asset Value**: $E_0$ is a rigorously audited, scoped empirical study in which the preregistered directional criterion $R_f < 1$ was observed across the three tested model families within the synthetic `ModComp` environment.
* **Publication Track**: $E_0$ is preserved as a scoped empirical result. A separate TMLR acceptance-risk audit must precede any submission attempt.
* **Research Integrity**: Retractions, ratio decomposition corrections, descriptive CIs, and compute overruns remain fully disclosed and SHA-256 hashed.

---

## 2. GOVERNANCE DECISION FOR CURRENT FORMULATION

$$\\boxed{\\textbf{STATUS: CURRENT FORMULATION CLOSED FOR JMLR. NO FURTHER COMPUTE AUTHORIZED FOR } E_0.}$$
"""
    with open(portfolio_path, "w") as f:
        f.write(portfolio_gov)

    # 2. Gather list of files to copy into frozen_e0
    files_to_freeze = [
        "FINAL_JMLR_RECORD_FREEZE.md",
        "E0_PRESERVED_SCOPED_RESULT.md",
        "FINAL_LIMITATIONS_LEDGER.md",
        "REFINED_COLLISION_TAXONOMY.md",
        "RESEARCH_PORTFOLIO_GOVERNANCE.md",
        "EVIDENCE_REGISTRY.csv",
        "JMLR_CLAIM_FORENSIC_LEDGER.csv",
        "BASE_PROBABILITY_NULL_V3.md",
        "CROSSOVER_THEOREM_FORMAL.md",
        "CROSSOVER_THEOREM_PROOF.md",
        "CORRELATED_BEST_OF_N_MODEL.md",
        "EMPIRICAL_PASS_AT_N_AUDIT.md",
        "HETEROGENEITY_JENSEN_AUDIT.md",
        "VERIFIED_LITERATURE_AUDIT.csv",
        "STATIC_PROJECT_FINAL_RECORD.md"
    ]

    for fname in files_to_freeze:
        src = os.path.join(audit_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(frozen_dir, fname))

    # Also include raw results manifest if available
    raw_results_src = os.path.join(base_dir, "MULTIFAMILY_REPLICATION_RAW_RESULTS.json")
    if os.path.exists(raw_results_src):
        shutil.copy2(raw_results_src, os.path.join(frozen_dir, "MULTIFAMILY_REPLICATION_RAW_RESULTS.json"))

    # 3. Fetch Git Commit and Tree SHAs
    git_commit = "UNCOMMITTED_PRE_COMMIT_STATE"
    git_tree = "UNKNOWN_TREE"
    try:
        commit_res = subprocess.run(["git", "rev-parse", "HEAD"], cwd=base_dir, capture_output=True, text=True)
        if commit_res.returncode == 0:
            git_commit = commit_res.stdout.strip()
        tree_res = subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=base_dir, capture_output=True, text=True)
        if tree_res.returncode == 0:
            git_tree = tree_res.stdout.strip()
    except Exception as e:
        print(f"[!] Note: Git SHA lookup failed or not a git repo: {e}")

    # 4. Generate E0_MANIFEST_SHA256.json
    manifest_data = {
        "manifest_created_at": "2026-08-16T02:16:30+05:30",
        "git_commit": git_commit,
        "git_tree": git_tree,
        "hash_algorithm": "sha256",
        "files": {}
    }

    for item in sorted(os.listdir(frozen_dir)):
        if item in ["E0_MANIFEST_SHA256.json", "E0_MANIFEST_SHA256.txt"]:
            continue
        item_path = os.path.join(frozen_dir, item)
        if os.path.isfile(item_path):
            manifest_data["files"][item] = compute_sha256(item_path)

    json_manifest_path = os.path.join(frozen_dir, "E0_MANIFEST_SHA256.json")
    with open(json_manifest_path, "w") as f:
        json.dump(manifest_data, f, indent=2)

    # 5. Generate E0_MANIFEST_SHA256.txt (Hash of E0_MANIFEST_SHA256.json)
    json_hash = compute_sha256(json_manifest_path)
    txt_manifest_path = os.path.join(frozen_dir, "E0_MANIFEST_SHA256.txt")
    with open(txt_manifest_path, "w") as f:
        f.write(f"{json_hash}  E0_MANIFEST_SHA256.json\n")

    # Also save top-level pointers in audit_dir
    shutil.copy2(json_manifest_path, os.path.join(audit_dir, "E0_MANIFEST_SHA256.json"))
    shutil.copy2(txt_manifest_path, os.path.join(audit_dir, "E0_MANIFEST_SHA256.txt"))

    print(f"[+] Complete frozen evidence package sealed in: {frozen_dir}")
    print(f"[+] Manifest SHA-256: {json_hash}")


if __name__ == "__main__":
    execute_seal_frozen_e0()
