#!/usr/bin/env python3
""" This module defines a type-annotated function
which takes a list of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list of integers and floats and returns their sum as a float

    Args:
        mxd_lst (List[Union[int, float]]): the list to get its sum

    Returns:
        float: the sum of the passed list
    """
    return sum(mxd_lst)
