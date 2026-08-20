import matplotlib.pyplot as plt
import numpy as np
import os

fig_dir = "/Users/shamthakare/.gemini/antigravity/scratch/submission_ieee_tcc/figures"
os.makedirs(fig_dir, exist_ok=True)

# Data from frozen CausalOpsBench experiments
baselines = ['Unconstrained LLM RAG', 'Heuristic Topological Walk', 'TraceMind (Ours)']
top1_acc = [0.0, 41.67, 100.0]
mrr_scores = [0.44, 0.62, 1.00]

plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
fig, ax1 = plt.subplots(figsize=(3.5, 2.5), dpi=300)

bars = ax1.bar(baselines, top1_acc, color=['#EF4444', '#F59E0B', '#10B981'], width=0.5, edgecolor='black', linewidth=0.8)
ax1.set_xlabel('Root-Cause Localization Baseline', fontsize=8, fontweight='bold')
ax1.set_ylabel('Top-1 Accuracy (%)', fontsize=8, fontweight='bold', color='#0F172A')
ax1.tick_params(axis='y', labelsize=7)
ax1.tick_params(axis='x', labelsize=7)
plt.xticks(rotation=15, ha='right')

for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=7, fontweight='bold')

ax1.set_ylim(0, 115)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

plt.title('Top-1 RCA Localization Accuracy on CausalOpsBench', fontsize=8, fontweight='bold', pad=8)
plt.tight_layout()

pdf_path = os.path.join(fig_dir, "mrr_comparison.pdf")
png_path = os.path.join(fig_dir, "mrr_comparison.png")

plt.savefig(pdf_path, format='pdf', bbox_inches='tight')
plt.savefig(png_path, format='png', dpi=600, bbox_inches='tight')

print("Successfully generated figure files at:")
print("  PDF:", pdf_path)
print("  PNG:", png_path)
