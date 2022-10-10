

frog_lis = ["B","B","B","_","G","G","G"]
req_frog = ["G","G","G","_","B","B","B"]
while True:
    user_inp = int(input("enter the location index"))

    if "_" == frog_lis[user_inp]:
        print("Please enter the valid location")
    else:
        if frog_lis[user_inp] == "B":
            if frog_lis[user_inp+1] == "_" :
                frog_lis[user_inp],frog_lis[user_inp+1] = frog_lis[user_inp+1],frog_lis[user_inp]
            elif frog_lis[user_inp+2] == "_":
                frog_lis[user_inp],frog_lis[user_inp+2] = frog_lis[user_inp+2],frog_lis[user_inp]
        else:
            if frog_lis[user_inp-1] == "_" :
                frog_lis[user_inp],frog_lis[user_inp-1] = frog_lis[user_inp-1],frog_lis[user_inp]
            elif frog_lis[user_inp-2] == "_":
                frog_lis[user_inp],frog_lis[user_inp-2] = frog_lis[user_inp-2],frog_lis[user_inp]
    print(frog_lis)
    if frog_lis == req_frog:
        print("You won")
        break
        

