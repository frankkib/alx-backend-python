#!/usr/bin/env python3
"""Asynchronous function that takes no argument and loop 10 times
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """returns list of random floats"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
