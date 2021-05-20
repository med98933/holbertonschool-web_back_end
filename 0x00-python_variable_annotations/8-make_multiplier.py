#!/usr/bin/env python3
""" a type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float
    """
    def g(x):
        """
        multiply two number
        """
        return x * multiplier
    return g
