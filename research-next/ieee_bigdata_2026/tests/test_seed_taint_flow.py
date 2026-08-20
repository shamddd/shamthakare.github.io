import os
import ast
import pytest

APPROVED_RNG_CALLS = {"manual_seed", "seed", "default_rng", "set_seed", "srand"}
SEED_VAR_NAMES = {"seed", "training_seed", "eval_seed", "rng_seed", "seed_index"}

class SeedTaintVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.violations = []

    def visit_BinOp(self, node):
        # Check if left or right is a seed variable
        for name in ast.walk(node):
            if isinstance(name, ast.Name) and name.id in SEED_VAR_NAMES:
                self.violations.append(f"Seed variable '{name.id}' used in BinOp at line {node.lineno}")
        self.generic_visit(node)

    def visit_Subscript(self, node):
        for name in ast.walk(node.slice):
            if isinstance(name, ast.Name) and name.id in SEED_VAR_NAMES:
                self.violations.append(f"Seed variable '{name.id}' used in Subscript slice at line {node.lineno}")
        self.generic_visit(node)

    def visit_Call(self, node):
        # Allow seed variables only in approved RNG calls
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
        
        if func_name not in APPROVED_RNG_CALLS:
            for arg in node.args:
                for name in ast.walk(arg):
                    if isinstance(name, ast.Name) and name.id in SEED_VAR_NAMES:
                        self.violations.append(f"Seed variable '{name.id}' passed to non-RNG function '{func_name}' at line {node.lineno}")
        self.generic_visit(node)

def test_seed_taint_flow():
    """AST static analysis ensuring seed variables are strictly confined to approved RNG calls."""
    active_dir = "research-next/ieee_bigdata_2026"
    all_violations = []
    
    for root, dirs, files in os.walk(active_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("test_"):
                path = os.path.join(root, f)
                with open(path, "r") as fp:
                    try:
                        tree = ast.parse(fp.read(), filename=path)
                        visitor = SeedTaintVisitor(path)
                        visitor.visit(tree)
                        if visitor.violations:
                            all_violations.extend([f"{path}: {v}" for v in visitor.violations])
                    except Exception as e:
                        pass
                        
    assert not all_violations, f"Seed taint violations detected: {all_violations}"
