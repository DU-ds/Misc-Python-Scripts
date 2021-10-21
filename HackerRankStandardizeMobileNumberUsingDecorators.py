# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
def wrapper(f):
    def fun(l):
        # complete the function
        l2 = []
        for e in l:    
            if len(e) == 10:
                l2.append(str("+91 " + e[:5] + " " + e[5:]))
            elif len(e) == 11:
                l2.append(str("+91 " + e[1:6] + " " + e[6:]))
            elif len(e) == 12:
                l2.append(str("+91 " + e[2:7] + " " + e[7:]))
            else:
                l2.append(str("+91 " + e[3:8] + " " + e[8:]))
        return f(l2)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# alternate answer:
def wrapper(f):
    def fun(l):
        # complete the function
        return f([ "+91 " + x[-10:-5] + " " + x[-5:] for x in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


