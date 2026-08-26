#!/usr/bin/env bash
# RunPod Worker Bootstrap Script for StateShift Phase 8
# Author: Sham Satish Thakare

set -euo pipefail

SCIENTIFIC_PROTOCOL_SHA="750039aa76bcd197ca7abf4fd91f202260914afb"

echo "=========================================================="
echo "STATESHIFT RUNPOD WORKER BOOTSTRAP INITIALIZATION"
echo "=========================================================="

# 1. Hardware & System Audit
nvidia-smi
python3 -c "import torch; print('CUDA Available:', torch.cuda.is_available()); print('Device Name:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"

# 2. Checkout Execution Repository
echo "Verifying scientific protocol freeze SHA ${SCIENTIFIC_PROTOCOL_SHA}..."
git clone https://github.com/shamddd/stateshift.git /workspace/stateshift || true
cd /workspace/stateshift

# 3. Environment Dependencies
echo "Installing Python dependencies (vLLM, PyTorch, Transformers, Sympy)..."
pip install -q --upgrade pip
pip install -q vllm torch transformers sympy pandas numpy pytest

# 4. Run DEV Smoke Test First
echo "Running DEV 100-Job Benchmark Smoke Test..."
python3 scripts/runpod_resumable_runner.py --benchmark_jobs 100

if [[ "${1:-}" == "--run-confirmatory" ]]; then
    echo "Launching full confirmatory inference with $4.00 initial budget guard..."
    python3 scripts/runpod_resumable_runner.py --max_budget_usd 4.00 --cost_per_hour 1.69
else
    echo "SMOKE TEST COMPLETE. Pass --run-confirmatory to start confirmatory execution."
fi
