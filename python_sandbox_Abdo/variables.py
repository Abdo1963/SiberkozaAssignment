# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_ao = 1           # int
# y_ao = 2.5         # float
# name_ao = 'John'   # str
# is_cool_ao = True  # bool

# Multiple assignment
x_ao, y_ao, name_ao, is_cool_ao = (1, 2.5, 'John', True)

# Basic math
a_ao = x_ao + y_ao

# Casting
x_ao = str(x_ao)
y_ao = int(y_ao)
z_ao = float(y_ao)

print(type(z_ao), z_ao)
