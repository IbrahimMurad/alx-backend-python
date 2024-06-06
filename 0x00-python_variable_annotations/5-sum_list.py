#!/usr/bin/env python3
""" This module defines a type-annotated function
which takes a list of floats and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of a list of floats

    Args:
        input_list (list[float]): the list to get its sum

    Returns:
        float: the sum of the list
    """
    return sum(input_list)
