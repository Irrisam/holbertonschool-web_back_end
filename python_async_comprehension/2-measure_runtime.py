#!/usr/bin/env python3
"""function that measures the runtime of 4 async methods with asyncio.gather"""

import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """function that measures the runtime of 4 async methods with
    asyncio.gather"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    total = end_time - start_time
    return total
