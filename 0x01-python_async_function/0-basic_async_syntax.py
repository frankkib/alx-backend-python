#!/usr/bin/env python3
"""Asynchronous function that takes one int argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
