import sys
import os

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if pkg_path not in sys.path:
    sys.path.insert(0, pkg_path)

# Also add scratch root if needed
scratch_root = os.path.abspath(os.path.join(pkg_path, ".."))
if scratch_root not in sys.path:
    sys.path.insert(0, scratch_root)
