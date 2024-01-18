#!/usr/bin/env python3
"""task 2"""

import time
from asyncio import Task, gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function to measure the time"""
    start = time.monotonic()
    tasks = [Task(async_comprehension()) for i in range(4)]
    await gather(*tasks)

    return (time.monotonic() - start)
