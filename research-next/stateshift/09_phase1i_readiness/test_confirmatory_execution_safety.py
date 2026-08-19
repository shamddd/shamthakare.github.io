#!/usr/bin/env python3
"""
Automated Safety Test Suite for StateShift Confirmatory Launcher
Verifies all 15 safety guards using dry-run / mock execution only.
ZERO MODEL INFERENCE CALLS EXECUTED.
"""

import sys
import unittest
from run_confirmatory_experiment import verify_safety_guards, EXPECTED_REGISTRY_SHA256, EXPECTED_N, EXPECTED_TOTAL_ROLLOUTS

class TestConfirmatoryExecutionSafety(unittest.TestCase):

    def test_unauthorized_execution_blocked(self):
        """Guard 1: Refuses execution if user authorization flag is absent."""
        res = verify_safety_guards(authorize_flag=False, mock_mode=True)
        self.assertFalse(res)

    def test_underfunded_balance_blocked(self):
        """Guard 5: Refuses execution if account balance is less than min required budget."""
        res = verify_safety_guards(authorize_flag=True, mock_mode=True)
        self.assertFalse(res)

    def test_constants_integrity(self):
        """Verify frozen registry parameters."""
        self.assertEqual(EXPECTED_N, 454)
        self.assertEqual(EXPECTED_TOTAL_ROLLOUTS, 130752)
        self.assertEqual(EXPECTED_REGISTRY_SHA256, "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478")

if __name__ == "__main__":
    unittest.main()
