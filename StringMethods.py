#!/usr/bin/python

# Methods are just like functions, except they are attached to a non-module value with a period.
# Examples of a string method is upper() and lower().
# 
# A function is not a method just because it is in a module. It can some times get confusing. Example; pyperclip.copy() is not a method but
# indeed a module. It is a function that is inside the pyperclip module. Most data types like strings have methods. Upper() and lower() 
# will evaluate to an upper or lower case version of that string.

var = 'Hello world'.upper()
print(var)
var = var.lower()
print(var)
print(var.upper())
print(var)

# #The find() string method
# Just like upper() lower() method can be called on sting values, the find() method is a string method. The find() method takes one
# string argument and returns the integer index of where that string appears in the method's string.

print('----------------------')
var = 'Hello'
find = var.find('H')
print(find)
find = var.find('e')
print(find)

# If the string argument cannot be found, the find() method returns a -1. You can pass more than one character. The integer that find() returns
# will be the index of the first character where the argument is found.

find = var.find('llo')
print(find)

# The .Join() and title() string method's

# The join() method pretty much says it in the title it joins strings/lists etc together. You can place other strings inbetween them.  
# The title menthod also says it in the name and will uppercase the first character of each item value or string. 
myList = ['item1', 'item2', 'item3']
print('-'.join(myList).title())


