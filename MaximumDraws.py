#!/bin/python3

# https://www.hackerrank.com/challenges/maximum-draws/problem

#
# Complete the maximumDraws function below.
#
def maximumDraws(n):
    return n+1
    # with n pairs of socks, if one were to pull
    # n non-matching socks out then the next must match


t = int(input())

while (t > 0):

    n = int(input())
    print(maximumDraws(n))

    t -= 1
