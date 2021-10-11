# https://www.hackerrank.com/challenges/nested-list/problem
import sys
if __name__ == '__main__':
    low = sys.maxsize -1
    low2 = sys.maxsize
    names = []
    names2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < low:
            low2 = low
            names2 = names
            low = score
            names = [name]
        elif score == low:
            names.append(name)
        elif score < low2:
            low2 = score
            names2 = [name]
        elif score == low2:
            names2.append(name)
    names2.sort()
    for n in names2:
        print(n)


# alternative implementation
import sys
if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
    lst = sorted(lst, key=lambda x: x[0])
    lst = sorted(lst, key=lambda x: x[1]) 
    # sorts are stable, so name order is preserved when sorting by score
    low = lst[0][1] # get lowest score
    minsize = -1*sys.maxsize
    low2 = minsize
    for i in lst:
       if low2 > minsize and low2 < i[1]:
            break
       elif low2 > minsize and low2 == i[1]:
            print(i[0])
       elif low < i[1]: # higher than lowest score
            low2 = i[1]
            print(i[0])