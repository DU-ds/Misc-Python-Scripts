#!/bin/python3

# answer to this question:
# https://www.hackerrank.com/challenges/python-time-delta/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


from datetime import datetime as dtf #date time functionalities
# why import datetime from datetime?:
# datetime module has datetime class so datetime.datetime.* 
# https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime#19480045

def time_delta(t1, t2):
# datetime docs:
# https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime

# formatting:
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# Sun 10 May 2015 13:54:36 -0700
    form = "%a %d %b %Y %H:%M:%S %z"
    d1 = dtf.strptime(t1, form)
    d2 = dtf.strptime(t2, form)
    diff = abs(d1 - d2)
    return int(diff.total_seconds())

t = int(input())

for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)#end of loop

    # one = t1.split()
    # two = t2.split()
    # hourMinSec1 = one[4].split(sep = ":")
    # hourMinSec2 = two[4].split(sep = ":")

    # d1 = datetime.datetime(int(one[3]), one[2], int(one[1]), hour = int(hourMinSec1[0]), minute = int(hourMinSec1[1]), second = int(hourMinSec1[2]), tzinfo = one[5]) 
    # d2 = datetime.datetime(two[3], two[2], two[1], hour = hourMinSec2[0], minute = hourMinSec2[1], second = hourMinSec2[2], tzinfo = two[5])



# def timeZoneDiff(t1s, t2s)
#     print(t1s[5][0])
#     print(t2s[5][0])
#     if((t2s[5][0] == "-" and t1s[5][0] == "-") or (t2s[5][0] == "+" and t1s[5][0] == "+")): #signs match
#         zone = int(t1s[5][1:]) - int(t2s[5][1:])
#     else: #signs don't match -- wraps around 0
#         zone = int(t1s[5][1:]) + int(t2s[5][1:])
#     return zone;

# def yearConverter(year1, year2):
#     diff = year1 - year2
#     return diff * 365 * 24 * 60 * 60; #assumes neither has leap days -- must be accounted for elsewhere


# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     t1s = t1.split()
#     t2s = t2.split()

#     zone = timeZoneDiff(t1s, t2s)
#     diff = abs(int(t1s[1]) - int(t2s[1])) * 24 * 60 * 60 #diff of days in seconds
#     hourMinSec1 = t1s[4].split(sep=":")
#     hourMinSec2 = t2s[4].split(sep=":")
#     diff += int(hourMinSec1[0]) - int(hourMinSec2[0]) * 60 * 60
#     diff += int(hourMinSec1[1]) - int(hourMinSec2[1]) * 60
#     diff += int(hourMinSec1[2]) - int(hourMinSec2[2])

#     # diff += monthConverter() #converts difference between months
#     diff += yearConverter(int(t1s[3]), int(t2s[3]))
#     diff += zone
#     return str(diff)
    

    # diff += abs(t1s[] - t2s[])
    # print(t1.split()[5])
    # Sun 10 May 2015 13:54:36 -0700




# scratch work:
# t1 = +0500
# t2 = +0300

# 0200 = abs (0500-0300)
# means t1 is 2 hours ahead of t2


# t1 = -0200
# t2 = +0300

# diff = abs(0200 + 0300)
# means they are 5 hours apart

# t1 = -0500
# t2 = -0300
# diff = abs(0500-0300)
# means they are 2 hours apart

# t1 = +0400
# t2 = -1200
# diff = abs(1200 + 0400)
# means they are 16 hours apart
