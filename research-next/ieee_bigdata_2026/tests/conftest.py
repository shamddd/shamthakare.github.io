import sys
import os

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if pkg_root not in sys.path:
    sys.path.insert(0, pkg_root)

scratch_root = os.path.abspath(os.path.join(pkg_root, ".."))
if scratch_root not in sys.path:
    sys.path.insert(0, scratch_root)
