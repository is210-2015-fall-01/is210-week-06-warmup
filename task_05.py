#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w6 warmup task 05."""


def flip_keys(to_flip):
    """This function takes a list, and returns it reversed to test mutability

    Args:
        to_flip(list): neste list to be reveresed

    Returns:
        list returns the original nested list with the elements reversed

    Examples:
         >>> flip_keys([(1,2,3),'A,B,C'])
        [(3, 2, 1), 'C,B,A']
        >>> flip_keys[(3, 2, 1), 'cba']
        [(1, 2, 3), 'abc']
    """
    counter = 0
    for item in to_flip:
        to_flip[counter] = item[::-1]
        counter += 1
    return to_flip
