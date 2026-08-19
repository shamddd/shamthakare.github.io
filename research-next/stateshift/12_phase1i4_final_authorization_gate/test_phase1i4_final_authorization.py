import json
import os
import sys
import hashlib
import unittest

sys.path.insert(0, "research-next/stateshift/09_phase1i_readiness")
from run_confirmatory_experiment import load_and_verify_config, verify_safety_guards, CONFIG_PATH, EXPECTED_CONFIG_SHA256

gate_dir = "research-next/stateshift/12_phase1i4_final_authorization_gate"
freeze_dir = "research-next/stateshift/11_phase1i3_execution_freeze"
v4_registry = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"
v4_strict = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"

class TestPhase1I4aSingleSourceConfig(unittest.TestCase):

    def test_01_config_hash_exact(self):
        """Verify config SHA-256 matches expected hash BEFORE parsing."""
        with open(CONFIG_PATH, "rb") as f:
            actual_sha = hashlib.sha256(f.read()).hexdigest()
        self.assertEqual(actual_sha, EXPECTED_CONFIG_SHA256)

    def test_02_missing_config_hard_fails(self):
        """Verify launcher hard-fails when config path does not exist."""
        with self.assertRaises((FileNotFoundError, Exception)):
            load_and_verify_config("non_existent_config.json", EXPECTED_CONFIG_SHA256)

    def test_03_altered_config_hard_fails(self):
        """Verify launcher hard-fails when config SHA-256 hash does not match."""
        with self.assertRaises(ValueError):
            load_and_verify_config(CONFIG_PATH, "0000000000000000000000000000000000000000000000000000000000000000")

    def test_04_scientific_invariants_exact(self):
        """Verify all scientific invariants loaded from JSON config."""
        cfg = load_and_verify_config()
        self.assertEqual(cfg["authoritative_n"], 454)
        self.assertEqual(cfg["strict_n"], 388)
        self.assertEqual(cfg["checkpoints"], [0, 256])
        self.assertEqual(cfg["rollouts_per_cell_k"], 16)
        self.assertEqual(cfg["total_confirmatory_rollouts"], 29056)
        self.assertEqual(cfg["sampling_temperature"], 0.6)
        self.assertEqual(cfg["sampling_top_p"], 0.95)
        self.assertEqual(cfg["max_new_tokens"], 512)
        self.assertEqual(cfg["hard_spend_ceiling_usd"], 8.00)
        self.assertEqual(cfg["expected_total_budget_usd"], 6.82)
        self.assertEqual(cfg["record_type"], "empirical_confirmatory")

    def test_05_registry_hashes_exact(self):
        """Verify primary and strict registry SHA-256 hashes against config."""
        cfg = load_and_verify_config()
        with open(v4_registry, "rb") as f:
            actual_auth = hashlib.sha256(f.read()).hexdigest()
        with open(v4_strict, "rb") as f:
            actual_strict = hashlib.sha256(f.read()).hexdigest()
        self.assertEqual(actual_auth, cfg["authoritative_registry_sha256"])
        self.assertEqual(actual_strict, cfg["strict_registry_sha256"])

    def test_06_ledger_hash_exact(self):
        """Verify 29,056-row ledger SHA-256 against config."""
        cfg = load_and_verify_config()
        ledger_file = cfg["ledger_path"]
        with open(ledger_file, "rb") as f:
            actual_ledger = hashlib.sha256(f.read()).hexdigest()
        self.assertEqual(actual_ledger, cfg["ledger_sha256"])

    def test_07_authorization_flag_required(self):
        """Verify launcher refuses execution without explicit user authorization flag."""
        res_unauth = verify_safety_guards(authorize_flag=False, mock_mode=True)
        self.assertFalse(res_unauth)

    def test_08_authorized_mock_run_passes(self):
        """Verify launcher passes all guards in authorized mock dry-run mode."""
        res_auth = verify_safety_guards(authorize_flag=True, mock_mode=True)
        self.assertTrue(res_auth)

if __name__ == "__main__":
    unittest.main()
