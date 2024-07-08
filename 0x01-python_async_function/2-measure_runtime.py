#!/usr/bin/env python3
""" This function measures the total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function returns total_time / n"""
    a_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    b_time = time.perf_counter()
    return (b_time - a_time) / n
