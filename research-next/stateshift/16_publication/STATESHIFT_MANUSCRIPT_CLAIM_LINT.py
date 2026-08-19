#!/usr/bin/env python3
"""
Phase 1L.1 Manuscript-Wide Automated Claim Lint Guard
"""

import os, json, hashlib, pandas as pd

PROHIBITED_TERMS = [
    "% acceleration",
    "monotonic improvement",
    "monotonically",
    "emerged at step",
    "emergence at checkpoint",
    "inflection point",
    "local peak",
    "full trajectory",
    "training trajectory shows",
    "natural self-correction"
]

ALLOW_CONTEXT_WORDS = [
    "limitations",
    "future work",
    "not measured",
    "unobserved",
    "prohibited",
    "prohibit",
    "not established",
    "does not establish",
    "not possess",
    "open question",
    "warning",
    "superseded",
    "simulation",
    "does not identify",
    "❌",
    "overclaim"
]

def run_claim_lint():
    print("==========================================================================")
    print("STATESHIFT PHASE 1L.1 MANUSCRIPT-WIDE AUTOMATED CLAIM LINT GUARD")
    print("==========================================================================")
    
    pub_dir = "research-next/stateshift/16_publication"
    violations = []
    files_checked = 0
    
    for f in sorted(os.listdir(pub_dir)):
        if f.endswith(".md"):
            filepath = os.path.join(pub_dir, f)
            files_checked += 1
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                lines = file.readlines()
                for line_idx, line in enumerate(lines, 1):
                    line_lower = line.lower()
                    for term in PROHIBITED_TERMS:
                        if term.lower() in line_lower:
                            # Check if allowed in context
                            is_allowed = any(context.lower() in line_lower for context in ALLOW_CONTEXT_WORDS)
                            if not is_allowed:
                                violations.append((f, line_idx, term, line.strip()))
    
    print(f"Files Checked: {files_checked}")
    print(f"Violations Found: {len(violations)}")
    
    for v in violations:
        print(f"  ❌ Violation in {v[0]}:{v[1]} -> Term: '{v[2]}' | Text: {v[3]}")
    
    assert len(violations) == 0, f"Claim lint failed with {len(violations)} violations"
    
    print("==========================================================================")
    print("CLAIM LINT GUARD STATUS: PASSED (ZERO PROHIBITED OVERCLAIMS)")
    print("==========================================================================")
    return True

if __name__ == "__main__":
    run_claim_lint()
