#!/usr/bin/env python3
"""function that takes alist  and return a list"""
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[str]) -> Sequence[Tuple[str, int]]:
    """return list"""
    return [(i, len(i)) for i in list]
