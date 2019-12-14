# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:16:08 2018

@author: Kenneth Collins
"""
"""colRecoder2(dataFrame, colName, oldVal, newVal):
requires: pandas dataFrame, colName must be the columns name (e.g. df.colName), not a string 
effects: returns a copy of the column. Does NOT mutate data.
Thus must be assigned to change data.
"""

def colRecoder2(dataFrame, colName, oldVal, newVal):
    columnCopy = dataFrame.colName.copy()
    columnCopy[oldVal] = newVal
    return columnCopy