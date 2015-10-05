#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provide mutability differences between strings"""


def flip_keys(to_flip):
    """This function return the original list in a reverse order

    Args:
        Return list.

    Return:
        Return list with revered elements.

    Example:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> mylist = flip_keys(LIST)
        >>> print mylist
        [(3, 2, 1), 'cba']
    """

    counter = 0

    for i in to_flip:
        to_flip[counter] = i[::-1]
        counter += 1

    return to_flip
