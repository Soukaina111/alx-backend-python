#!/usr/bin/env python3
"""2-Mesures time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension() four times in parallel and measures the total runtime.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = asyncio.get_running_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
