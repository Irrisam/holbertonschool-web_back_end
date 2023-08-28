#!/usr/bin/env python3
"""returns sum of the list of float and int"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of the list of float and int"""
    return sum(mxd_lst)
