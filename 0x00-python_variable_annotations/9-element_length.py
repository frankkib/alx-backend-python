#!/usr/bin/env python3
"""function that takes alist  and return a list"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list"""
    return [(i, len(i)) for i in list]
