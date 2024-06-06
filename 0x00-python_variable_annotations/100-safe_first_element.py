#!/usr/bin/env python3
""" This module defines a type-annotated function
that takes a sequence of any type as input
and returns the first element in the sequence or none.
"""
from typing import Any, Sequence, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Takes a sequence of any type as input and
    returns the first element in the sequence or none."""
    if lst:
        return lst[0]
    else:
        return None
