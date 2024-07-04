#!/usr/bin/env python3
"""
functions for complex types
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that return the product of floats
    """
    def multiplies(n: float):
        """
        multiply 2 number
        """
        return n * multiplier
    return multiplies
