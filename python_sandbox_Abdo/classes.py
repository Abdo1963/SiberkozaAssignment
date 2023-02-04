# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User_ao:

  # Constructor
  def __init__(self, name, email, age):
    self.name_ao = name
    self.email_ao = email
    self.age_ao = age
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name_ao} and I am {self.age_ao}'

  def has_birthday(self):
      self.age += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User_ao):
  # Constructor
  def __init__(self, name, email, age):
      User_ao.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name_ao= name
      self.email_ao = email
      self.age_ao = age
      self.balance_ao = 0

  def set_balance(self, balance):
      self.balance_ao = balance

  def greeting(self):
      return f'My name is {self.name_ao} and I am {self.age_ao} and my balance is {self.balance_ao}'

#  Init user object
brad = User_ao('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())

#Encapsulation -->
brad.print_encap()
brad._private = 800 #Changing for brad
brad.print_encap()

# Method inherited from parent
janet.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet._private = 600
janet.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad.print_encap()
