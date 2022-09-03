"""Write a Python program to check whether a JSON string contains complex object or not."""

import json
class is_complex():
    def __init__(self):
        print("inside first methode __init__")

    def is_complex_num(objct):
        print("inside second methode __init__")
        if '__complex__' in objct:
            return complex(objct['real'], objct['img'])

        return objct

    def print_ans(self):
        print("inside third methode __init__")
        complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook =self.is_complex_num)
        simple_object =json.loads('{"real": 4, "img": 3}', object_hook = self.is_complex_num)
        print("Complex_object: ",complex_object)
        print("Without complex object: ",simple_object)




lp = is_complex("4+5j")
lp.is_complex_num()
lp.print_ans()

