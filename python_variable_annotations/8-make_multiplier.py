#!/usr/bin/env python3
""" task 8 """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def multiplier_function(number: float) -> float:
        """mult function"""
        return number * multiplier
    return multiplier_function