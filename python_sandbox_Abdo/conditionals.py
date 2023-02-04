# If/ Else conditions are used to decide to do something based on something being true or false

x_ao = 21
y_ao = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ao > y_ao:
  print(f'{x_ao} is greater than {y_ao}')

# If/else
if x_ao > y_ao:
  print(f'{x_ao} is greater than {y_ao}')
else:
  print(f'{y_ao} is greater than {x_ao}')  

# elif
if x_ao > y_ao:
  print(f'{x_ao} is greater than {y_ao}')
elif x_ao == y_ao:
  print(f'{x_ao} is equal to {y_ao}')  
else:
  print(f'{y_ao} is greater than {x_ao}')  

# Nested if
if x_ao > 2:
  if x_ao <= 10:
    print(f'{x_ao} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_ao > 2 and x_ao <= 10:
    print(f'{x_ao} is greater than 2 and less than or equal to 10')

# or
if x_ao > 2 or x_ao <= 10:
    print(f'{x_ao} is greater than 2 or less than or equal to 10')

# not
if not(x_ao == y_ao):
  print(f'{x_ao} is not equal to {y_ao}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_ao = [1,2,3,4,5]

#  in
if x_ao in numbers_ao:
  print(x_ao in numbers_ao)

# not in
if x_ao not in numbers_ao:
  print(x_ao not in numbers_ao)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_ao is y_ao:
  print(x_ao is y_ao)

# is not
if x_ao is not y_ao:
  print(x_ao is not y_ao)