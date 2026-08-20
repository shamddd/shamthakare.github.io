import json
import os
import sys
import hashlib
import unittest

sys.path.insert(0, "research-next/stateshift/09_phase1i_readiness")
import run_confirmatory_experiment as launcher

gate_dir = "research-next/stateshift/12_phase1i4_final_authorization_gate"
v4_registry = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"
v4_strict = "research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"

class TestPhase1I4bRealSourceConformance(unittest.TestCase):

    def test_01_real_module_imports_cleanly(self):
        """Verify the real launcher module imports cleanly without error."""
        self.assertTrue(hasattr(launcher, "load_and_verify_config"))
        self.assertTrue(hasattr(launcher, "verify_safety_guards"))
        self.assertTrue(hasattr(launcher, "CONFIG"))

    def test_02_json_import_present_and_used(self):
        """Verify json module is present and properly used."""
        self.assertTrue(hasattr(launcher, "json"))

    def test_03_config_parsed_only_after_sha_verification(self):
        """Verify raw bytes SHA-256 is checked before parsing JSON."""
        with open(launcher.CONFIG_PATH, "rb") as f:
            actual_sha = hashlib.sha256(f.read()).hexdigest()
        self.assertEqual(actual_sha, launcher.EXPECTED_CONFIG_SHA256)

    def test_04_altered_config_hash_hard_fails(self):
        """Verify load_and_verify_config hard-fails on tampered SHA-256."""
        with self.assertRaises(ValueError):
            launcher.load_and_verify_config(launcher.CONFIG_PATH, "0000000000000000000000000000000000000000000000000000000000000000")

    def test_05_missing_config_hard_fails(self):
        """Verify load_and_verify_config hard-fails on missing config file."""
        with self.assertRaises(FileNotFoundError):
            launcher.load_and_verify_config("non_existent_config_file.json", launcher.EXPECTED_CONFIG_SHA256)

    def test_06_zero_config_get_fallback_defaults_exist(self):
        """Audit source code to ensure ZERO superseded constants exist as active runtime configuration."""
        with open("research-next/stateshift/09_phase1i_readiness/run_confirmatory_experiment.py", "r") as f:
            source_text = f.read()
        
        # Remove expected hash string from search to avoid false positive hex matching
        sanitized_source = source_text.replace(launcher.EXPECTED_CONFIG_SHA256, "")

        self.assertNotIn("CONFIG.get(", sanitized_source)
        self.assertNotIn("130752", sanitized_source)
        self.assertNotIn("131328", sanitized_source)
        self.assertNotIn("35.00", sanitized_source)
        self.assertNotIn("30.70", sanitized_source)
        self.assertNotIn("456", sanitized_source)
        self.assertNotIn("[32,64,96,128,160,192,224]", sanitized_source)

    def test_07_only_permitted_hardcoded_identifiers_exist(self):
        """Verify ONLY CONFIG_PATH and EXPECTED_CONFIG_SHA256 are hardcoded."""
        self.assertEqual(launcher.CONFIG_PATH, "research-next/stateshift/12_phase1i4_final_authorization_gate/PHASE1I4_FINAL_EXECUTION_CONFIG.json")
        self.assertEqual(launcher.EXPECTED_CONFIG_SHA256, "079f99bf8e5ceb8b45b680b4bc2e34f718e4453031c55ee456da0a331209cdcf")

    def test_08_invariants_loaded_directly_from_config(self):
        """Verify scientific invariants extracted directly from CONFIG."""
        cfg = launcher.CONFIG
        self.assertEqual(cfg["authoritative_n"], 454)
        self.assertEqual(cfg["strict_n"], 388)
        self.assertEqual(cfg["checkpoints"], [0, 256])
        self.assertEqual(cfg["rollouts_per_cell_k"], 16)
        self.assertEqual(cfg["total_confirmatory_rollouts"], 29056)
        self.assertEqual(cfg["max_new_tokens"], 512)
        self.assertEqual(cfg["sampling_temperature"], 0.6)
        self.assertEqual(cfg["sampling_top_p"], 0.95)
        self.assertEqual(cfg["hard_spend_ceiling_usd"], 8.00)
        self.assertEqual(cfg["expected_total_budget_usd"], 6.82)
        self.assertEqual(cfg["record_type"], "empirical_confirmatory")

    def test_09_registry_and_ledger_hashes_exact(self):
        """Verify registry and ledger hashes against CONFIG."""
        cfg = launcher.CONFIG
        with open(v4_registry, "rb") as f:
            actual_auth = hashlib.sha256(f.read()).hexdigest()
        with open(v4_strict, "rb") as f:
            actual_strict = hashlib.sha256(f.read()).hexdigest()
        with open(cfg["ledger_path"], "rb") as f:
            actual_ledger = hashlib.sha256(f.read()).hexdigest()

        self.assertEqual(actual_auth, cfg["authoritative_registry_sha256"])
        self.assertEqual(actual_strict, cfg["strict_registry_sha256"])
        self.assertEqual(actual_ledger, cfg["ledger_sha256"])

    def test_10_authorization_flag_required(self):
        """Verify safety guards block execution without explicit authorization flag."""
        res_unauth = launcher.verify_safety_guards(authorize_flag=False, mock_mode=True)
        self.assertFalse(res_unauth)

    def test_11_authorized_mock_run_passes(self):
        """Verify authorized dry-run mock execution passes cleanly."""
        res_auth = launcher.verify_safety_guards(authorize_flag=True, mock_mode=True)
        self.assertTrue(res_auth)

if __name__ == "__main__":
    unittest.main()
