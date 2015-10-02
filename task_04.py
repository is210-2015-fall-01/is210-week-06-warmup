#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping a list"""


def process_data2(data):
    """This function will take any list of numbers, sum and average them.

    Args:
        It takes one argument, a list called 'data', containing the list

    Returns:
        Total of the list, and it's average in floating point.

    Examples:
        >>> 
        (21, 3.5)
    """
    total_sum = 0
    count = 0
    for list_item in data:
        total_sum += list_item
        count += 1
    average = float(total_sum)/count
    return (total_sum, average)

print process_data2([1, 2, 3, 4, 7, 4])
