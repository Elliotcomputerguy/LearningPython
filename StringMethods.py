#!/usr/bin/env python

# Methods are just like functions, except they are attached to a non-module value with a period.

# A function is not a method just because it is in a module. It can some times get confusing. Example; pyperclip.copy() is not a method but
# indeed a module. It is a function that is inside the pyperclip module. Most data types like strings have methods. 

# Upper() and lower() 
# will evaluate to an upper or lower case version of that string.
# ===============================================================
# Example:

print('elliotcomputerguy'.upper())
print('elliotcomputerguy'.lower())

# ===============================================================
# The title method() changes each word to title case, where each word will begin with a capital letter
# ===============================================================
# Example:

print('elliotcomputerguy'.title())

# ===============================================================
# capatalize() method. Pretty much explains itself. It will only capatilize the first word in the string.
# ===============================================================
# Example:

print('elliotcomputerguy'.capitalize())

# ===============================================================
# The find() method takes one string argument and returns the integer index of where that string appears in the method's string. 
# If the string argument cannot be found, the find() method returns a -1. You can pass more than one character. 
# The integer that find() returns will be the index of the first character where the argument is found.
# ===============================================================
# Example:

var = 'Hello'.find('l')
print(var) #<--- This will evaluate to the index of [2] as it is the position in the string where it starts. Here the method is
var = 'Hello' # assigned to the string.
find = var.find('He') #<--- This will evaluate to the index of [0] as it is the position in the string where it starts. 
print(find)           # Here the method is assigned to the variable.  

# ===============================================================
# format() method is String interpolation which is a process of injecting a value into a placeholder 
# (a placeholder is nothing but a variable to which you can assign data/value later) in a string literal.
# ===============================================================
# Example:

var = 'variable'
print('format method: {}.'.format(var))

# ===============================================================
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator. syntax = string.join(iterable)
# ===============================================================
# Example

myList = []
for i in range(10):
    myList += [str(i)] #<--- I convert the integer value you into string using the str() function. This allows us to use the join() method
print(''.join(myList))  # without having the , also be present. 

myList = ['bird', 'dog', 'cat', 'mouse']
print('-'.join(myList))

print('@'.join('a sentence is a set of words that is complete in itself'))

# ===============================================================
# The .replace() method will replace characters/words from strings. The first example will replace all empty spaces inbetween the
# words with no spaces in conjunction with .join() method.
# The second example replaces the word 'Hello' with 'Hey' from the string 'Hello World' assigned to variable var.
# ===============================================================
# Example

print(''.join('a sentence is a set of words that is complete in itself').replace(' ', ''))

var = 'Hello World '
print(var.replace('Hello', 'Hey'))
print(var)

# ===============================================================
# Python string method strip() returns a copy of the string in which all chars have been stripped from the beginning and 
# the end of the string (default whitespace characters). To remove just left while space use .lstrip() and for right use .rstrip()

# ===============================================================
# Example

print(' Enter a string with whitespace ').strip()
print(' Enter a string with whitespace ').lstrip()
print(' Enter a string with whitespace ').rstrip()

# ===============================================================
