#!/usr/bin/env python3
"""task 2"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ wait """
    start_time = time.time()
    return_list = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    #print(f"{sum(return_list)} /// {elapsed_time}")
    return elapsed_time / n