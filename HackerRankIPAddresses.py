# https://www.hackerrank.com/challenges/ip-address-validation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def is_ipv4(s):
    """
    returns True if s is of the form a1.a2.a3.a4
    where ai is a base ten integer in [0,255]

    Raises: 
        ValueError: if ai is cannot be converted to an int

    """
    regex4 = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    match4 = re.match(regex4, s)
    if not bool(match4): #doesn't fit the pattern
        return False
    else:
        int_lst = s.split(".")
        for i in int_lst:
            try:
                if int(i) > 255 or int(i) < 0: #not a valid int
                    return False
            except ValueError:
                return False # not a valid int
    return True # passed all tests!

def is_ipv6(s):
    """
    returns True if s is of the form
    a1:a2:a3:a4:a5:a6:a7:a8
    where ai is a hex int in [0000, ffff]

    case insensitive so F == f

    also valid to allow zeros to be dropped e.g. 
        0001 --> 1
        0025 --> 25
    and to allow for consecutive zeros to be dropped once
    e.g.
        ...0000:0000:... --> ...::...
    see this for more details:
    https://en.wikipedia.org/wiki/IPv6#Address_representation
    """
    regex6 = r"^[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}:[0-9a-fA-F]{0,4}$"
    match6 = re.match(regex6, s)
    if not bool(match6): # doesn't fit pattern
        return False

    hex_lst = s.split(":")
    n_empty = 0 # counter -- only one :: or address is indeterminate ie invalid
    for i in hex_lst:
        if not i: # empty string
            # TODO handle empty string
            if n_empty == 0:
                n_empty += 1
            else:
                return False # two :: or other invalid address
# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
        try:
            a = int(i, 16)
            if a > (2**16 - 1) or a < 0: # out of valid range for 16 bits
                return False
        except ValueError:
            return False # not convertable to a hex int
    return True # passed all tests 
         


n = int(input())

for i in range(n):
    line = input()
    
    if is_ipv4(line):
        print("IPv4")

    elif is_ipv6(line):
        print("IPv6")
    else:
        print("Neither")    

