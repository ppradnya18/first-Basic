

import random

def allowzero():
    allow_zero = input("Do you want to add zero's in Game?")
    print(allow_zero)
    if allow_zero == "Yes" or allow_zero == "No":
        print("Zero's" ,allow_zero)
        return allow_zero
    else:
        print("Please enter Yes or No")
        allow_zero = allowzero()
        return allow_zero


def duplicate(user_inp):
    check_dup = False
    """To check the dupplicate lines in user input"""
    if len(str(user_inp)) == len(set(str(user_inp))):
        check_dup = False
        return check_dup
    else:
        print("Duplicate fouund")
        
        check_dup = True
        return check_dup


check_zeros = allowzero()
if check_zeros == "Yes":
    games_input = random.randint(100,999)
    print("game input for testing ",games_input)
    

def fermi(user_inp,games_input):
    count = 0
    for i in range(0,len(str(games_input))):
        if str(games_input)[i] == str(user_inp)[i]:
            count+=1
    if count == 3:
        print("Fermi 3")
        return "Fermi Fermi Fermi!!!"
    elif count>0:
        print("Fermi ",count)
        print(count)
        return "Fermi"
    

def pico(user_inp,games_input):
    for i in str(user_inp):
        if i in str(games_input):
            digit_input = True
            final_out = "PICO"
            digit_input = True
            return final_out

    
def bagels(user_inp,games_input):
    digit_input = False
    if str(user_inp) not in str(games_input):
        digit_input = True
        final_out = "bagels"
        digit_input = False
        return final_out

"""Source Code"""

def get_inp():
    inp = input("Get the input from user")
    check_duplicate = duplicate(inp)
    if check_duplicate == True:
        print("Duplicate Found, Please enter new Input")
        get_new_input = get_inp()
    if len(inp)>3:
        inp = get_inp()
    else:
        return inp
    return inp


lis=[]
user_inp=901
games_input=910
for i in range(0,len(str(user_inp))):
    if str(user_inp)[i] == str(games_input)[i]:
        lis.append("Fermi")
    
    elif str(user_inp)[i] in str(games_input):
        lis.append("PICO")

    if len(lis) == 0:
        print("Bagels")
print(" ".join(lis))

