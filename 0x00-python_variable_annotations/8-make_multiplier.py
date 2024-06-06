#!/usr/bin/env python3
""" This module defines a type-annotated function
that takes a float as argument and
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float as argument and
returns a function that multiplies a float by multiplier.

    Args:
            multiplier (float): the number to multiply with

    Returns:
            Callable[float]: a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
