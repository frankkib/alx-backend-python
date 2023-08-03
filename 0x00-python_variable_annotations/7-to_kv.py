#!/usr/bin/env python3
"""function that returns A tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple of a string and float"""
    return (k, v**2)
