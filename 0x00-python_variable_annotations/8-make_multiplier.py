#!/usr/bin/env python3
""" Complex types - functions. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument,
    and returns a function that multiplies a float by the multiplier.
    """
    def f(n: float) -> float:
        """ Multiplies a float by the multiplier. """
        return n * multiplier

    return f
