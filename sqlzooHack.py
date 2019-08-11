lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

# https://stackoverflow.com/questions/54621596/include-both-single-quote-and-double-quote-in-python-string-variable
# https://stackoverflow.com/questions/54620287/how-to-include-both-single-and-double-quotes-in-the-same-string-variable-in-pyth
special = {|}~[\]^_`!"#$%&'()*+,-./:;<=>?@)
# so use .join or """ i guess?

''.join("{|}~[\]^_`!#$%&'()*+,-./:;<=>?@)") + '"'

for ch in lower:
   # check for ch in 
   if(checkPasswordCharacter(ch, username, url)):
      # add it to the list

for ch in numbers:
   if(checkPasswordCharacter(ch, username, url)):
      # add it to the list

for ch in special:
   # check for ch in 
   if(checkPasswordCharacter(ch, username, url)):
      # add it to the list

for ch in upper:
   # check for ch in 
   if(checkPasswordCharacter(ch, username, url)):
      # add it to the list


