#!/usr/bin/env python3
"""annotating correctly the values"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotated values for given function"""
    return [(i, len(i)) for i in lst]
