#!/usr/bin/env python3
"""Asynchronous function for time measurement"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the time taken for async comprehensions"""
    start_time = perf_counter()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
