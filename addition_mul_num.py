def mul_int(n):
    p=0
    s=0
    ls=[]
    for i in range(1,n+1):
        d=n**i
        s=s+d
        ls.append(n)
        p=p+1
    print(ls)
    print("final score",s)


mul_int(3)








