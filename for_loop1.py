# i = 1
"""While loop for getting the factors"""
# while i <= 100:
#     if 100 % i ==0:
#         print(i)
#     i=i+1


"""For loop for getting the factors"""
# for i in range(1, 100+1):
#     if 100 % i == 0:
#         print(i,end=" ")


"""for loop for prime numbers """

# for num in range(1,30):
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "No prime")
#             break
#     else:
#         print(num,"---prime number")



"""while loop with prime nums"""
# i=1
# while i<30:
#     for p in range(2,i):
#         if i % p == 0:
#             print(i,"-Prime Numbers")
#             break
#     else:
#         print(i,"i===Prime")
#     i = i+1




"""For loop for summation"""

# ds=0
# for i in range(0,25):
#     sd = (1/24)*((3/4)**i)
#     ds=ds+sd
# print(ds)


"""While loop for summation"""

# i=0
# bs=0
# while i <= 25:
#     sb = (1/24)*((3/4)**i)
#     bs=bs+sd
#     i=i+1
# print(ds)

"""for loop product """
# ds=1
# for i in range(1,25):
#     sd = (1/24)*((3/4)**i)
#     ds=ds*sd
# print(ds)



"""While loop for summation"""

# i=1
# bs=1
# while i <= 25:
#     sb = (1/24)*((3/4)**i)
#     bs=bs*sd
#     i=i+1
# print(ds)

# for num in range(1,30):
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "No prime")
#             break
#     else:
#         print(num,"---prime number")


# ls=[]
# for num in range(1, 100):
#     if 100 % num == 0:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print(num)
#                 break
#         else:
#             if num == 1:
#                 print(num,"PRIME")
#                 continue
#             ls.append(num)
# print(ls)





# def num1():
#     def num2():

#         return 2+3
#     return num2()
# print(num1())

def add(a,b):
    return a+b

z= add


del z
print(z(3,4))