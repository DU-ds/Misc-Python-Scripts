# https://www.hackerrank.com/challenges/maximize-it/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = map(int, input().split())
import itertools
lines = []
for i in range(k):
    l = list(map(int,input().split()))[1:] # discard N_i, can take len of lines[i] if needed
    lines.append(l)

def sum_of_squares(*vals):
    total = 0
    for num in vals:
        total += num ** 2
    return total
    

tups = itertools.product(*lines)
biggest = 0
for t in tups:
    s2 = sum_of_squares(*t) % m
    biggest = max(biggest, s2) 
    
print(biggest)
