#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the task_05 docstring."""


def flip_keys(to_flip):
    """This function reverses the srings (or elements) inside a list.

    Reverses only the elements iside the list, not the order in which
    they appear in the list.

    Args:
        A list (list): A list containing more than one element.

    Returns:
        The same list but with reversed elements.

    Example:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> mylist = flip_keys(LIST)
        >>> print mylist
        [(3, 2, 1), 'cba']

    """
    counter = 0
    for element in to_flip:
        to_flip[counter] = element[::-1]
        counter += 1
    return to_flip
