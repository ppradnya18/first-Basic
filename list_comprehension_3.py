#Create a function that takes numbers as input, displays the sum of those numbers, stores the numbers inside a dictionary with number being the key and values being the square root of those numbers in reverse order in float datatype using map function and dictionary comprehension.

# num = (input("Enter the list of numbers ").split())
# print(num)
# sd = list(num)
# numd =0
# for i in range(len(sd)):
#     print(sd[i])
#     numd = numd+int(sd[i])
# print(numd)

"""By List comprehension ----"""
# nu = [int(sd[i])+numd for i in range(len(sd))]
# print("99",nu) #Not working

# new_ = {float(i):int(i)**(1/2) for i in sd[::-1]}
# print(new_)





"""2. Create a function that uses dictionary comprehension to create a dictionary 
that stores the character of the string as the keys and its value will be a group of (1,True)
 if it is a vowel or (0,False) if it is not."""


# new_char = input("Enter the input Name")
# new_dict = {}
# for i in new_char:
#     if i in "aeiou":
#         new_out = (1,True)
#     else:
#         new_out = (0,False)

#     new_dict[i]=(new_out)

# print(new_dict)


# nes = {new_dict[i]=(new_out) new_out (1,True) if i in "aeiou" else new_out (0,False) for i in new_char }
# net ={i: (1,True) if i in "aeiou" else (0,False) for i in new_char }

# print(net)



#Create a function that mimics a lottery system that is based on the vowels and consonants from the user's name. Vowels are worth 5 points each and consonants are worth 1 point each. Points calculation also includes the index numbers of the vowels and consonants. If the vowel points equates to consonant points, it is a lottery!

#Note : Enter your name in lowercase. Try solving this using enumerate and range function

vow = 0
cons = 0

# strr = input("creat the name ")
# for i in lenstrr:
#     if i in "aeiou":
#         vow +=1
#     else:
#         cons+=1

# print(cons,vow)




# inp = list(input("enter the name of people in room"))
# from itertools import combinations
# c = combinations(inp, 2)
# print(*c)



dict_new={}
inp = int(input("enter the number"))

# for i in range(1,(inp**2)+1):
#     if i%2 ==0:
#         val = "Black"
#     else:
#         val = "White"
#     dict_new[i]=val
#     print(i)
# print(dict_new)



ls = 8
ld = 8
lssst =[]
c_p=[]
for p in range(1,9):
    c_p1=[]
    c_p2=[]
    for j in range(1,9):
        lssst.append([p,j])
        if p%2!=0:
            if j%2!=0:
                c_p1.append("Black")
            elif j==8:
                c_p1.append("White")
                c_p.append(c_p1)
                c_p1=[]
            else:
                c_p1.append("White")
        elif p%2==0:
            if j%2==0:
                
                c_p2.append("White")
            elif j==8:
                c_p2.append("White")
                c_p.append(c_p2)
                c_p2=[]
            else:
                c_p.append("Black")
print(len(c_p))











