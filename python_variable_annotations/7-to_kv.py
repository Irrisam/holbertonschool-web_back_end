#!/usr/bin/env python3
"""annotates then returns tuple with types"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """returns the type annotated values"""
    return k, v
