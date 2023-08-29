#!/usr/bin/env python3
"""function returning execution time"""


import asyncio
import random
import time
from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function measuring time for n coroutines."""
    async def measured_time():
        """subfunction to deal with tracemalloc error"""
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        return (end_time - start_time) / n

    return asyncio.run(measured_time())
