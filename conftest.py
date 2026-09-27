"""Pytest path bootstrap: make the repo root importable.

BugFlow runs ``pytest tests/`` with the snapshot root as cwd; this
guarantees ``import calc`` resolves the same way locally and remotely.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
