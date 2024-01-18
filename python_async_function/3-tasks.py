#!/usr/bin/env python3
"""task 3"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """wait random task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task