#!/usr/bin/env python3
""" concurrent coroutines
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with the specified max_delay.
    and returns the list of all the delays (float values).
    The list of the delays should be in ascending order """
    delay_list = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
        )
    return delay_list
