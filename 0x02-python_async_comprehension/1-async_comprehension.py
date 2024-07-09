#!/usr/bin/env python3
"""List from an async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random nums with an async comprehension
    over async_generator().
    """
    return [num async for num in async_generator()]
