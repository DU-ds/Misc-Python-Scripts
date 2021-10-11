# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = [ "" for i in range(m) ]


for _ in range(n):
    matrix_item = input()
    for i in range(len(matrix_item)):
        matrix[i] += matrix_item[i]

out = ""
for s in matrix:
    out += s
out = re.sub(r"(\w)\W+(\w)", r"\1 \2", out)
print(out)