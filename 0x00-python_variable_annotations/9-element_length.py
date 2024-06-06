#!/usr/bin/env python3
""" This module defines a type-annotated function
that takes an iterable of iterables as argument
and returns a list of tuples of the element and its length.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list of tuples of the element and its length

    Args:
        lst (Iterable[Sequence]): the list of sequences

    Returns:
        List[Tuple[Sequence, int]]: a list of tuples
        of the element and its length
    """
    return [(i, len(i)) for i in lst]
