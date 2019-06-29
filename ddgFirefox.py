from sys import argv
import sys
import os
import subprocess
# https://docs.python.org/3/library/sys.html

# print(argv[1])

searchArr = argv[1:]

# search = argv[1]

# searchArr = search.split()
# https://stackoverflow.com/questions/17222355/string-split-formatting-in-python-3
# print (searchArr)
# print(searchArr[0])
# print(searchArr[len(searchArr) - 1])

# alternate way of creating strings with +
# query = "+"
# query = query.join(searchArr)
# print(query)

# create string with + seperating words
query = ""
for s in searchArr:
   # add control flow (eg an if statement) to deal with quotes and other options
   query += s + "+"


# https://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string
query = query[:-1] #get rid of trailing +

# print(query)
duckDuckGoURL = "https://duckduckgo.com/"
finalQuery = duckDuckGoURL + "?q=" + query


# https://stackoverflow.com/questions/39212541/unable-to-pipe-python-output-to-program
# import sys
print(finalQuery)
# sys.stdout.flush()

"""
Search:
string.join in python

URI:
https://duckduckgo.com/?q=string.join+in+python&t=lm&ia=web
"""



"""
bash var:

$USERINPUT
https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php
https://linuxtechlab.com/9-bash-scripting-user-input-read-command-redirection/
https://stackoverflow.com/questions/4651437/how-do-i-set-a-variable-to-the-output-of-a-command-in-bash


FIREURL=$(python3 ddgFirefox.py $USERINPUT)

"""


"""
next time:

figure out why firefox command isnt using piped url data to open url e.g.

python3 ddgFirefox.py "test my code" | firefox

opens default page
also tried 

python3 ddgFirefox.py "'test my code hehe'" > tmp.txt
firefox < tmp.txt

and 

python3 ddgFirefox.py "test my code" | firefox -search

and 

python3 ddgFirefox.py "test my code" | firefox -new-tab

for good measure


bash user input -- work around firefox pipe issue

control flow in search string for more complex searches
"""


# command = 'firefox %s' % finalQuery
command = ['firefox', finalQuery]

# command2 = 'firefox --search "%s"' search
# /usr/local/

# https://docs.python.org/3/library/subprocess.html
pop1 = subprocess.Popen(command)
# ps2 = subprocess.Popen(command2)
try:
   out1, err1 = pop1.communicate(timeout=12)
except TimeoutExpired:
   print("Timeout, try again.")
   pop1.kill


