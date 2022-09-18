"""Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. """




class check_list():
    def __init__(self,input):
        self.input =  input

    def check_length(self):
        if len(self.input) == 8 and self.input.count(self.input[4]) == 3:
            return True
        else:
            return False

input=[4,6,5,6,7,7,3,7]

df=check_list(input)
if df.check_length() == True:
    print("True")

else:
    print("False")
