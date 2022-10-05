"""Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five"""


input=[2,3,4,5,6,65,19,19,5,5,5]

class find_occur:
    def __init__(self,liss):
        self.liss = liss
    
    def check_occur(self):
        print(self.liss)
        print(dir(self.liss))
        print(type(self.liss))
        fifteen_count=self.liss.count(19)
        five_count = self.liss.count(5)
        if fifteen_count == 2 and five_count == 3 :
            return True
        else:
            print("More amount has been refelected from the list..")
            return False



sd=find_occur(input)
if sd.check_occur() == True:
    print("True")

else:
    print("False")
         