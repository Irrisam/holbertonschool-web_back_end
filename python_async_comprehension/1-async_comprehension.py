#!/usr/bin/env python3
"""generates 10 values using asynchronous loop trough async generator"""

import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> float:
    """generates 10 values using asynchronous loop trough async generator"""
    return_values = []
    async for rand in async_generator():
        return_values.append(rand)
    return return_values
