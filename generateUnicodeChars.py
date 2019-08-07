s = []

# https://stackoverflow.com/a/4435194/

for i in range(0,int(1e3)): #1e3 == 10.0 ** 3
   s.append(chr(i))

s = "".join(s)

# made a blank file
# e.g. cat > ~/Documents/unicodeChars.txt
# ctrl-D

fileName = "unicodeChars.txt"

with open(fileName, 'wt') as o:
   o.write(s)


#if you need more characters, set n and run this:

n = 1e4 #1e4 == 10.0 ** 4

s = []

# https://stackoverflow.com/a/4435194/

for i in range(int(1e3),int(n)): 
   s.append(chr(i))

s = "".join(s)

# made a blank file
# e.g. cat > ~/Documents/unicodeChars.txt
# ctrl-D

fileName = "unicodeChars.txt"

with open(fileName, 'at') as o:
   o.write(s)


# to read the file:
with open(fileName, 'rt') as r:
   st = r.read()

 