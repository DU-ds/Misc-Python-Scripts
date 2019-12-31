# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://docs.python.org/3/library/stdtypes.html#set
# https://www.hackerrank.com/challenges/no-idea/problem
def happyness(A, B, n):
    sum = 0
    for i in range(0, n):
        e = lst[i]
        if(e in A):
            sum += 1
        if(e in B):
            sum -= 1
    return sum;



n, m = input().split()
lst = input().split() 
a = input().split()
b = input().split()
A = set(a)
B = set(b)

happy = happyness(A, B, int(n))


print(happy)
