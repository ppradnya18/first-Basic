cd = 65744
print(len(str(cd)))
print(set(str(cd)))
print(len(set(str(cd))))

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
            
    
def pico(user_inp,games_input):
    for i in str(user_inp):
        if i in str(games_input):
            digit_input = True
            final_out = "PICO"
            digit_input = True
            print("Oico")
            return final_out


# fermi(234,214)
pico(705,697)