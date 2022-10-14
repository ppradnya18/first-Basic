#Create a list to store the numbers between 111 to 200 that are divisible by 7 using comprehension.
# ls = []
# for i in range(111,201):
#     if i % 7 ==0:
#         ls.append(i)
# print(ls)

ls =[i for i in range(111,200) if i%7==0]
print(ls)
#{'0': (0.0, 0), '1': (1.0, 1), '2': (2.0, 4), '3': (3.0, 9), '4': (4.0, 16)}
# d1= {i: tuple(float(i),i**2) for i in range(1,6)}
d1= {i: (float(i),i**2) for i in range(1,6)}
print(d1)

# print(tuple(2))
print(len(str(10)))

#Create a dictionary with key-value pairs that has key as the number and their respective value as True if the length of the number is greater than 1 else False using comprehensions.
new = {i:True if len(str(i))>1  else False for i in range(1,14)}
print(new)


#Create a set that filters the numbers that are divisible by 7 as well as 8 between 0 - 1000 using set comprehension.

new = lambda a,b: {i for i in range(a,b) if i%7==0 and i%8==0}
# print("--",(new))
print(new(1000,10001))


# print(ns)

# 

for i in range(1000,3000):
    count=0
    for p in str(i):
        if int(p)%2==0:
            count+=1

    # if count==4:
    #     print(i)




count =0
ns = [''.join(x) for x in [[p for p in str(i)  if (int(p))%2==0 ] for i in range(1000,3000)] if len(x)==4]
# print(ns)



i=4563



L = [2, 4, 6, 8]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):
    print(lval, rval)


R_new = ['3', '6', '9', '12', '15']


for i in map(int, R_new):
    print(type(i))



name = "abhishek"

vow =0
cons =0
lst=[]
cd = "aeiou"
for i in name:
    if i in cd:
        print(i)
        vow+=1
        lst = name.split()
        
        
        
    else:
        cons+=1


print(cons)
print(name.split())