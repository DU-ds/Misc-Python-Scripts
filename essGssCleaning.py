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
gssdf2 = gssdf1.dropna()
gssdf1.rincome.size
gssdf2.ndim
gssdf2.rincome.size
gssdf2.rincome.size == gssdf2.size / gssdf2.columns.size
gssdf2.dtypes
gssdf2.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset4.txt", sep = "|", index = False )
gssdf3 = pd.read_table("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset4.txt", sep = "|")
gssdf3.head()












