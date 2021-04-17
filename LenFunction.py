#!/usr/bin/python

#The Len() function accepts a string value argument and returns an integer value of how many characters are in the string. 

var = len('Hello')
print('length of characters stored in var =', var)

var = 'Elliot'
var = len(var)
print('The lenght of new var =', var)

var = len('Hello' + ' ' + 'world')
print(var)

print('----------------------------------------------')
message = 'some text'
# Indexing s = 0, o = 1, m = 2, e = 3, ''= 4, t = 5, e = 6, x = 7, t = 8
# We can see that we have a total of 8 characters in this string starting from 0. Len() will start from 1 so stores it as 9 characters in variable i. 
# Unless we using slicing [:9] or [0:9] as it does not produce errors we will run into the out of range error. 
i = len(message)
print('The length of message =', i)
# The next line will prodcue an error message out of range as it is out of range. commented out 
# print('The last character in variable message =', message[i])
print('Message printed using blank slice indexing 0-9=', message[:9])
print('-------------------------------------------------')

i = len(message) - 1
print('The lengh of the message -1 =', i)
print('The last character in variable message =', message[i])
print('Message printed using indexing', message[8])
