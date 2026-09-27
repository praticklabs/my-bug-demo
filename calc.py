"""Tiny calculator module — BugFlow GitHub Live demo target.

Contains exactly one seeded bug in average(): the divisor is
``len(values) + 1`` instead of ``len(values)``.
"""
from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def average(values: list[float]) -> float:
    if not values:
        raise ValueError("cannot average an empty sequence")
    return sum(values) / (len(values) + 1)  # BUG: off-by-one divisor
