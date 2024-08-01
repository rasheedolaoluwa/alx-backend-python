#!/usr/bin/env python3

""" Mixed list of integers and floats. """

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of a mixed list as a float. """
    return float(sum(mxd_lst))
