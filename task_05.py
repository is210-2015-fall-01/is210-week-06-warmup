#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability in a list and immutability in a tuple"""


def flip_keys(to_flip):
    """This function will use flip lists backwards.

    Args:
        It takes one argument, a list called 'to_flip'

    Returns:
        A flipped tuple of numbers and a reversed string.

    Examples:
        >>> [(1, 2, 3, 4), 'abc']
            [(4, 3, 2, 1), 'cba']
    """
    print to_flip
    counter = 0
    for loop1 in to_flip:
        to_flip[counter] = loop1[::-1]
        counter += 1
    return to_flip

print flip_keys([(1, 2, 3, 4), 'abc'])
