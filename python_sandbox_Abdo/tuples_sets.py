# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_ao = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2_ao = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_ao = ('Apples',)

# Get value
print(fruits_ao[1])

# Can't change value
fruits_ao[0] = 'Pears'

# Delete tuple
del fruits2_ao

# Get length
print(len(fruits_ao))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_ao = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_ao)

# Add to set
fruits_set_ao.add('Grape')

# Remove from set
fruits_set_ao.remove('Grape')

# Add duplicate
fruits_set_ao.add('Apples')

# Clear set
fruits_set_ao.clear()

# Delete
del fruits_set_ao

print(fruits_set_ao)
