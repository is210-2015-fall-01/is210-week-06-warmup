#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def process_data(data):
    """a list or tuple of numbers.
    Args:
        The total sum of the data
    Return:
        The average of the data with floating point precision
     """
    total = 0
    for item in data:
        total += item
    average = total / float(len(data))
    return (total, average)
