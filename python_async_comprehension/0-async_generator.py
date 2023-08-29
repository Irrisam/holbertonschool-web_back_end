#!/usr/bin/env python3
"""function generating asynchronous method"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    """function generating asynchronous method"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
