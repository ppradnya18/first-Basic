# bub=[4,3,2,3,4,5,4,5,44,5,4,4,443,33]

# def merging(arr):
#     len_arr=len(arr)//2
#     l=arr[:len_arr]
#     r=arr[len_arr:]

#     merging(l)
#     merging(r)

#     return 
# merging(bub)


s=[6,454,6,3,4,5,4,3,22]

s.append(4444)
# print(s)


##Reverse a string

st="newlife"
str=""
# for p in st:
    

## find the second largest number in python?


lst=[6,4,4,5,67,7,8,53,6,55]

for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
        print(lst)
    if lst[i]==lst[i+1]:
            pass
    else:
        print("second largest element",lst[i])
        break



# print("smallest num",lst)













