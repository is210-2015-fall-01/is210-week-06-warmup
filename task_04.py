#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""

TOTAL_SUM = ['03', '19', '86']


def process_data(data):
    """The total sum of the data

    Args:
         data (mixed): A list or tuple of numbers.

         Returns:
             The average of the data with floating point precision
    """
    mytotalsum = (data)
    myavg = mytotalsum/float(len(data))
    return (mytotalsum, myavg)
