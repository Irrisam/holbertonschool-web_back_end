#!/usr/bin/env python3
"""function that stores time waited and returns it in a n long loop"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that returns waited time"""
    values_list = []
    for _ in range(n):
        wait_time = await wait_random(max_delay)
        values_list.append(wait_time)

    return sorted(values_list)
