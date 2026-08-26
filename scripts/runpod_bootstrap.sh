#!/usr/bin/env bash
# RunPod Worker Bootstrap Script for StateShift Phase 8
# Author: Sham Satish Thakare

set -euo pipefail

echo "=========================================================="
echo "STATESHIFT RUNPOD WORKER BOOTSTRAP INITIALIZATION"
echo "=========================================================="

# 1. Hardware Audit
nvidia-smi
python3 -c "import torch; print('CUDA Available:', torch.cuda.is_available()); print('Device Name:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"

# 2. Checkout Frozen Repository SHA
echo "Checking out frozen repository SHA 750039aa76bcd197ca7abf4fd91f202260914afb..."
git clone https://github.com/shamddd/stateshift.git /workspace/stateshift || true
cd /workspace/stateshift
git checkout 750039aa76bcd197ca7abf4fd91f202260914afb

# 3. Environment Dependencies
echo "Installing Python dependencies (vLLM, PyTorch, Transformers, Sympy)..."
pip install -q --upgrade pip
pip install -q vllm torch transformers sympy pandas numpy pytest

# 4. Launch Resumable Runner
echo "Launching StateShift Resumable vLLM Execution Runner..."
python3 scripts/runpod_resumable_runner.py --max_budget_usd 15.0

echo "Bootstrap complete."
