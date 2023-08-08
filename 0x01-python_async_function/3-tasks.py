#!/usr/bin/env python
"""Asyncchronous function that create a tasks"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a float object of asynchronous"""
    return asyncio.create_task(wait_random(max_delay))
