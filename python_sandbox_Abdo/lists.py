# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_ao = [1, 2, 3, 4, 5]
fruits_ao = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_ao[1])

# Get the last value
print(fruits_ao[-1])



# Get length
print(len(fruits_ao))

# Append to list
fruits_ao.append('Mangos')

# Remove from list
fruits_ao.remove('Grapes')

# Insert into position
fruits_ao.insert(2, 'Strawberries')

# Change value
fruits_ao[0] = 'Blueberries'

# Remove with pop
fruits_ao.pop(2)

# Reverse list
fruits_ao.reverse()

# Sort list
fruits_ao.sort()

# Reverse sort
fruits_ao.sort(reverse=True)

print(fruits_ao)
