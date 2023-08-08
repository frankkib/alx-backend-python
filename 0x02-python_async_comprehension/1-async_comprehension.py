#!/usr/bin/env python3
"""Asyncgronous function comprehention"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """returns asynchronous generator"""
    return [i async for i in async_generator()]
