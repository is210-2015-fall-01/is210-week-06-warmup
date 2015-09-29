#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w6 warmup task 04."""


def process_data(data):
    """This is a fuction that returns the sum of data and the avg

    Args:
        data(list): a group of numbers

    Retruns:
        A tuple that contains the total and the average.

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)
        >>>process_data([1, 2, 3, 4, 5])
        (15, 3.0)

    """
    total = 0
    for i in data:
        total = total+i

    average = total/float(len(data))

    return total, average
