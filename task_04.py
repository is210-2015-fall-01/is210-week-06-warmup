#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses for loop and loop"""


def process_data(data):
    """This function will return average and floating point precision

    Args:
        data(int): Contains data in list format.

    Returns:
        total(int): Calculate total.
        average(int, float): Calculate average.

    Example:
        >>> process_data([1, 2, 3])
        (6, 2.0)
"""

    total = 0
    for i in data:
        total += i

    return total, (total/float(len(data)))
