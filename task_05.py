#!user/bin/env python
# -*- coding: utf-8 -*-
"""lists and tuples"""


def flip_keys(to_flip):
    """reverses individual elements within list.

    Returns:
        original list individual items reversed

    Examples:
        flip_keys(LIST)
        >>>[(3, 2, 1), 'cba']
    """

    counter = 0

    for item in to_flip:
        listvar = (item[::-1])
        to_flip[counter] = listvar
        counter += 1

    return to_flip


LIST = [(1, 2, 3), 'abc']

print flip_keys(LIST)
