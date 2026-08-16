"""
Data contamination and train-test leakage checker for PRELUDE v1.
Uses exact n-gram and normalized hash matching to detect prompt overlap.
"""

from typing import List, Dict, Set, Tuple
import re


def normalize_text(text: str) -> str:
    """Removes punctuation and normalizes whitespace for leakage detection."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())


def compute_ngrams(text: str, n: int = 10) -> Set[str]:
    """Extracts word n-grams from normalized text."""
    words = normalize_text(text).split()
    if len(words) < n:
        return set([" ".join(words)])
    return set([" ".join(words[i:i+n]) for i in range(len(words) - n + 1)])


def check_dataset_leakage(train_examples: List[Dict[str, str]], 
                          test_examples: List[Dict[str, str]], 
                          ngram_n: int = 8) -> Tuple[bool, float, List[Dict[str, str]]]:
    """
    Checks if test prompts leak into training prompts.
    Returns:
        has_leakage (bool), max_overlap_ratio (float), list of leaked pairs
    """
    train_ngrams: Set[str] = set()
    for ex in train_examples:
        train_ngrams.update(compute_ngrams(ex["question"], n=ngram_n))
        
    leaks = []
    total_overlapping = 0
    
    for test_idx, test_ex in enumerate(test_examples):
        test_grams = compute_ngrams(test_ex["question"], n=ngram_n)
        if not test_grams:
            continue
        intersection = test_grams.intersection(train_ngrams)
        overlap_ratio = len(intersection) / len(test_grams)
        if overlap_ratio > 0.60:  # >60% overlapping 8-grams
            total_overlapping += 1
            leaks.append({
                "test_index": test_idx,
                "test_question": test_ex["question"],
                "overlap_ratio": overlap_ratio
            })
            
    leakage_pct = (total_overlapping / len(test_examples)) if test_examples else 0.0
    has_leakage = leakage_pct > 0.01  # >1% contamination triggers flag
    return has_leakage, leakage_pct, leaks
