#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def process_data(data):
    """Docstring explaining the process_data function.

    Args:
        data (): A list or tuple of numbers.
    Returns:
         Tup (): returns the average and total.

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)
    """
    total = 0
    average = 0
    for num in data:
        total += num
    average = total/float(len(data))
    return total, average
