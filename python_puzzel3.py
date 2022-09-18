""" We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile."""




# def get_nums(n):
#     new_lis=[]
#     mm=0
#     while len(new_lis) < n:
#         mm = n+2
#         mm=mm+2
#         new_lis.append(mm)

#     print(new_lis)
#     return new_lis




def get_nums(n):  
    return [n + 2 * i for i in range(n)]   


print(get_nums(17))

sd=[]
n=7

for i in range(n):
    cd= i * 2
    ss= n+cd
    sd.append(ss)
    print(sd)
    print(i)

    


