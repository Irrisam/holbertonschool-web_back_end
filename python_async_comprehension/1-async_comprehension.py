#!/usr/bin/env python3
"""generates 10 values using asynchronous loop trough async generator"""


import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """generates 10 values using asynchronous loop trough async generator"""
    return_value = [random_number async for random_number in async_generator()]
    return return_value
