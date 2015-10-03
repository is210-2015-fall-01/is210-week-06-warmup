#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Altering an existing list."""


import data

BALLETS = data.BALLETS

del data.BALLETS[11]
data.BALLETS[1] = ('Swan Lake'[:9])
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
