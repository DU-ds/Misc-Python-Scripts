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
"""#commented so I don't keep reruniing it
gssdf2.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/GSSVariableSubset4.txt", sep = "|", index = False )
"""
#oops, wrote to wrong file. Changed file name and code to coresspond ESS --> GSS
gssdf3 = pd.read_table("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/GSSVariableSubset4.txt", sep = "|")
gssdf3.head()
gssdf3.dtypes
gssdf3["gssOrEss"] = 1
#make same column name in ess DataFrame and assign Ess.gssOrEss to 2
gssdf3.gssOrEss.mean() #1
gssdf3.gssOrEss.std() #0

gssdf3.dtypes
essdf1.dtypes
#essdf2 = essdf1.copy()
"""
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
"""
essdf1.columns
essdf1 = essdf1.rename(index = str, columns = {"gndr" : "sex", "hinctnt" : "income" } )
"""
essdf1.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset4.txt", sep = "|", index = False )
#commented so I don't keep reruniing it"""
"""
essdf2["sex"]  =  essdf1.gndr.copy()
essdf2["income"] = essdf1.hinctnt.copy()
"""
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
essdf1["gssOrEss"] = 2
essdf1.columns
#essdf2 = essdf2.drop(['hinctnt','gndr'], axis = 1) #pobably should've renamed the columns instead
"""
BOTH : need to recode tax vars to a compatible coding scheme
BOTH : need to make sure sex vars are both coded the same
ESS  : need to recode essround to the corresponding year
GSS  : need to figure out income vs rincome
"""
"""
Income:  In which of these groups did your total family income, from all sources, fall last year before taxes, that is? Just tell me the letter
Rincome: Did you earn any income from (OCCUPATION DESCRIBED IN OCC-INDUSTRY) in [the previous year]?
"""

gssdf4 = gssdf4.drop(["rincome"], axis = 1)

"""
http://nesstar.ess.nsd.uib.no/webview/index.jsp?v=2&submode=variable&study=http%3A%2F%2F129.177.90.83%3A-1%2Fobj%2FfStudy%2FESS2e03.5&gs=undefined&variable=http%3A%2F%2F129.177.90.83%3A80%2Fobj%2FfVariable%2FESS2e03.5_V213&mode=documentation&top=yes
search term : essround
 ESS1-2002, ed.6.5
  ESS2-2004, ed.3.5
  ESS3-2006, ed.3.6
  ESS7-2014, ed.2.1
  ESS6-2012, ed.2.3
  ESS8-2016, ed.2.0
  ESS4-2008, ed.4.4
  ESS5-2010, ed.3.3
"""
essdf1.mean()
essdf1["essround" ] = 2004

""" GSS: Sex
Male 1
Female 2
"""
"""
ESS : gndr
1	Male	
2	Female
9  	No answer
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
"""
reverseCoding(gssdf4.paytaxes)
don't run this funtion multiple times
"""
gssdf4.paytaxes = reverseCoding2(gssdf4.paytaxes)
essdf1 = essdf1.rename({ "ctzchtx" : "paytaxes"} ,axis = "columns")


"""
essdf1.pweight.std()
Out[39]: 9.332080311636187e-15

essdf1.pweight.mean()
Out[40]: 3.2484026000000097

essdf1.pweight.min()
Out[41]: 3.2484026000000004

essdf1.pweight.max()
Out[42]: 3.2484026000000004
Consistent with my expectation from the documentation
given it only contains data from Italy
"""

gssdf5 = gssdf4.drop( columns = ["wtssall", "wtss"]) 
#I prefer this way of dropping, easier to understand without reading the documentation
essdf2 = essdf1.drop(columns = ["pweight","dweight"] )
"""
gssdf5.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/GSSVariableSubset5.txt", sep = "|", index = False )
essdf2.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset5.txt", sep = "|", index = False )
#commented so it doesn't keep running
"""
gssdf5 = pd.read_table("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/GSSVariableSubset5.txt", sep = "|")
essdf2 = pd.read_table("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSVariableSubset5.txt", sep = "|")
gssdf5 = gssdf5.rename({"wtssnr" : "weight"}, axis = "columns")
essdf2 = essdf2.rename({ "essround" : "year", "pspwght" : "weight"}, axis = "columns")

essdf2.columns == gssdf5.columns
#names line up now!

"""
Now I need to merge the data sets and run the models. maybe run em in python? 
https://pandas.pydata.org/pandas-docs/stable/merging.html
"""

essgssdf1 = pd.concat([essdf2, gssdf5], keys = ["ess", "gss"])
essgssdf1.year.size == (essdf2.year.size + gssdf5.year.size) # true, same sizes
essgssdf1.columns == essdf2.columns #true
essdf2.columns == gssdf5.columns    #true
"""
essgssdf1.to_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSGSSCombinedDataset1.txt", sep = "|", index = False)
#commenting so it doesn't keep running
"""
df1 = pd.read_csv("R:/R_WD/Thesis/JustDeserts/WorldValuesSurvey/ESSGSSCombinedDataset1.txt", sep = "|")
"""
looks like python only has one implementation for ordered logit
the statsmodels hasn't implemented it, but it has most of the other GLM models I'm used to
"""


