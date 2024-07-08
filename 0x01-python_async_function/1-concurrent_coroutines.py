#!/usr/bin/env python3
"""This code demonstrates how to execute multiple coroutines concurrently in Python"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random coroutines n times with the specified max_delay,
and returns the list of all the delays (float values) in the order they completed.."""
    nextones = [wait_random(max_delay) for _ in range(n)]
    nextones = asyncio.as_completed(futures)
    retards = [await e for e in nextones]
    return retards
