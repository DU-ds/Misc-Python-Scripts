


def checkCharacter(index, character):
   """checks for character(s) at specified location in the password 

   Args:
      index: integer representing the location in the password string to check for character
      character: a single character or group of characters to check

   Returns: 
      bool: boolean
         true iff character is found at index in the password string

   Raises:
      tbd -- needs to be updated later!

   """


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

def readQuery(query):
   """ reads the html returned by the query and determines if login was successful

   Args:
      query: String
         html result of a form submission -- from sqlzoo.net/hack

   Returns: boolean
      true iff login was successful

   Raises: tbd

   """



def constructPayload():
   """

   Args:
      

   Returns: 
      payload: dictionary 
         form parameters as keys and data to submit as values

   """   

