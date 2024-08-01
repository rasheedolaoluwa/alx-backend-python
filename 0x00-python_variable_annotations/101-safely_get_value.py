#!/usr/bin/env python3
""" More involved type annotations. """

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """ Safely returns the value for a key in a dictionary,
    or a default value if the key is not found. """
    if key in dct:
        return dct[key]
    return default
