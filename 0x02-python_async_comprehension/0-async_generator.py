#!/usr/bin/env python3
"""generator Creation"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that yields a random number {0-10}/sec x 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
