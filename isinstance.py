"""Write a Python program to add two objects if both objects are an integer type."""

def check_instance(a,b):
    if not isinstance(a,int) and isinstance(b,int):

        return "It is not integer"
    c=a+b
    print(c)
    return a+b


