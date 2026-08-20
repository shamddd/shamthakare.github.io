"""
Unit tests for deterministic math reasoning verifiers in PRELUDE v1.
"""

import pytest
from ..verifiers.math_verifier import extract_answer_from_prediction, verify_math_equivalence, verify_reasoning_rollout


def test_answer_extraction_patterns():
    # 1. #### Box
    t1 = "Let's calculate: 10 + 5 = 15.\n#### 15"
    assert extract_answer_from_prediction(t1) == "15"
    
    # 2. \boxed{...}
    t2 = "The total number is \\boxed{42.5}."
    assert extract_answer_from_prediction(t2) == "42.5"
    
    # 3. Text sentence
    t3 = "Therefore, the answer is $120."
    assert extract_answer_from_prediction(t3) == "120"
    
    # 4. Trailing line number
    t4 = "Step 1: 5 * 2 = 10\nStep 2: 10 - 3\n7"
    assert extract_answer_from_prediction(t4) == "7"


def test_math_equivalence_cases():
    # Exact integers
    assert verify_math_equivalence("15", "15") is True
    assert verify_math_equivalence("15", "16") is False
    
    # Comma formatting
    assert verify_math_equivalence("1,000", "1000") is True
    assert verify_math_equivalence("1000.0", "1,000") is True
    
    # Fractions vs decimals
    assert verify_math_equivalence("3/4", "0.75") is True
    assert verify_math_equivalence("1/2", "0.5") is True
    
    # Negative values
    assert verify_math_equivalence("-4.5", "-4.50") is True
    assert verify_math_equivalence("-4", "4") is False
    
    # None candidate
    assert verify_math_equivalence(None, "10") is False


def test_full_rollout_verification():
    gold = "Let's add 5 and 3.\n#### 8"
    good_pred = "First we take 5, then add 3 to get 8.\n#### 8"
    bad_pred = "First we take 5, then add 3 to get 9.\n#### 9"
    
    r_good, cand_good, gold_ans = verify_reasoning_rollout(good_pred, gold)
    assert r_good == 1
    assert cand_good == "8"
    assert gold_ans == "8"
    
    r_bad, cand_bad, _ = verify_reasoning_rollout(bad_pred, gold)
    assert r_bad == 0
    assert cand_bad == "9"


if __name__ == "__main__":
    test_answer_extraction_patterns()
    test_math_equivalence_cases()
    test_full_rollout_verification()
    print("[+] All verifier unit tests PASSED.")
