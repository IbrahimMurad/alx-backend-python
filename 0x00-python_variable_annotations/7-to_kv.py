#!/usr/bin/env python3
""" This module defines a type-annotated function
that takes a string and an int OR float as arguments
and returns a tuple.
The first element of the tuple is the string.
The second element is the square of the int/float
and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple of the string and the number

    Args:
            k (str): the first element in the tuple
            v (Union[int, float]): the second element of the tuple

    Returns:
            Tuple[str, float]: a tuple of the string and the number
    """
    return (k, v * v)
