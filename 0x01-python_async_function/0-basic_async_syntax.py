#!/usr/bin/env python3
"""This function defines an asynchronous coroutine for a random number """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function waits for a random delay between 0 and a maximum time"""
    aleatoire = random.uniform(0, max_delay)
    await asyncio.sleep(aleatoire)
    return aleatoire
