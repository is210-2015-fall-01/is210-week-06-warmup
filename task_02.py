#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Altering an existing list."""


import data

BALLETS = data.BALLETS

del data.BALLETS[11]
data.BALLETS[2] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
NEWLIST = [('DonQuixote', 'Sylvia')]
BALLETS.extend(NEWLIST)
