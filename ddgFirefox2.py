from sys import argv
import sys
import os
import subprocess
# https://docs.python.org/3/library/sys.html


in1 = argv[1:]
# https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list

search = "--search '"

for s in in1:
   search.join(s)
   search.join(" ")

search[:-1] #remove trailing space
search.join("'")

command = ["firefox", search]
# , "--search"
# https://docs.python.org/3/library/subprocess.html
pop1 = subprocess.Popen(command)
try:
   out1, err1 = pop1.communicate(timeout=12)
except TimeoutExpired:
   print("Timeout, try again.")
   pop1.kill


