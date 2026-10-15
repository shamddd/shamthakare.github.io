#!/usr/bin/env python3
import json
import os

# Relative or clean script path configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "rlvr-reasoning")
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "research", "rlvr-reasoning")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Store Canonical Verified Data JSON (Without Administrative Manuscript IDs)
canonical_data = {
    "paper_title": "Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training",
    "author": "Sham Satish Thakare",
    "last_verified": "2026-08-20",
    "version": "v1.0",
    "git_commit": "cc2bec4",
    "model": "Qwen/Qwen2.5-0.5B-Instruct",
    "dataset": "GSM8K (N=100 prompt clusters, 98 degrees of freedom)",
    "table_1_proxies": [
        {"proxy": "Self-Consistency (K=4)", "auroc": 0.812, "r_err": 0.582, "r_len": 0.114, "partial_r": -0.569, "p_val": "8.1e-10", "n_samples": 100},
        {"proxy": "Token Pred. Entropy", "auroc": 0.618, "r_err": 0.214, "r_len": 0.486, "partial_r": -0.092, "p_val": "0.365", "n_samples": 100},
        {"proxy": "Mean Token NLL", "auroc": 0.605, "r_err": 0.198, "r_len": 0.432, "partial_r": -0.081, "p_val": "0.422", "n_samples": 100},
        {"proxy": "Logit Margin Unc.", "auroc": 0.624, "r_err": 0.226, "r_len": 0.495, "partial_r": -0.104, "p_val": "0.303", "n_samples": 100}
    ],
    "table_2_rl_controls": [
        {"method": "Standard-GRPO", "group_size": 4, "pass_at_1": 80.00, "std_dev": 0.00, "train_rwd": 0.12, "seeds": 3},
        {"method": "Compute-Matched-GRPO", "group_size": 8, "pass_at_1": 78.33, "std_dev": 2.89, "train_rwd": 0.26, "seeds": 3},
        {"method": "Random-Weight-Control", "group_size": 4, "pass_at_1": 75.00, "std_dev": 5.00, "train_rwd": 0.21, "seeds": 3},
        {"method": "Permuted-Consist.-Control", "group_size": 4, "pass_at_1": 80.00, "std_dev": 0.00, "train_rwd": 0.29, "seeds": 3},
        {"method": "CA-GRPO (Proposed)", "group_size": 4, "pass_at_1": 80.00, "std_dev": 0.00, "train_rwd": 0.12, "seeds": 3}
    ],
    "zero_dropout_audit": {
        "active_dropout_modules": 0,
        "attention_dropout": 0.0,
        "mc_dropout_var_log_p": 0.0000000000,
        "delta_logit": 0.0,
        "gradient_cosine_similarity": 1.000000,
        "order_of_operations_noise": 1e-12
    },
    "stress_test": {
        "misidentification_rate_pct": 42.1,
        "n_samples": 100,
        "description": "Token entropy misidentifies correct multi-step reasoning traces as more uncertain than short incorrect errors in 42.1% of paired comparisons."
    }
}

with open(os.path.join(DATA_DIR, "figure-data.json"), "w") as f:
    json.dump(canonical_data, f, indent=2)

print("Saved figure-data.json cleanly.")

