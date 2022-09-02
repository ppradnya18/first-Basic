"""9. Write a Python program to access only unique key value of a Python object."""


input_json = '{"a":1,"b":2,"c":3,"d":4,"a":3}'


import json
print(type(input_json))
input_json1=json.loads(input_json)

print(input_json1)
