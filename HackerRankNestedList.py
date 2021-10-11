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
