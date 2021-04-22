#!/usr/bin env python

# #The math.ceil(), math.floor() and round() function
# When you divide number using the / operator, the expression returns a floating point number. This happens even if the number divides 
# evenly. For example, 21 / 7 will evaluate to 3.0, not 3. 
# round() will round to the nearest integer 

mathVar = round(5.5)
print(mathVar)

mathVar = round(5.4)
print(mathVar)

import math

mathVar = math.ceil(5.5)
print(mathVar)

mathVar = math.floor(5.5)
print(mathVar)