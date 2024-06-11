#!/usr/bin/env python3
""" measuring runtime for 4 async comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ collect 10 random numbers using an async comprehension
    over async_generator, then return the 10 random numbers. """

    start = time.time()
    await asyncio.gather(
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension())
        )
    runTime = time.time() - start
    return runTime
