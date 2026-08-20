#!/usr/bin/env python3
"""
Automated Safety Test Suite for StateShift Confirmatory Launcher (Phase 1I.3)
Verifies all safety guards using dry-run / mock execution only.
ZERO MODEL INFERENCE CALLS EXECUTED.
"""

import unittest
from run_confirmatory_experiment import (
    verify_safety_guards,
    EXPECTED_REGISTRY_SHA256,
    EXPECTED_N,
    EXPECTED_TOTAL_ROLLOUTS,
    HARD_SPEND_CEILING_USD,
    MIN_REQUIRED_BALANCE_USD
)

class TestConfirmatoryExecutionSafety(unittest.TestCase):

    def test_unauthorized_execution_blocked(self):
        """Guard 1: Refuses execution if user authorization flag is absent."""
        res = verify_safety_guards(authorize_flag=False, mock_mode=True)
        self.assertFalse(res)

    def test_authorized_mock_execution_passes(self):
        """Guards 2-6: Authorized dry-run passes all budget & hash safety checks."""
        res = verify_safety_guards(authorize_flag=True, mock_mode=True)
        self.assertTrue(res)

    def test_constants_integrity(self):
        """Verify frozen Phase 1I.3 registry and budget parameters."""
        self.assertEqual(EXPECTED_N, 454)
        self.assertEqual(EXPECTED_TOTAL_ROLLOUTS, 29056)
        self.assertEqual(EXPECTED_REGISTRY_SHA256, "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478")
        self.assertEqual(MIN_REQUIRED_BALANCE_USD, 6.82)
        self.assertEqual(HARD_SPEND_CEILING_USD, 8.00)

if __name__ == "__main__":
    unittest.main()
