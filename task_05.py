#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provide mutability differences between strings"""


def flip_keys(to_flip):
    """This function return the original list in a reverse order"""

    counter = 0

    for i in to_flip:
        to_flip[counter] = i[::-1]
        counter += 1

    return to_flip
