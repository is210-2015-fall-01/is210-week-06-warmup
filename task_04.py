#!user/bin/env python
# -*- coding: utf-8 -*-
"""Using for loop"""


def process_data(data):
    """ returns as a tuple the sum and mean of list or tuple elements

    arguments:
        tup_sum: sum of the input dataset

        for loop: returns mean of sum of dataset

    returns:
        returns sum and mean as a tuple

    exampls:
        process_data([1, 2, 3])
        >>>(6, 2.0)
    """
    tup_sum = sum(data)

    for _ in [data]:
        tupval = tup_sum, float(tup_sum/float(len(data)))
        tupval = tuple(tupval)

    return tupval


print process_data([1, 2, 3])
