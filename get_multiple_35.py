import sys
def get_multiples(n):
    if n%3==0 or n%5==0:
        return True
    else:
        return False
        
sum_1=0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3 = (n-1)//3
    n5 = (n-1)//5
    n15 = (n-1)//15
    sum_of_3 = int((1+n3)*3*n3) #(Sum = n/2*(2a +(n-1)d))
    sum_of_5 = int((1+n5)*5*n5)
    sum_of_15 = int((1+n15)*15*n15)
    print((sum_of_3+sum_of_5-sum_of_15)//2)
    