"""1. Write a Python program to convert JSON data to Python object. Go to the editor"""



import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)

print(python_obj["Name"])


