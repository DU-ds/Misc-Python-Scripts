# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:16:59 2018

@author: Kenneth Collins
"""

"""colRecoder(dataFrame, colNameString, oldVal, newVal:)
requires: pandas dataFrame, colNameString must be a string (obviously)
effects: returns a copy of the column. Does NOT mutate data.
Thus must be assigned to change data.
"""
def colRecoder(dataFrame, colNameString, oldVal, newVal):
    columnCopy = dataFrame[colNameString].copy()
    columnCopy[oldVal] = newVal
    return columnCopy
