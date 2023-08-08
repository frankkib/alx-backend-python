#!/usr/bin/env python3
"""Asynchronous function returning alist of random numbers"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function returns list of sorted random numbers"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
