"""
Deterministic ground-truth math reasoning verifiers for recovery_eval.
Parses model generation answers, extracts boxed/final values, and performs symbolic equivalence checks.
"""

import re
from typing import Optional, Tuple, Any
import sympy as sp


def extract_answer_from_gold(gold_text: str) -> str:
    """Extracts target numerical or symbolic answer from reference text."""
    if "####" in gold_text:
        return gold_text.split("####")[-1].strip()
    match = re.search(r"\\boxed\{([^}]+)\}", gold_text)
    if match:
        return match.group(1).strip()
    # Fallback to last numerical token
    numbers = re.findall(r"[-+]?\d*\.?\d+", gold_text.replace(",", ""))
    return numbers[-1] if numbers else gold_text.strip()


def extract_answer_from_prediction(pred_text: str) -> Optional[str]:
    """Extracts the final candidate answer from a model reasoning rollout."""
    # Pattern 1: #### Answer
    if "####" in pred_text:
        ans_part = pred_text.split("####")[-1].strip()
        num_match = re.search(r"[-+]?\d*\.?\d+", ans_part.replace(",", ""))
        if num_match:
            return num_match.group(0)
            
    # Pattern 2: \boxed{...}
    boxed_match = re.search(r"\\boxed\{([^}]+)\}", pred_text)
    if boxed_match:
        cand = boxed_match.group(1).strip()
        num_match = re.search(r"[-+]?\d*\.?\d+", cand.replace(",", ""))
        if num_match:
            return num_match.group(0)
            
    # Pattern 3: "The answer is ..." or "is: ..."
    ans_regex = re.search(r"(?:the answer is|equals|is equal to|result is|is:)\s*([\$]?[-+]?\d*\.?\d+)", pred_text, re.IGNORECASE)
    if ans_regex:
        return ans_regex.group(1).replace("$", "").strip()

    # Pattern 4: Last line / last numerical token
    lines = [line.strip() for line in pred_text.split("\n") if line.strip()]
    if lines:
        last_line = lines[-1]
        numbers = re.findall(r"[-+]?\d*\.?\d+", last_line.replace(",", ""))
        if numbers:
            return numbers[-1]
            
    # Pattern 5: Overall last numerical token
    all_numbers = re.findall(r"[-+]?\d*\.?\d+", pred_text.replace(",", ""))
    if all_numbers:
        return all_numbers[-1]
        
    return None


def verify_math_equivalence(pred_str: Optional[str], gold_str: str, tolerance: float = 1e-4) -> bool:
    """Checks deterministic mathematical equivalence using SymPy and numerical normalization."""
    if pred_str is None:
        return False
        
    clean_gold = gold_str.replace(",", "").replace("$", "").strip()
    clean_pred = pred_str.replace(",", "").replace("$", "").strip()
    
    # 1. Exact string match
    if clean_pred == clean_gold:
        return True
        
    # 2. Float numerical conversion
    try:
        f_pred = float(clean_pred)
        f_gold = float(clean_gold)
        if abs(f_pred - f_gold) <= tolerance:
            return True
    except (ValueError, OverflowError):
        pass

    # 3. SymPy symbolic evaluation (fractions, algebraic expressions)
    try:
        sp_pred = sp.sympify(clean_pred)
        sp_gold = sp.sympify(clean_gold)
        diff = sp.simplify(sp_pred - sp_gold)
        if diff == 0 or (diff.is_number and abs(float(diff)) <= tolerance):
            return True
    except Exception:
        pass
        
    return False


def verify_reasoning_rollout(prediction_text: str, gold_reference: str) -> Tuple[int, Optional[str], str]:
    """
    Evaluates a single model rollout.
    Returns:
        reward (int: 0 or 1), extracted_candidate (str or None), gold_answer (str)
    """
    gold_answer = extract_answer_from_gold(gold_reference)
    candidate_answer = extract_answer_from_prediction(prediction_text)
    is_correct = verify_math_equivalence(candidate_answer, gold_answer)
    return (1 if is_correct else 0, candidate_answer, gold_answer)
