#!/usr/bin/env python3
from typing import Callable
""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier(value: float) -> float:
        result = value * multiplier
        return result
    return make_multiplier
