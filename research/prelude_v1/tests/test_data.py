"""
Unit tests for data loader and contamination detection in PRELUDE v1.
"""

from ..data.contamination import check_dataset_leakage, normalize_text, compute_ngrams


def test_ngram_and_normalization():
    t = "Question: Sarah has 15 apples, right?"
    norm = normalize_text(t)
    assert "question sarah has 15 apples right" == norm
    
    grams = compute_ngrams(t, n=3)
    assert len(grams) > 0
    assert "sarah has 15" in grams


def test_leakage_detection():
    train_ex = [
        {"question": "Tom has 10 marbles and gives 3 to Alice. How many does he have?", "answer": "7"},
        {"question": "What is the speed of light in vacuum in meters per second?", "answer": "3e8"}
    ]
    
    # 1. Clean test set
    clean_test = [
        {"question": "A train travels 120 miles in 2 hours. What is the average speed in miles per hour?", "answer": "60"}
    ]
    has_leak, pct, _ = check_dataset_leakage(train_ex, clean_test, ngram_n=5)
    assert has_leak is False
    assert pct == 0.0
    
    # 2. Contaminated test set (near duplicate)
    leaked_test = [
        {"question": "Tom has 10 marbles and gives 3 to Alice. How many does he have left?", "answer": "7"}
    ]
    has_leak2, pct2, leaks = check_dataset_leakage(train_ex, leaked_test, ngram_n=5)
    assert has_leak2 is True
    assert len(leaks) == 1


if __name__ == "__main__":
    test_ngram_and_normalization()
    test_leakage_detection()
    print("[+] All data contamination unit tests PASSED.")
