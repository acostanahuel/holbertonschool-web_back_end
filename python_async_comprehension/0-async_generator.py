#!/usr/bin/env python3
"""task 0"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator"""
    for i in range(10):
        random_number = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield(random_number)
        