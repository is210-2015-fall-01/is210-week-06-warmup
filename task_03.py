#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is an example of adding to a list."""

import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = DIRECTIONS[:len(DIRECTIONS)-1] + ('West',)
