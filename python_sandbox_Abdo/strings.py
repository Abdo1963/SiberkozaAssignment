# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ao = 'Brad'
age_ao = 37

# Concatenate
print('Hello, my name is ' + name_ao + ' and I am ' + str(age_ao))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name_ao, age=age_ao))

# F-Strings (3.6+)
print(f'Hello, my name is {name_ao} and I am {age_ao}')

# String Methods

s_ao = 'helloworld'

# Capitalize string
print(s_ao.capitalize())

# Make all uppercase
print(s_ao.upper())

# Make all lower
print(s_ao.lower())

# Swap case
print(s_ao.swapcase())

# Get length
print(len(s_ao))

# Replace
print(s_ao.replace('world', 'everyone'))

# Count
sub = 'h'
print(s_ao.count(sub))

# Starts with
print(s_ao.startswith('hello'))

# Ends with
print(s_ao.endswith('d'))

# Split into a list
print(s_ao.split())

# Find position
print(s_ao.find('r'))

# Is all alphanumeric
print(s_ao.isalnum())

# Is all alphabetic
print(s_ao.isalpha())

# Is all numeric
print(s_ao.isnumeric())
