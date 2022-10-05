"""Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20."""



def check_num(a,b):
    if a+b > 15 and a+b<20:
        return 20
    return "number is not in between 20 and 15"




sd=check_num(8,20)
print(sd)