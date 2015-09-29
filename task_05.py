#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mutability differences between strings and tuple"""


def flip_keys(to_flip):
    """A reversed list

    Args:
        to flip a list of numbers or letters.

         Returns:
              The function should return the original list.
    """
    counter = 0
    for values in to_flip:
        to_flip[counter] = values[::-1]
        counter += 1

        return to_flip
