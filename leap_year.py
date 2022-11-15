# def is_leap(year):
#     leap = False
#     if year % 4:
#         leap = True
#     if year % 4 ==0 and year %100==0:
#         leap = False
#     else:
#         if year % 4 ==0 and year % 400 ==0:
#             leap = True
        
def is_leap(year):
    leap = False
    if year % 4 == 0:
        print("inside 1")
        leap = True
        if year % 100 == 0:
            leap = False
            print("inside 2")
            return leap
        if leap % 400 == 0:
            leap = True
            print("inside 3")
        return leap
            

    return leap

year = int(input())
print(is_leap())