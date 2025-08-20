#How import works in python 

import math
from math import sqrt,pi 
result=sqrt(9) * pi 
print(result)
# The code calculates the square root of 9, which is 3, and then multiple


#importing everything

from math import *
result = sqrt(16) * pi
print(result)
# The code calculates the square root of 16, which is 4, and then multiplies it by pi.

#as keyword

import math as m
result= m.sqrt(25)
print(result)
print("The square root of 25 is:", result)
print(m.pi)
# The code calculates the square root of 25, which is 5, and prints it along with the value of pi.


#dir functiion
import math
print(dir(math))
print(math.pi, type(math.pi))
# The dir() function returns a list of all the attributes and methods of the math module.
