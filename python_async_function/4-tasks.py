#!/usr/bin/env python3
"""altered function returning task"""

import _asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """altered function returning task"""
    values_list = []
    for _ in range(n):
        wait_time = await task_wait_random(max_delay)
        values_list.append(wait_time)

    return sorted(values_list)
