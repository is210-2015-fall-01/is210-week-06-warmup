#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module demonstrates tuple math."""


def process_data(data):
    """Uses a for statement to do tuple math, including sum and average.

    Args:
        data: a list or tuple of numbers

    Returns:
        A tuple containing the sum and the average of the values in a tuple

    Raises:
        TypeError: process_data() takes exactly 1 argument (x given)
        TypeError: 'int' object is not iterable
        NameError: name 'x' is not defined (List/tuple values must be numbers)
    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)
        >>> process_data((2, 4, 6, 7))
        (19, 4.75)
    """
    datasum = 0
    dataavg = 0
    for item in data:
        datasum += item
    dataavg = float(datasum) / len(data)
    return (datasum, dataavg)
