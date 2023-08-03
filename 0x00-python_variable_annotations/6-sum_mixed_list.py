#!/usr/bin/env python3
"""function that takes mixed list and returns a float"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """returns float"""
    return sum(mxd_list)
