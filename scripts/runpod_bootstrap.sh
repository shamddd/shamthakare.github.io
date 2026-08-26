#!/usr/bin/env bash
# RunPod Worker Bootstrap Script for StateShift Phase 8
# Author: Sham Satish Thakare

set -euo pipefail

SCIENTIFIC_PROTOCOL_SHA="750039aa76bcd197ca7abf4fd91f202260914afb"
EXECUTION_CODE_SHA="18d31ab3bed815f95de625a559890de568012c04"

echo "=========================================================="
echo "STATESHIFT RUNPOD WORKER BOOTSTRAP INITIALIZATION"
echo "=========================================================="

# 1. Hardware & System Audit
nvidia-smi
python3 -c "import torch; print('CUDA Available:', torch.cuda.is_available()); print('Device Name:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"

# 2. Checkout Execution Repository & Verify SHAs
echo "Cloning and checking out execution code commit SHA ${EXECUTION_CODE_SHA}..."
git clone https://github.com/shamddd/stateshift.git /workspace/stateshift || true
cd /workspace/stateshift
git checkout "$EXECUTION_CODE_SHA"

CURRENT_HEAD="$(git rev-parse HEAD)"
if [[ "$CURRENT_HEAD" != "$EXECUTION_CODE_SHA"* ]]; then
    echo "FAIL-CLOSED: Execution SHA mismatch! Expected ${EXECUTION_CODE_SHA}, got ${CURRENT_HEAD}"
    exit 1
fi
echo "Execution SHA verified cleanly: ${CURRENT_HEAD}"

# 3. Environment Dependencies
echo "Installing pinned Python dependencies from requirements-phase8-runpod.txt..."
pip install -q --upgrade pip
pip install -q -r requirements-phase8-runpod.txt

# 4. Run DEV 100-Job Benchmark First
echo "Running DEV 100-Job Benchmark on Pilot Manifest..."
python3 scripts/runpod_resumable_runner.py --benchmark_jobs 100 --benchmark_manifest artifacts/stateshift_v4/manifest/pilot_benchmark_job_manifest.jsonl

if [[ "${1:-}" == "--run-confirmatory" ]]; then
    echo "Launching full confirmatory inference with $4.00 initial budget guard..."
    python3 scripts/runpod_resumable_runner.py --max_budget_usd 4.00 --cost_per_hour 1.69
else
    echo "PILOT BENCHMARK COMPLETE. Stopping worker before confirmatory execution."
fi
