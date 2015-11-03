#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def flip_keys(to_flip):
    """Docstring explaining the flip_keys function.

    Args:
        to_flip (): A list that has immutable and nested sequences.
    Returns:
         List (): returns original list with elements reversed.
    Examples:
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    counter = 0
    for num in to_flip:
        reverse = (num[::-1])
        to_flip[counter] = reverse
        counter += 1
    return to_flip

LIST = [(1, 2, 3), 'abc']
