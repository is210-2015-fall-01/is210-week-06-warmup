#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def process_data(data):
    """The total sum of the data

    Args:
         data (mixed): A list or tuple of numbers.

         Returns:
             The average of the data with floating point precision

    """
    total = 0
    for i in data:
        total = total+i
        

        average = total/float(len(data))

    return total, average
