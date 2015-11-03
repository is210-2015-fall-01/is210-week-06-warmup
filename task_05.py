#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mutability differences between strings and tuple"""


def flip_keys(to_flip):
    """Making my list flip

     Args:
        to_flip this list
      Returns:
        The function should return the original list
    """
    counter = 0
    for item in to_flip:
        to_flip[counter] = item[::-1]
        counter += 1
    return to_flip
