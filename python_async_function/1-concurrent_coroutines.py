#!/usr/bin/env python3
"""task 1"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ waait """
    return_list = []
    for i in range(n):
        return_list.append(await wait_random(max_delay))
    return sorted(return_list)