# Helper SVG Generation Functions
def save_svg(filename, svg_content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Generated {filename}")

# 1. Hero Concept SVG (Redesigned 10-Second Flow)
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 360" width="100%" height="100%">
  <rect width="850" height="360" fill="#0f172a" rx="12"/>
  <text x="425" y="38" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="19" font-weight="700" text-anchor="middle">
    Reasoning Complexity Confound in RLVR Confidence Signals
  </text>
  <text x="425" y="60" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    GSM8K (N = 100 prompt clusters) — Token entropy tracks completion length (r = 0.486) rather than error
  </text>

  <!-- Flow Chart Structure -->
  <g transform="translate(70, 95)">
    <!-- Box 1 -->
    <rect x="0" y="0" width="200" height="70" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
    <text x="100" y="30" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Longer Reasoning</text>
    <text x="100" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Multi-step proof traces</text>

    <path d="M 205 35 L 235 35" stroke="#64748b" stroke-width="2"/>

    <!-- Box 2 -->
    <rect x="240" y="0" width="200" height="70" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5" rx="6"/>
    <text x="340" y="30" fill="#c084fc" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Higher Token Entropy</text>
    <text x="340" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">r = 0.486 (N=100)</text>

    <path d="M 445 35 L 475 35" stroke="#64748b" stroke-width="2"/>

    <!-- Box 3 -->
    <rect x="480" y="0" width="230" height="70" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="595" y="30" fill="#fde68a" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">"More Uncertain"?</text>
    <text x="595" y="50" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Naive Error Assumption</text>

    <!-- Branching Down -->
    <path d="M 595 75 L 595 110" stroke="#64748b" stroke-width="2"/>

    <!-- Left Branch: True Error -->
    <g transform="translate(180, 120)">
      <rect x="0" y="0" width="250" height="90" fill="#0f291e" stroke="#10b981" stroke-width="1.5" rx="6"/>
      <text x="125" y="28" fill="#34d399" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Self-Consistency Consensus</text>
      <text x="125" y="50" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">AUROC = 0.812 (N=100)</text>
      <text x="125" y="70" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">partial r = -0.569 (p = 8.1e-10)</text>
    </g>

    <!-- Right Branch: Length Confound -->
    <g transform="translate(460, 120)">
      <rect x="0" y="0" width="250" height="90" fill="#3b0707" stroke="#ef4444" stroke-width="1.5" rx="6"/>
      <text x="125" y="28" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Raw Token Entropy</text>
      <text x="125" y="50" fill="#fef2f2" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Length Confound Proxy</text>
      <text x="125" y="70" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">partial r = -0.092 (p = 0.365)</text>
    </g>
  </g>
</svg>"""
save_svg("hero-concept.svg", hero_svg)

# 2. Zero Dropout Audit SVG
zero_dropout_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 320" width="100%" height="100%">
  <rect width="850" height="320" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Architectural Audit: Zero-Dropout MC Probing Determinism
  </text>
  <text x="425" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    Qwen/Qwen2.5-0.5B-Instruct contains exactly 0 active nn.Dropout modules in its compute graph
  </text>

  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="210" height="180" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
    <text x="105" y="30" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Model Compute Graph</text>
    <text x="105" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Qwen2ForCausalLM</text>
    <rect x="25" y="85" width="160" height="30" fill="#0f172a" rx="4"/>
    <text x="105" y="105" fill="#f8fafc" font-family="monospace" font-size="11" text-anchor="middle">attention_dropout = 0.0</text>
    <text x="105" y="145" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Active Dropout Modules: 0</text>

    <path d="M 220 90 L 250 90" stroke="#64748b" stroke-width="2"/>

    <rect x="260" y="0" width="210" height="180" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="365" y="30" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">MC Probing Pass</text>
    <text x="365" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">mc_dropout = True</text>
    <rect x="285" y="85" width="160" height="30" fill="#0f172a" rx="4"/>
    <text x="365" y="105" fill="#f59e0b" font-family="monospace" font-size="11" text-anchor="middle">Var(log P) = 0.000000</text>
    <text x="365" y="145" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Deterministic Execution</text>

    <path d="M 480 90 L 510 90" stroke="#64748b" stroke-width="2"/>

    <rect x="520" y="0" width="210" height="180" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="625" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Update Alignment</text>
    <text x="625" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Policy Gradient Vector</text>
    <rect x="545" y="85" width="160" height="30" fill="#0f172a" rx="4"/>
    <text x="625" y="105" fill="#34d399" font-family="monospace" font-size="11" text-anchor="middle">cos(Δθ) = 1.000000</text>
    <text x="625" y="145" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Collinear to Standard GRPO</text>
  </g>
</svg>"""
save_svg("zero-dropout-audit.svg", zero_dropout_svg)

# 3. AUROC Benchmark SVG
auroc_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 340" width="100%" height="100%">
  <rect width="850" height="340" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Diagnostic Error Discrimination Benchmark (GSM8K, N = 100)
  </text>
  <text x="425" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    Self-consistency achieves AUROC = 0.812, while token entropy (0.618) is degraded by sequence length bias
  </text>

  <g transform="translate(220, 80)">
    <line x1="0" y1="0" x2="550" y2="0" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="-15" y="4" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">1.00</text>

    <line x1="0" y1="50" x2="550" y2="50" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="-15" y="54" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">0.80</text>

    <line x1="0" y1="100" x2="550" y2="100" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="-15" y="104" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">0.60</text>

    <line x1="0" y1="150" x2="550" y2="150" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="-15" y="154" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">0.40</text>

    <line x1="0" y1="200" x2="550" y2="200" stroke="#475569" stroke-width="1.5"/>
    <text x="-15" y="204" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">0.00</text>

    <rect x="40" y="47" width="80" height="153" fill="#10b981" rx="4"/>
    <text x="80" y="37" fill="#34d399" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0.812</text>
    <text x="80" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Self-Consistency</text>
    <text x="80" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(K=4, N=100)</text>

    <rect x="170" y="95.5" width="80" height="104.5" fill="#ef4444" rx="4"/>
    <text x="210" y="85.5" fill="#fca5a5" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0.618</text>
    <text x="210" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Token Entropy</text>
    <text x="210" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(r_len = 0.486)</text>

    <rect x="300" y="94" width="80" height="106" fill="#f59e0b" rx="4"/>
    <text x="340" y="84" fill="#fde68a" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0.624</text>
    <text x="340" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Logit Margin</text>
    <text x="340" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(r_len = 0.495)</text>

    <rect x="430" y="98.7" width="80" height="101.3" fill="#64748b" rx="4"/>
    <text x="470" y="88.7" fill="#cbd5e1" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">0.605</text>
    <text x="470" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Mean NLL</text>
    <text x="470" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(r_len = 0.432)</text>
  </g>
</svg>"""
save_svg("auroc-benchmark.svg", auroc_svg)

# 4. RL Control Results SVG
rl_results_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 360" width="100%" height="100%">
  <rect width="850" height="360" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Preregistered 5-Way Controlled RL Benchmark (N = 3 Seeds)
  </text>
  <text x="425" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    Across the 3 evaluated seeds, CA-GRPO and Standard GRPO produced identical mean Group Pass@1 (80.00%, d = 0.00)
  </text>

  <g transform="translate(100, 85)">
    <line x1="60" y1="0" x2="700" y2="0" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="45" y="4" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">100%</text>

    <line x1="60" y1="50" x2="700" y2="50" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="45" y="54" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">75%</text>

    <line x1="60" y1="100" x2="700" y2="100" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="45" y="104" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">50%</text>

    <line x1="60" y1="150" x2="700" y2="150" stroke="#334155" stroke-dasharray="4,4"/>
    <text x="45" y="154" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">25%</text>

    <line x1="60" y1="200" x2="700" y2="200" stroke="#475569" stroke-width="1.5"/>
    <text x="45" y="204" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="end">0%</text>

    <rect x="90" y="40" width="80" height="160" fill="#3b82f6" rx="4"/>
    <text x="130" y="30" fill="#60a5fa" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">80.00%</text>
    <text x="130" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Standard GRPO</text>
    <text x="130" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Group K=4, N=3)</text>

    <rect x="210" y="43.3" width="80" height="156.7" fill="#8b5cf6" rx="4"/>
    <text x="250" y="33.3" fill="#c084fc" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">78.33%</text>
    <text x="250" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Compute-Matched</text>
    <text x="250" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Group K=8, N=3)</text>

    <rect x="330" y="50" width="80" height="150" fill="#64748b" rx="4"/>
    <text x="370" y="40" fill="#cbd5e1" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">75.00%</text>
    <text x="370" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Random Control</text>
    <text x="370" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Shuffled, N=3)</text>

    <rect x="450" y="40" width="80" height="160" fill="#f59e0b" rx="4"/>
    <text x="490" y="30" fill="#fde68a" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">80.00%</text>
    <text x="490" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Permuted Control</text>
    <text x="490" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Negative, N=3)</text>

    <rect x="570" y="40" width="80" height="160" fill="#10b981" rx="4"/>
    <text x="610" y="30" fill="#34d399" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">80.00%</text>
    <text x="610" y="225" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">CA-GRPO (Proposed)</text>
    <text x="610" y="240" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">(Consensus, N=3)</text>
  </g>
</svg>"""
save_svg("rl-control-results.svg", rl_results_svg)

# 5. Correlation & Partial Correlation SVG
correlation_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 320" width="100%" height="100%">
  <rect width="850" height="320" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Partial Correlation Analysis (GSM8K, N = 100 Prompt Clusters)
  </text>
  <text x="425" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    Controlling for token length collapses entropy-error association from r = -0.214 to partial r = -0.092 (p = 0.365)
  </text>

  <g transform="translate(80, 90)">
    <rect x="0" y="0" width="320" height="190" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="160" y="30" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Bivariate Association (N=100)</text>
    <text x="160" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Token Entropy vs Error: <tspan fill="#ef4444" font-weight="bold">r = -0.214</tspan></text>
    <text x="160" y="95" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Token Entropy vs Length: <tspan fill="#ef4444" font-weight="bold">r = +0.486</tspan></text>
    <rect x="20" y="125" width="280" height="40" fill="#450a0a" stroke="#991b1b" rx="4"/>
    <text x="160" y="150" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
      Appears to Predict Error Naively
    </text>

    <path d="M 335 95 L 365 95" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

    <rect x="380" y="0" width="320" height="190" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="540" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Partial Correlation (Length Controlled)</text>
    <text x="540" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">Token Entropy vs Error | Length (N=100):</text>
    <text x="540" y="95" fill="#34d399" font-family="monospace" font-size="18" font-weight="bold" text-anchor="middle">partial r = -0.092</text>
    <text x="540" y="118" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">(p = 0.365 — Not Statistically Significant)</text>
    <rect x="400" y="135" width="280" height="35" fill="#064e3b" stroke="#047857" rx="4"/>
    <text x="540" y="157" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
      Association Collapses Completely
    </text>
  </g>
</svg>"""
save_svg("correlation-length-entropy.svg", correlation_svg)

# 6. Stress Test Failure SVG
stress_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 300" width="100%" height="100%">
  <rect width="850" height="300" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Stress Test: Correct-but-Complex Derivation Failure Mode (N = 100)
  </text>
  <text x="425" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="13" text-anchor="middle">
    Token predictive entropy misidentifies valid multi-step reasoning as more uncertain than short errors in 42.1% of cases
  </text>

  <g transform="translate(60, 85)">
    <rect x="0" y="0" width="340" height="170" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="170" y="25" fill="#fbbf24" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Trace A: Short Incorrect Answer</text>
    <text x="20" y="55" fill="#cbd5e1" font-family="monospace" font-size="11">"x = 5 + 2 = 10" (Incorrect)</text>
    <text x="20" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Sequence Length: 4 tokens</text>
    <text x="20" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Mean Token Entropy: 0.18</text>
    <rect x="20" y="125" width="300" height="30" fill="#451a03" stroke="#b45309" rx="4"/>
    <text x="170" y="145" fill="#fde68a" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Naively Rated as "High Confidence"</text>

    <text x="365" y="90" fill="#ef4444" font-family="system-ui, sans-serif" font-size="16" font-weight="bold">VS</text>

    <rect x="390" y="0" width="340" height="170" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="560" y="25" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Trace B: Multi-Step Correct Derivation</text>
    <text x="410" y="55" fill="#cbd5e1" font-family="monospace" font-size="11">"Let total = 5... Step 1... Step 2... = 7"</text>
    <text x="410" y="80" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Sequence Length: 48 tokens</text>
    <text x="410" y="105" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12">Mean Token Entropy: 0.42</text>
    <rect x="410" y="125" width="300" height="30" fill="#450a0a" stroke="#b91c1c" rx="4"/>
    <text x="560" y="145" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="11" font-weight="600" text-anchor="middle">Penalized as "Uncertain" (42.1% Pair Misranking)</text>
  </g>
</svg>"""
save_svg("stress-test-failure.svg", stress_svg)

# 7. Experiment Pipeline SVG
pipeline_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="100%" height="100%">
  <rect width="850" height="280" fill="#0f172a" rx="12"/>
  <text x="425" y="32" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Preregistered RLVR Consistency-Aware Evaluation Pipeline
  </text>
  
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="130" height="150" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
    <text x="65" y="30" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1. PROMPT DATA</text>
    <text x="65" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">GSM8K Dataset</text>
    <text x="65" y="85" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">N = 100 Clusters</text>

    <path d="M 135 75 L 155 75" stroke="#64748b" stroke-width="2"/>

    <rect x="160" y="0" width="130" height="150" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5" rx="6"/>
    <text x="225" y="30" fill="#c084fc" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2. ROLLOUTS</text>
    <text x="225" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">K=4 / K=8 Samples</text>
    <text x="225" y="85" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">256 Token Budget</text>

    <path d="M 295 75 L 315 75" stroke="#64748b" stroke-width="2"/>

    <rect x="320" y="0" width="130" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="385" y="30" fill="#fde68a" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. PROXIES</text>
    <text x="385" y="60" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Entropy, NLL,</text>
    <text x="385" y="78" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Logit Margin,</text>
    <text x="385" y="96" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Self-Consistency</text>

    <path d="M 455 75 L 475 75" stroke="#64748b" stroke-width="2"/>

    <rect x="480" y="0" width="130" height="150" fill="#1e293b" stroke="#ec4899" stroke-width="1.5" rx="6"/>
    <text x="545" y="30" fill="#f472b6" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">4. ADVANTAGE</text>
    <text x="545" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Â_i Scaling</text>
    <text x="545" y="85" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">5-Way Controls</text>

    <path d="M 615 75 L 635 75" stroke="#64748b" stroke-width="2"/>

    <rect x="640" y="0" width="140" height="150" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="710" y="30" fill="#34d399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">5. EVALUATION</text>
    <text x="710" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Pass@1 Bench</text>
    <text x="710" y="85" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">N=3 Seeds (d=0.00)</text>
  </g>
</svg>"""
save_svg("experiment-pipeline.svg", pipeline_svg)

# 8. Limitations & Scope Boundary SVG
limitations_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="100%" height="100%">
  <rect width="850" height="280" fill="#0f172a" rx="12"/>
  <text x="425" y="35" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">
    Scope & Limitations Boundary
  </text>
  
  <g transform="translate(50, 75)">
    <rect x="0" y="0" width="360" height="160" fill="#064e3b" stroke="#059669" stroke-width="1.5" rx="8"/>
    <text x="180" y="30" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">
      VALIDATED FINDINGS
    </text>
    <text x="20" y="60" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">• MC-Dropout determinism on 0-dropout LLMs</text>
    <text x="20" y="85" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">• Length confounding in token entropy (r=0.486, N=100)</text>
    <text x="20" y="110" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">• Offline error prediction ≠ Online RL credit</text>
    <text x="20" y="135" fill="#ecfdf5" font-family="system-ui, sans-serif" font-size="12">• Pass@1 equality (d=0.00) across N=3 training seeds</text>

    <rect x="390" y="0" width="360" height="160" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5" rx="8"/>
    <text x="570" y="30" fill="#a5b4fc" font-family="system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">
      UNTESTED / FUTURE SCOPE
    </text>
    <text x="410" y="60" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">• Models > 7B parameters</text>
    <text x="410" y="85" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">• Non-mathematical reasoning domains (Code, Med)</text>
    <text x="410" y="110" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">• Process-level step verifiers (PRMs)</text>
    <text x="410" y="135" fill="#e0e7ff" font-family="system-ui, sans-serif" font-size="12">• Dynamic K > 16 rollout budgets</text>
  </g>
</svg>"""
save_svg("limitations-boundary.svg", limitations_svg)

# 9. Assumption vs Reality SVG
assumption_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 260" width="100%" height="100%">
  <rect width="850" height="260" fill="#0f172a" rx="12"/>
  <text x="425" y="32" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">
    Old Assumption vs Observed Length Confound
  </text>
  
  <g transform="translate(60, 65)">
    <rect x="0" y="0" width="340" height="160" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
    <text x="170" y="30" fill="#60a5fa" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CONVENTIONAL ASSUMPTION</text>
    <text x="20" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• Token entropy measures output uncertainty</text>
    <text x="20" y="90" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• High entropy directly signals mathematical error</text>
    <text x="20" y="115" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• Downweighting uncertain tokens stabilizes RL</text>

    <rect x="390" y="0" width="340" height="160" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="560" y="30" fill="#fca5a5" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">EMPIRICAL DISCOVERY (N=100)</text>
    <text x="410" y="65" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• Token entropy tracks sequence length (r = 0.486)</text>
    <text x="410" y="90" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• Partial r collapses to -0.092 (p = 0.365)</text>
    <text x="410" y="115" fill="#e2e8f0" font-family="system-ui, sans-serif" font-size="12">• Suppresses multi-step exploration in 42.1% of cases</text>
  </g>
</svg>"""
save_svg("assumption-vs-reality.svg", assumption_svg)

print("All 9 SVGs regenerated cleanly.")
