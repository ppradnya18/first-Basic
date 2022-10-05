"""35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. """



from operator import truediv


def check_value(a,b):
    if a==b or a+b==5 or abs(a-b) == 5:
        return True
    return False


cr=check_value(5,10)
print(cr)