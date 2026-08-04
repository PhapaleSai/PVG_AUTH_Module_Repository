"""
conftest.py — adds the backend root to sys.path so that
test modules can import database, models, auth, etc. directly.
"""

import os
import sys

# Ensure the backend/ directory is on the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
