# STATESHIFT ENDPOINT-K16 REPRODUCTION GUIDE

1. Install dependencies from REQUIREMENTS_LOCK.txt
2. Verify input registry hashes against REGISTRY_MANIFEST.json
3. Run `python3 research-next/stateshift/09_phase1i_readiness/run_confirmatory_experiment.py --authorize-confirmatory-run`
4. Re-calculate bootstrap using `python3 research-next/stateshift/13_phase1j_confirmatory_execution/` analysis scripts.
