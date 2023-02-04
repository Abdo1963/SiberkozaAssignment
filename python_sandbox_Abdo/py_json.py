# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_ao = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON_ao)

# print(user)
# print(user['first_name'])

car_ao = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_ao = json.dumps(car_ao)

print(carJSON_ao)