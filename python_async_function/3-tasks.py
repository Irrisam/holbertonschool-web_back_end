#!/usr/bin/env python3
"""creates and returns a task from async io module"""


import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates and returns a task from async io module"""
    instance = wait_random(max_delay)
    task = asyncio.create_task(instance)

    return task
