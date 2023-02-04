# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ao = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_ao in people_ao:
  print(f'Current Person: {person_ao}')

# Break
for person_ao in people_ao:
  if person_ao == 'Sara':
    break
  print(f'Current Person: {person_ao}')

# Continue
for person_ao in people_ao:
  if person_ao == 'Sara':
    continue
  print(f'Current Person: {person_ao}')

# range
for i in range(len(people_ao)):
  print(people_ao[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_ao = 0
while count_ao < 10:
  print(f'Count: {count_ao}')
  count_ao += 1