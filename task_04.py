#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses for loop and loop"""


def process_data(data):
    """This function will return average and floating point precision"""

    total = 0
    for i in data:
        total += i

    return total, (total/float(len(data)))
