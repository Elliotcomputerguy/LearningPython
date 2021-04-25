#!/usr/bin/env python

# The Len() function accepts a string value argument and returns an integer value of how many characters are in the string. 
# It will start from 1 not 0. 

# ===============================================================
# Example:

var = len('Hello')
print('length of characters stored in var =', var)

# ===============================================================

# ===============================================================
# Example:

print('----------------------------------------------')
message = 'some text'

# Indexing s = 0, o = 1, m = 2, e = 3, ''= 4, t = 5, e = 6, x = 7, t = 8

# We can see that we have a total of 8 characters in this string starting from 0. Len() will start from 1 so stores it as 9 characters in variable i. 
# Unless we using slicing [:9] or [0:9] as it does not produce errors we will run into the out of range error as from an Index perspective 
# only 8 charachters exist. Not 9. 
i = len(message)
print('The length of message =', i)
# The next line will prodcue an error message out of range as it is out of range. commented out 
# print('The last character in variable message =', message[i])
print('Message printed using blank slice indexing 0-9=', message[:9]) #<-- Slicing does not return an error. 
print('-------------------------------------------------')

i = len(message) - 1 #<-- subtract 1 from len(message) which will evaluate to the value of 8
print('The lengh of the message -1 =', i) 
print('The last character in variable message =', message[i])
