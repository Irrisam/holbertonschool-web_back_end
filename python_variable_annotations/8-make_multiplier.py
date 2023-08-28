#!/usr/bin/env python3
from typing import Callable
"""function that returns a multiplying function"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function returning the multiplying function"""
    def multiplier_func(value: float) -> float:
        """the multiplying function"""
        result = value * multiplier
        return result
    return multiplier_func
