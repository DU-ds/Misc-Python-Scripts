# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:15:01 2018

@author: Kenneth Collins
"""

"""

https://pandas.pydata.org/pandas-docs/stable/io.html

"""

import pandas as pd
import numpy as np

essdf1 = pd.read_table( "R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset3.txt", sep = "|" )
gssdf1 = pd.read_table( "R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/GSSVariableSubset3.txt", sep = "|" )

essdf1 = pd.DataFrame(essdf1)
gssdf1 = pd.DataFrame(gssdf1)
essdf1.head()
gssdf1.head()


gssdf1.dtypes
essdf1.dtypes

"""
https://stackoverflow.com/questions/34794067/how-to-set-a-cell-to-nan-in-a-pandas-dataframe
do not look at accepted answer, another one is better :)
"""
gssdf1.rincome  = pd.to_numeric(gssdf1["rincome"], errors="coerce")
gssdf1.income   = pd.to_numeric(gssdf1["income"], errors="coerce")
gssdf1.age      = pd.to_numeric(gssdf1["age"], errors="coerce")
gssdf1.cohort   = pd.to_numeric(gssdf1["cohort"], errors="coerce")
gssdf1.paytaxes = pd.to_numeric(gssdf1["paytaxes"], errors="coerce")
#some values are text strings, some are numbers stored as strings. converts to numbers and other strings to NaN
gssdf2 = gssdf1.dropna()
#drops the NaN values

gssdf1.rincome.size
gssdf2.ndim
gssdf2.rincome.size
gssdf2.rincome.size == gssdf2.size / gssdf2.columns.size
gssdf2.dtypes
gssdf2.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset4.txt", sep = "|", index = False )

gssdf3 = pd.read_table("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset4.txt", sep = "|")
gssdf3.head()
gssdf3.dtypes
gssdf3["gssOrEss"] = 1
#make same column name in ess DataFrame and assign Ess.gssOrEss to 2
gssdf3.gssOrEss.mean() #1
gssdf3.gssOrEss.std() #0

gssdf3.dtypes
essdf1.dtypes
essdf2 = essdf1.copy()
essdf2["sex"]  =  essdf1.gndr.copy()
essdf2["income"] = essdf1.hinctnt.copy()

"""
In [79]: essdf1.columns.size
Out[79]: 8

In [80]: gssdf1.columns.size
Out[80]: 10

In [81]: gssdf1.columns
Out[81]: 
Index(['paytaxes', 'sex', 'cohort', 'age', 'income', 'rincome', 'year',
       'wtssall', 'wtssnr', 'wtss'],
      dtype='object')

In [82]: essdf1.columns
Out[82]: 
Index(['ctzchtx', 'gndr', 'age', 'hinctnt', 'essround', 'dweight', 'pweight',
       'pspwght'],
      dtype='object')
"""

"""
gssdf3.cohort.mean()
Out[84]: 1965.214240705734

essdf1.age.mean()
Out[85]: 47.86436170212766

gssdf3.age.mean()
Out[86]: 43.278512917454314
drop cohort
https://stackoverflow.com/questions/34682828/pandas-extracting-specific-selected-columns-from-a-dataframe-to-new-dataframe
"""

gssdf4 = gssdf3.drop(["cohort"], axis = 1)
gssdf4.columns #no more cohort column
essdf2["gssOrEss"] = 2
essdf2.columns
essdf2 = essdf2.drop(['hinctnt','gndr'], axis = 1) #pobably should've renamed the columns instead




"""
https://pandas.pydata.org/pandas-docs/stable/merging.html
"""



