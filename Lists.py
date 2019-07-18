n = int(input())
lst = []

for i in range(0, n):
    s = input()
    if(s == "print"):
        print(lst)
    elif("insert" in s):
        s2 = s.split()
        lst.insert(int(s2[1]), int(s2[2]))
    elif("remove" in s):
        s2 = s.split()
        lst.remove(int(s2[1]))
    elif("append" in s):
        s2 = s.split()
        lst.append(int(s2[1]))
    elif("sort" in s) :
        lst.sort()
    elif("pop" in s):
        lst.pop()
    else : 
        lst.reverse()
  

# https://www.hackerrank.com/challenges/python-lists/problem
