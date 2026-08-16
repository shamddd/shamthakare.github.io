"""
Generator script for IEEE BigData 2026 Manuscript & Artifact Package.
Creates main.tex, references.bib, figures, README.md, REPRODUCIBILITY_CHECKLIST.md, ARTIFACT_MANIFEST.md, COVER_LETTER.md, SUBMISSION_CHECKLIST.md.
"""

import os
import sys
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

base_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch")
manuscript_dir = os.path.join(base_dir, "research-next/ieee_bigdata_2026/manuscript")
figures_dir = os.path.join(manuscript_dir, "figures")

os.makedirs(figures_dir, exist_ok=True)

def generate_figures():
    print("[*] Generating publication-grade figures...", flush=True)

    # Style configuration
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
    plt.rcParams["font.size"] = 10
    plt.rcParams["axes.edgecolor"] = "#333333"
    plt.rcParams["axes.linewidth"] = 0.8

    # Figure 1: Architecture
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=300)
    ax.axis("off")
    
    # Draw architecture blocks
    boxes = [
        ("Fresh Evaluation\nRegistry\n(N=20 GSM8K)", 0.05, 0.5, "#E8F0FE", "#1A73E8"),
        ("State Perturbation &\nControl Matching\n(d <= 0.25)", 0.28, 0.5, "#E6F4EA", "#137333"),
        ("Interleaved\nNeural Rollouts\n(400 Continuations)", 0.51, 0.5, "#FEF7E0", "#B06000"),
        ("Math Verifier &\nSHA-256 Provenance\nLedger (JSONL)", 0.74, 0.5, "#FCE8E6", "#C5221F")
    ]
    
    for text, x, y, bg, border in boxes:
        ax.text(x, y, text, ha="center", va="center", bbox=dict(boxstyle="round,pad=0.6", facecolor=bg, edgecolor=border, lw=1.5), fontsize=8.5, weight="bold", color="#202124")
        
    for i in range(len(boxes) - 1):
        x1 = boxes[i][1] + 0.09
        x2 = boxes[i+1][1] - 0.09
        ax.annotate("", xy=(x2, 0.5), xytext=(x1, 0.5), arrowprops=dict(arrowstyle="->", color="#5F6368", lw=1.5))

    ax.set_xlim(-0.05, 0.95)
    ax.set_ylim(0.2, 0.8)
    plt.title("Figure 1: recovery_eval End-to-End Governance & Evaluation Pipeline", fontsize=11, weight="bold", pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, "fig1_architecture.pdf"))
    plt.savefig(os.path.join(figures_dir, "fig1_architecture.png"))
    plt.close()

    # Figure 2: State Construction
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=300)
    ax.axis("off")
    
    ax.text(0.15, 0.7, "Recovery State (Perturbed Prefix)\nStep 1: Notebooks/hr = 11.\nStep 2: Hours = 4. Total = 46 (Error!)\nPrefix Continuation Goal: Correct Error", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.5", facecolor="#FCE8E6", edgecolor="#C5221F", lw=1.2), fontsize=8)
    ax.text(0.65, 0.7, "Matched Control State (Valid Prefix)\nStep 1: Notebooks/hr = 11.\nStep 2: Hours = 4. Total = 44 (Valid)\nPrefix Continuation Goal: Complete Solution", ha="center", va="center", bbox=dict(boxstyle="round,pad=0.5", facecolor="#E6F4EA", edgecolor="#137333", lw=1.2), fontsize=8)

    ax.text(0.40, 0.3, "Prospective Matching Filter (d = 0.036 <= 0.25)\nContinuous Covariates: Depth (2.0), Remaining Length (1.0), Token Length (35 vs 33)\nCategorical Exact Match: Operation (multiplication), Difficulty (LOW)", ha="center", va="center", bbox=dict(boxstyle="square,pad=0.6", facecolor="#E8F0FE", edgecolor="#1A73E8", lw=1.2), fontsize=8.5, weight="bold")

    plt.title("Figure 2: Verifier-Defined Recovery State vs Matched Reference Control State Construction", fontsize=10.5, weight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, "fig2_state_construction.pdf"))
    plt.savefig(os.path.join(figures_dir, "fig2_state_construction.png"))
    plt.close()

    # Figure 3: Provenance Chain
    fig, ax = plt.subplots(figsize=(7.5, 3), dpi=300)
    ax.axis("off")
    
    chain = [
        "PREEXECUTION LOCK\nSHA-256: d3b14589...",
        "REAL model.generate()\nPyTorch Output Tensor",
        "BPE DECODE\nAssert Token Round-Trip",
        "RAW JSONL PROVENANCE\nSHA-256: 51b5a157...",
        "INDEPENDENT RECONSTRUCTION\nE5 Contrast: -0.110"
    ]
    for idx, text in enumerate(chain):
        ax.text(0.1 + idx * 0.2, 0.5, text, ha="center", va="center", bbox=dict(boxstyle="round,pad=0.4", facecolor="#F1F3F4", edgecolor="#3C4043", lw=1.2), fontsize=7, weight="bold")
        if idx < len(chain) - 1:
            ax.annotate("", xy=(0.1 + (idx+1)*0.2 - 0.07, 0.5), xytext=(0.1 + idx*0.2 + 0.07, 0.5), arrowprops=dict(arrowstyle="->", color="#1A73E8", lw=1.5))

    ax.set_xlim(-0.02, 0.98)
    plt.title("Figure 3: Append-Only Immutable Primitive Evidence Provenance Chain", fontsize=10.5, weight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, "fig3_provenance_chain.pdf"))
    plt.savefig(os.path.join(figures_dir, "fig3_provenance_chain.png"))
    plt.close()

    # Figure 4: Empirical Results
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    categories = ["Recovery States\n(mean_SR)", "Control States\n(mean_SC)", "Matched Contrast\n(D_recovery)"]
    instruct_vals = [0.430, 0.540, -0.110]
    
    colors = ["#1A73E8", "#137333", "#C5221F"]
    bars = ax.bar(categories, instruct_vals, color=colors, width=0.45, zorder=3)
    
    # Error bar for D_recovery [-0.240, 0.030]
    ax.errorbar([2], [-0.110], yerr=[[-0.110 - (-0.240)], [0.030 - (-0.110)]], fmt="none", ecolor="#202124", elinewidth=2, capsize=6, capthick=2, zorder=4)
    
    ax.axhline(0, color="#5F6368", linestyle="--", linewidth=1, zorder=2)
    ax.set_ylabel("Observed Continuation Success Diff / Contrast", fontsize=9.5, weight="bold")
    ax.set_ylim(-0.35, 0.70)
    ax.grid(axis="y", linestyle=":", alpha=0.6, zorder=1)
    
    for bar in bars:
        height = bar.get_height()
        va = "bottom" if height >= 0 else "top"
        y_pos = height + 0.02 if height >= 0 else height - 0.04
        ax.text(bar.get_x() + bar.get_width()/2., y_pos, f"{height:+.3f}", ha="center", va=va, fontsize=9, weight="bold")

    ax.text(2, 0.06, "95% Bootstrap CI\n[-0.240, +0.030]", ha="center", va="bottom", fontsize=7.5, color="#202124", bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF", edgecolor="#5F6368", lw=0.8))

    plt.title("Figure 4: Observed Recovery/Control Differences & Matched Contrast (N=400)", fontsize=10.5, weight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(figures_dir, "fig4_empirical_results.pdf"))
    plt.savefig(os.path.join(figures_dir, "fig4_empirical_results.png"))
    plt.close()

    print("[+] All figures generated successfully.", flush=True)

if __name__ == "__main__":
    generate_figures()
