

"""Selection sort 

Time complexity n*n
space complexity n
worst in every sitution as time complexity is n*n

"""

class selection_sort:
    def __init__(self,lis):
        self.lis=lis

    def selction_sort(self):
        print("entered into first method")
        for i in range(len(self.lis)):
            print("entered into first loop",i)

            min_ind=i
            for j in range(i+1,len(self.lis)):
                print("entered into second loop",j)
                if self.lis[j]< self.lis[min_ind]:
                    print("changing the min_ind",min_ind)
                    min_ind=j
                    print("changed mid_ind",min_ind)
                

            self.lis[i],self.lis[min_ind]=self.lis[min_ind],self.lis[i]
            print("swapping the")
            print(self.lis)

    # def bubble_sort(self):
    #     for i in range(len(self.lis)):
    #         for j in range(0,len(self.lis)-i-1):
    #             if self.lis[j]>self.lis[j+1]:
    #                 self.lis[j],self.lis[j+1]=self.lis[j+1],self.lis[j]

    #     print(self.lis)

        
    

p1 = selection_sort([50,40,30,20,10])
p1.selction_sort()
# p1.bubble_sort()







