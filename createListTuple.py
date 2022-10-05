"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers."""

#Part 1
def createList(lis):
    liss=list(lis)
    return liss

def createTuple(tupp):
    tup=tuple(tupp)
    return tup
sd=createList([3,4,5,6,7,7])
print(sd)
dd=createTuple([8,4,5,6,7,8])
print(dd)



#Part 2

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
