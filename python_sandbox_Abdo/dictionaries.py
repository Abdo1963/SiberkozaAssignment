# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_ao = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_ao['first_name'])
print(person_ao.get('last_name'))

# Add key/value
person_ao['phone'] = '555-555-5555'

# Get dict keys
print(person_ao.keys())

# Get dict items
print(person_ao.items())

# Copy dict
person2 = person_ao.copy()
person2['city'] = 'Boston'

# Remove item
del(person_ao['age'])
person_ao.pop('phone')

# Clear
person_ao.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
