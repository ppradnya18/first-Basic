# user_inp = int(input("Enter the net worth of Mark "))

# if user_inp == 54500000000 :
#     print("That's 54.5 billion!")
# elif user_inp < 54500000000	:
#     print("That's not much!")
# elif user_inp > 54500000000	:
#     print("I'll make more when I graduate")






# user_inp = int(input("Enter the cost prize of the bike "))

# if user_inp > 100000:
#     print("The total prize is " ,((user_inp*100)/15 )+ user_inp)

# elif (user_inp > 50000 and user_inp <= 100000	):
#     print("The total prize is " ,((user_inp*100)/10 )+ user_inp)


# elif (user_inp <= 50000):
#     print("The total prize is " ,((user_inp*100)/5 )+ user_inp)




# clsses_held=  int(input("Enter the classes held "))

# clsses_attended =  int(input("Enter the classes held "))


# attend_per = (clsses_attended /clsses_held) % 100

# if attend_per > 75:
#     print("can sit for exam")
# else:
#     print("cant sit for exam")


# gender= (input("Enter the gender of the worker"))
# age_worker =  int(input("Enter the age of the worker "))

# if age_worker >= 18 and age_worker < 30	:
#     if gender== "M":
#         print("The daily wages are 700")
#     else:
#         print("The daily wages are 750")

# elif age_worker >= 30 and age_worker <= 40:
#     if gender== "M":
#         print("The daily wages are 800")
#     else:
#         print("The daily wages are 850")

# else:
#     print("You are retired ")

# check_Year =  int(input("Enter the Year "))

# if (check_Year%4) == 0:
#     print("the year is leap year")
#     if (check_Year%100) == 0:
#         if (check_Year%400) == 0:
#             print("The year is leap year")


# else:
#     print("it is not leap year")




# student_days =  int(input("Enter the days"))

# if student_days < 5:
#     print("Total charge: ",student_days*2)
# if student_days >6 and  student_days < 10:
#     total_cost = (student_days-5)*3  + 10
#     print("Total charge: ",total_cost)


# if student_days >11 and  student_days < 15:
#     rem= student_days-10
#     total_cost = (student_days-10)*4  + (rem)*3 + 10
#     print("Total charge: ",total_cost)
    
# if student_days > 15:
#     rem= student_days-15
#     rem2=rem - 5
#     total_cost = ((student_days-15)*5)  + ((rem)*4) + (rem2 *2)
#     print("Total charge: ",total_cost)
# units_user = int(input("enter the units from"))






user_unit = int(input("enter the units"))

if user_unit <100:
    print("FREE !!!")


elif user_unit >11 and  user_unit < 15:
    rem= user_unit-100
    
    rem2=rem-200
    total_cost = rem +(rem-10)*4  + (rem)*3 + 10
    print("Total charge: ",total_cost)
    