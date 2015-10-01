#!user/bin/env python
# -*- coding: utf-8 -*-
"""List of ballets"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = 'Swan Lake'

BALLETS.append('Herman Schmerman')

TWONEW = ('Don Quixote', 'Sylvia')

BALLETS.extend(TWONEW)
