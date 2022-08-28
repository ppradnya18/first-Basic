""" Write a Python program to sum of three given integers. However, if two values are equal sum will be zero."""


def check_num(a,b,c):
    if a==b or b==c or c==a:
        return 0

    else :
        return a+b+c


c=check_num(2,3,2)
print(c)