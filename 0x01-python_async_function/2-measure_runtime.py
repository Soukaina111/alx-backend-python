#!/usr/bin/env python3
"""
Measures the total execution time for waiting on multiple coroutines concurrently.
"""
import asyncio
import time
from typing import Tuple
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> Tuple[float, List[float]]:
    """
    Measures the average time it takes to execute the `wait_n` function.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        Tuple[float, List[float]]: The average time per coroutine and the list of delays.
    """
    start_time = time.perf_counter()
    delays = await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n, delays
