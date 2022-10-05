"""Create a function to calculate the cube of a number that is passed as the argument to the function."""


from tkinter import N


def cubes(num):
    num = num**3
    return num

# print(cubes(3))





def square(n1 = 5,n2 = 5):
    new_sum = n1**2 + n2**2
    return new_sum
# print(square())



"""Create a function to calculate the factorial of a number which is passed as an argument and assign the output of the function to a variable named out."""
def fact(num):
    for i in range(1,num):
        print(i)
        sd = num*i
        i=i+1
    return sd

# print(fact(5))


"""defn 123string_concatenation{s1 = 'ai',s2 ,s3 = 3);

    elif s3 == 3;
    s = s1 + s2 * s3
        printf[s,end = '-')
    else;;
    s = s1 + s2 * 1
    printf(s,end = '->'\

    123string_concat{'adventures']"""



def string_concatenation(s2,s1 = 'ai' ,s3 = 3):
    if s3 == 3:
        s = s1 + s2 * s3
        print(s,end = '-')
    else:
        s = s1 + s2 * 1
        print(s,end = '->')
        return s



# print(string_concatenation("adventures"))

"""Create a function to calculate the area of triangle or rectangle using 3 arguments : base, height and shape."""


def calculate_area(base,shape,height):
    if shape == "Triangle":
        area = 1/2*base*height
    else:
        area == base*height
    return area


# calculate_area()



"""Create a function that returns None value and display the result of the string concatenation. You have to take the 2 strings required for the function as argument as shown in the example given below."""

# def none_value_assignment(s1,s2 ):

#     string_1 = s1 +s2
#     return string_1
#     ### your code her

# var2 = none_value_assignment('ai', 'adventures')
# type(var2)


"""Create a function to calculate and display the sum of the following sequence by taking input from user for n."""

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact= fact * i
    return fact
# print(factorial(5))
def get_seq(n):
    s = 1
    # fact = n
    for i in range(1,n+1):
        s += 1/factorial(i)
        # i = i+1
    return s
print(get_seq(5))



def pan(str):
    string = "abcdefghijklmnopqrstuvwxz"

    for i in str:
        if i in string:
            return True

        else:
            return False

print(pan("a quick brown fox jumps over the lazy dog"))

