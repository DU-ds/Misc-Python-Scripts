# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://docs.python.org/3/library/stdtypes.html#set
# https://www.hackerrank.com/challenges/py-set-add/problem?h_r=next-challenge&h_v=zen
n = int(input())
s = set()

for i in range(0, n):
    s.add(input())

m = len(s)
print(m)

