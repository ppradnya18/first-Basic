"""29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
"""



color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["White", "Black", "Red"])

print(set(color_list_1))
# d=[x for x in color_list_1]

nd=set(color_list_1).isdisjoint(set(color_list_2))
print(nd)


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]



# print(fruits.union(more_fruits))
fruits.union(more_fruits)
print(fruits)



Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}


print(Dates)
