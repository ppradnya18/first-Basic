"""14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)"""




from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2015, 7, 2)
delta = l_date - f_date
print(delta.days)