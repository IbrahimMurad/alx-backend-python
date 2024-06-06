#!/usr/bin/env python3
""" This module contains a function
that safely retrieves value from a dictionary.
"""

from typing import Union, Any, Mapping, TypeVar


def safely_get_value(
                    dct: Mapping[Any, Union[Any, TypeVar('T')]],
                    key: Any,
                    default: Union[TypeVar('T'), None] = None
                    ) -> Union[Any, TypeVar('T')]:
    """ Return the value linked to key in dct,
    or default if key doesn't exist. """
    if key in dct:
        return dct[key]
    else:
        return default
