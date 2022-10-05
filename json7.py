
"""Write a Python program to convert JSON encoded data into Python objects."""
import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
python_dict =  json.loads(jobj_dict)
python_list = json.loads(jobj_list)
python_str =  json.loads(jobj_string)
python_int =   json.loads(jobj_int)
python_float = json.loads(jobj_float)


print(python_list)
print(type(python_dict))