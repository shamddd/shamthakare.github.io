"""
Security Audit Script for Entire Account Workspace.
Scans all text files for sensitive keys, passwords, tokens, API keys, and CyberChair credentials.
"""

import os
import sys
import re

secret_patterns = [
    (re.compile(r"(?:password|passwd|pwd|secret)\s*[:=]\s*['\"]([^'\"]{4,})['\"]", re.IGNORECASE), "Plaintext Password/Secret"),
    (re.compile(r"p497", re.IGNORECASE), "CyberChair Paper Password Tag"),
    (re.compile(r"hf_[a-zA-Z0-9]{34,}", re.IGNORECASE), "HuggingFace Access Token"),
    (re.compile(r"sk-[a-zA-Z0-9]{32,}", re.IGNORECASE), "OpenAI API Key"),
    (re.compile(r"github_pat_[a-zA-Z0-9]{22,}", re.IGNORECASE), "GitHub Personal Access Token"),
    (re.compile(r"AKIA[0-9A-Z]{16}", re.IGNORECASE), "AWS Access Key ID"),
    (re.compile(r"AIza[0-9A-Za-z-_]{35}", re.IGNORECASE), "Google API Key")
]

ignore_dirs = {".git", ".pytest_cache", "__pycache__", "node_modules", ".next", "venv", ".venv"}

base_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch")

findings = []

for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for fn in files:
        if fn.endswith((".py", ".md", ".json", ".txt", ".yml", ".yaml", ".sh", ".html", ".js", ".ts", ".tsx", ".cff", ".bib", ".tex")):
            fp = os.path.join(root, fn)
            rel_p = os.path.relpath(fp, base_dir)
            try:
                content = open(fp, "r", encoding="utf-8", errors="ignore").read()
                for pattern, name in secret_patterns:
                    matches = pattern.findall(content)
                    if matches:
                        # Exclude self-references in audit scripts or doc examples
                        if "run_security_audit.py" in rel_p or "reconcile_final_hashes_and_audit.py" in rel_p or "verify_references_primary_source.py" in rel_p:
                            continue
                        findings.append((rel_p, name, str(matches[:2])))
            except Exception:
                pass

print("=== GLOBAL SECURITY AUDIT RESULTS ===", flush=True)
if not findings:
    print("[+] ZERO SECRETS OR PASSWORDS DETECTED. ALL REPOSITORIES CLEAN!", flush=True)
else:
    print(f"[!] DETECTED {len(findings)} POTENTIAL SECRETS:", flush=True)
    for p, name, sample in findings:
        print(f"    - {p}: {name} (Sample: {sample})", flush=True)
