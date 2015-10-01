#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Sum and average."""


def process_data(data):
    """Gives total sum and average of the data with floating point precision
    ARGS:
        data(mixed): Enter list or tuple of numbers.
    RETURNS:
        The sum of all numbers & average.
    EXAMPLE:
        >>> process_data([1, 2, 3])
        (6, 2.0)
        >>> process_data([9, 10, 11])
        (30, 10.0)
    """
    total = 0
    for value in data:
        total += value
    return total, (total/float(len(data)))
