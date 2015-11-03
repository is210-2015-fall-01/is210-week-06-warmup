#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the task_04 docstring."""


def process_data(data):
    """Docstring for the module.

    This function takes numbers and calculates the total and average adn
    returns them in a tuple.

    Args:
        data (int): A list consisting of 'int' data types.

    Returns:
        total (int): The total of all numbers.
        average (float): Average of all numbers in float (2 sigfigs).

    Example:
        >>> process_data([2, 3, 4])
        (9, '3.0')

    """
    total = 0
    for number in data:
        total += number
    results = (total, total/float(len(data)))
    return results
