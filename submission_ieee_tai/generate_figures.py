import matplotlib.pyplot as plt
import numpy as np
import os

fig_dir = "/Users/shamthakare/.gemini/antigravity/scratch/submission_ieee_tai/figures"
os.makedirs(fig_dir, exist_ok=True)

# Data from frozen experiments
protocols = ['Static Raft (R=3)', 'Static Raft (R=5)', 'AdaptiveReplica (Ours)']
p99_latencies = [65.20, 120.48, 13.50]
availability = [98.40, 99.10, 99.97]

# Styling for IEEE TAI (Clean, high contrast, professional)
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
fig, ax1 = plt.subplots(figsize=(3.5, 2.5), dpi=300)

color = '#1E3A8A'
ax1.set_xlabel('Consensus Protocol', fontsize=8, fontweight='bold')
ax1.set_ylabel('Write p99 Latency (ms)', color=color, fontsize=8, fontweight='bold')
bars = ax1.bar(protocols, p99_latencies, color=['#94A3B8', '#64748B', '#2563EB'], width=0.5, edgecolor='black', linewidth=0.8)
ax1.tick_params(axis='y', labelcolor=color, labelsize=7)
ax1.tick_params(axis='x', labelsize=7)
plt.xticks(rotation=15, ha='right')

# Add value labels above bars
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}ms',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=7, fontweight='bold')

ax1.set_ylim(0, 140)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

plt.title('Write p99 Latency under 50ms Fault Injection', fontsize=8, fontweight='bold', pad=8)
plt.tight_layout()

# Save vector PDF & high-res PNG
pdf_path = os.path.join(fig_dir, "latency_comparison.pdf")
png_path = os.path.join(fig_dir, "latency_comparison.png")

plt.savefig(pdf_path, format='pdf', bbox_inches='tight')
plt.savefig(png_path, format='png', dpi=600, bbox_inches='tight')

print("Successfully generated figure files at:")
print("  PDF:", pdf_path)
print("  PNG:", png_path)
