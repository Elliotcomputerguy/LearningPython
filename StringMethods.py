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
