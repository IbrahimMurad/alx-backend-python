#!/usr/bin/env python3
"""
This module contains a function that safely retrieves value from a dictionary.
"""
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(
                    dct: Mapping[Any, Union[Any, T]],
                    key: Any,
                    default: Union[T, None] = None
                    ) -> Union[Any, T]:
    """ Return the value linked to key in dct,
    or default if key doesn't exist. """
    if key in dct:
        return dct[key]
    else:
        return default
