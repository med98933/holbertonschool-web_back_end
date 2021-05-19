#!/usr/bin/env python3
""" a type-annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    return a sum of all nums inside a list
    """
    return sum(input_list)
