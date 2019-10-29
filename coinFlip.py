# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:01 2019

@author: Kenneth Collins
"""

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
    