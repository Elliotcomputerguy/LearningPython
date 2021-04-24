#!/usr/bin/env python

# #Strings
# A string is a series of characters. Anything inside quotes are considered a string. All programs define and gather differnt types of data. 
# There are many different data types. Strings are one of them.

# When you create a string you can use '' or "" but not at the same time! You cannot start with " and end with '. 
# You can put '' inside of "" or put '' inside of "". You can also do the below but is not advisable. The aim is to make
# your code as conventional and clear as possible for other readers. So choose your posion and use either '' or "". I prefer ''.
# ===============================================================
# Example:

print('this is a string' + ' ' + "this is a string")

# ===============================================================
# String concatenation can be achieved with the + operator. You can add together two string values
# by using the + operator. If you want a space there must be a space in one of the strings. You dont just have to use the + operator
# you can also use , But again keeping your code clear and easy to read is key.
# ===============================================================
# Example:

print('this is a string', "this is a string")

# ===============================================================
# You can achieve string replication with the * operator.
# The * operator can work with a string and integer data type value. It cannot work with two string values. 'Hello' * 'World'
# ===============================================================
# Example:

print('Hello World' * 10)

var = 'Hello world ' * 10
print(var)

var *= 10
print(var)

# ===============================================================
# Escape characters are used to enable us to print out characters that are difficult to type into
# the source code. 

#   \'	    Single Quote	
#   \\	    Backslash	
#   \n	    New Line	
#   \r	    Carriage Return	
#   \t	    Tab	
#   \b	    Backspace	
#   \f	    Form Feed	
#   \ooo	Octal value	
#   \xhh	Hex value

# ===============================================================
# Example:

print('\nthis is a new line,\tthis is a tab\nanother line')

# ===============================================================
# You can also add variables into your strings. This is known as string formatting or string interpolation. 
# String interpolation is a process of injecting a value into a placeholder 
# (a placeholder is nothing but a variable to which you can assign data/value later) in a string literal.
# ===============================================================
# Example:

variableOne = 'variableElement'

print('One way of displaying a varaible [ %s ] in a string:' % (variableOne)) # <-- Uses the modulo operator %

print (f'This is another way: [ {variableOne} ]') # <--  f-string formatting

print('Another way by unsing the format method: {}.'.format(variableOne)) # <-- .format( ) method

print(' Last but not least another way but using concatenation: ' + variableOne) # <-- This is not using formatting but concatenation 

# ===============================================================
# Converting an integer into a string using str()
# You can convet an integer value into a string value by using str(). 
# ===============================================================
# Example:

variableNumber = 1
print(str(variableNumber))

# ===============================================================
# String Imutability. Sequences fall into one or two categories. mutable or immutable. A sequence that is mutable is one that can change. 
# A sequence that is immutable means unchangable so it is one that cannot change.
# strings are "immutable" which means they cannot be changed after they are created. You can how ever either assign the string to another 
# variable modifying the sting or use slicing.
# ===============================================================
# Example:

message = input('Enter your message:')
new_message = ''
CHARACTERSTOREMOVE = 'aeiou'

for character in message:
    if character.lower() not in CHARACTERSTOREMOVE:
        new_message += character
        print('A new string has been created: %s' % (new_message))
print('Your message with the characters removed: \n %s' % (new_message))

# ===============================================================
# slicing to change the characters. Below example will change the character t with an X.
# ===============================================================
# Example:

var = 'elliotcomputerguy'
var = var[:5] + 'X' + var[6:]
print(var)

# ===============================================================
# Final string to print gives you the ability to specify your own final string to be printed. 
# ===============================================================
# Example:

for i in range(0, 50, 5):
    print(i, end=' ') # <-- The end='' print argument evaluates characters going across your screen rather than down it.                 

import random
for i in range(5):
    print(random.randint(1, 100,),end=' ')

print('The show must', end=' ') 
print('go on...')
# ===============================================================
# Using triple quoted strings. Below i use ASCII from a online generator. You would use a tripple quote string for long text or a 
# a game title like i have done. 
# ===============================================================
# Example:

print('''

 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

 ''')

# ===============================================================
