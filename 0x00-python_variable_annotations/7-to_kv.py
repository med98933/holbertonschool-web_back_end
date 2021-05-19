#!/usr/bin/env python3
""" a type-annotated function to_kv """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
 cast to tuple
    """
    return (k, v ** 2)
