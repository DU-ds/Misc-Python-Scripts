# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:17:29 2018

@author: Kenneth Collins
"""

def reverseCoding(obj): 
    add = 1 + obj.max() #+1 so obj > 0
    obj *= -1
    obj += add
    return obj
""" reverseCoding(obj)
flips the ordering around then puts it back on the same scale
f: obj1 --> obj2
for all x1, y1 in {obj1} x2, y2 in {obj2} such that f(x1,y1) = (x2,y2), 
  (x1 >  y1) implies (x2 <  y2), 
  (x1 == y1) implies (x2 == y2), 
  (x1 <  y1) implies (x2 >  y2)
  MUTATES obj!!!!
"""