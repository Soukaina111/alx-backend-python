#!/usr/bin/env python3
"""This function do  multiple coroutines at the same time """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """this function create spawns that  wait_random n times with the specified max_delay
        and returns the list of all the delays in a float format."""
    prochains = [task_wait_random(max_delay) for _ in range(n)]
    prochains = asyncio.as_completed(prochains)
    retards = [await p for p in prochains]
    return retards
