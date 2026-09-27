"""Tests for the calc demo module — exactly one must fail (the bug)."""
from __future__ import annotations

import pytest

from calc import add, average


def test_add():
    assert add(2, 3) == 5


def test_average():
    assert average([2, 4, 6]) == 4.0


def test_average_empty():
    with pytest.raises(ValueError):
        average([])
