from distutils.command.build_scripts import build_scripts
import math
c_side = 5
degree1=30



a_side = c_side * math.sin(degree1)
# b_side_sqr= ((a_side)**2) + ((c_side)**2)
# b_side = b_side_sqr**0.5

third_angle = 90 - degree1

b_side_diff= c_side * math.cos(third_angle)
print(b_side_diff)
print(third_angle)
