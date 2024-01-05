#!/usr/bin/env python3
""" task 8 """

from typing import List, Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]