# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 00:27:32 2018

"""
#bisection method for finding roots, inspired by the python script fron the brilliant.org wiki

def bisection(f, a, b, n): #f is a (continous and differentiable (at least on [a,b]) function, a is the lower bound of the range to search, b is the upper bound of the range to search, n is the number of itterations to bisect
  mid = (a + b) / 2
  for i in range(0,n):#remember, a must be negative and b must be positive since we're finding roots (where the funtion eqauls 0) here
    if f(mid) < 0:
        a = mid
    else:
        b = mid
    mid = (a + b) / 2
  return mid
"""creating a lambda function in R:
    function(x){f(x)} for whatever f(x) is. e.g. function(z){1/(exp(-1 * z)+1)}
   creating a lambda function in Python:
       lambda x: f(x) for whatever f(x) is e.g. lambda s: s**2 - 2 * s + 4 - sin(s)
"""
from math import e
from math import sin
"""specific problem that needed solving:
    one of the roots of 3 * x + sin(x) - e ** x = 0 lies between 0 and 1. If we apply the bisection method 5 times, which of the following intervals will we end up with?

"""
 bisection(lambda x: 3 * x + sin(x) - e ** x, 0, 1, 5)
 #so, it only prints out one number (the approximation). Let's alter the funtion so it spits out the other values as it goes
 
def bisectionFountain(f, a, b, n): #f is the (continous and differentiable (at least on [a,b]) function, a is the lower bound of the range to search, b is the upper bound of the range to search, n is the number of itterations to bisect
  mid = (a + b) / 2
  for i in range(0,n):#remember, a must be negative and b must be positive since we're finding roots (where the funtion eqauls 0) here
    print(mid)
    if f(mid) < 0:
      a = mid
    else:
      b = mid
    mid = (a + b) / 2
  return mid
 
 
    
#ok, let's run it with the new function
bisectionFountain(lambda x: 3 * x + sin(x) - e ** x, 0, 1, 5)


list[] a = bisectionFountain(lambda x:  x * sin(x) )
print a