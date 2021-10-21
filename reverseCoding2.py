# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:18:02 2018

@author: Kenneth Collins
"""

def reverseCoding2(obj):
    temp = obj.copy() #more expensive because it copies obj
    add = 1 + temp.max()
    temp *= -1
    temp += add
    return temp
""" reverseCoding2(obj)
flips the ordering around then puts it back on the same scale
f: obj1 --> obj2
for all x1, y1 in {obj1} x2, y2 in {obj2} such that f(x1,y1) = (x2,y2), 
  (x1 >  y1) implies (x2 <  y2), 
  (x1 == y1) implies (x2 == y2), 
  (x1 <  y1) implies (x2 >  y2)
  Does not mutate obj passed as an arugment.
"""