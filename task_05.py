#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrating mutability by reversing a list with nested sequences."""


def flip_keys(to_flip):
    """Uses a for statement to reverse the elements within a list.

    Args:
        to_flip: a list containing nested, immutables sequences

    Returns:
        The reversed, mutable list to_flip

    Raises:
        TypeError: flip_keys() takes exactly 1 argument (x given)
        TypeError: 'int' object is not iterable
        NameError: name 'x' is not defined (List/tuple values must be numbers)
    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']

    """
    ind = 0
    for listup in to_flip:
        if isinstance(listup, int):
            to_flip[ind] = int(str(listup)[::-1])
        else:
            to_flip[ind] = listup[::-1]
        ind += 1
    return to_flip
