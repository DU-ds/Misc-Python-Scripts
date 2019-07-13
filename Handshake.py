#!/bin/python3

# https://www.hackerrank.com/challenges/handshake/problem

def factorial(n):
    prod = 1
    i = n
    while(i > 1):
        prod *= i
        i -= 1
    return prod

#
# Complete the handshake function below.
#
def handshake(n):
    # n choose 2
    # return factorial(n)/(factorial(2)*factorial(n-2))
    return n*(n-1)/2 #simplified

t = int(input())

while(t > 0):
    n = int(input())
    print(int(handshake(n)))
    t -= 1

