"""Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."""

p1=int(input("enter the value of x1"))
p2=int(input("enter the value of x2"))
p1=int(input("enter the value of y1"))
p2=int(input("enter the value of y2"))


import math

distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)