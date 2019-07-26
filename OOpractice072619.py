class User:


   def __init__(self, name, password, age):
      self.name = name
      self.password = password
      self.age = age

   def login(self):
      print(self.name + " " + self.password)

   def birthday(self):
      self.age += 1
