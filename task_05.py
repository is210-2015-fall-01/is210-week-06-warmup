#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Catch you on the flippty flip."""


def flip_keys(to_flip):
    """This will flip the data entered
    ARGS:
        to_flip(mixed): lists of numbers & letters
    RETURNS:
        Reversed entered data.
    EXAMPLES:
        >>> flip_keys(['civic', 'racecar', 'radar'])
            ['civic', 'racecar', 'radar']
    """
    count = 0
    for value in to_flip:
        to_flip[count] = value[::-1]
        count += 1
    return to_flip
