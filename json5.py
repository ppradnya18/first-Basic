"""Write a Python program to access only unique key value of a Python object."""
import json
class check_json():
    print("inside the class")
    def __init__(self,input_json):
        print("iside the first methos")
        self.input_json=input_json

    def unique_json(self):
        print("iside the second methos")
        new_json=json.loads(self.input_json)
        print(new_json)



newcheck = check_json('{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}')
newcheck.unique_json()


