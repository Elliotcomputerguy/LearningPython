#!/usr/bin/env python

# A string is a series of characters. Anything inside quotes are considered a string. All programs define and gather differnt types of data. 
# There are many different data types. Strings are one of them.

# When you create a string you can use '' or "" but not at the same time. You cannot start with " and end with '. 
# The quotes around your strings are called delimiters. When you type them into your program they are called string literals. 
# You can put '' inside of "" or put '' inside of "". You can also do the below but is not advisable. 
# The aim is to make your code as conventional and clear as possible for other readers. 
# ===============================================================
# Example:

var = "Hello "
var + 'World'
print(var)

# ===============================================================
# String concatenation can be achieved with the + operator. You can add together two string values
# by using the + operator. If you want a space there must be a space in one of the strings. You dont just have to use the + operator
# you can also use , But again keeping your code clear and easy to read is key.
# ===============================================================
# Example:

print('this is a string' + ' ' + 'this is a string')
print('this is a string', 'this is a string')

# ===============================================================
# You can do string replication with the * operator.
# The * operator can work with a string and integer data type value. It cannot work with two string values. 'Hello' * 'World'
# ===============================================================
# Example:

print('Hello World' * 10)

var = 'Hello world ' * 10
print(var)

var *= 10
print(var * 10)

# ===============================================================
# Python provides Escape characters to use when working with strings. 
# ===============================================================

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
# Adding variables into strings is known as string formatting or string interpolation. 
# String interpolation is a process of injecting a value into a placeholder. 
# A placeholder is nothing but a variable to which you can present a value in your string literal.
# ===============================================================
# Example:

variableOne = 'variableElement'

print('One way of displaying a varaible [ %s ] in a string:' % (variableOne)) # <-- Uses the modulo operator %

print (f'This is another way: [ {variableOne} ]') # <--  f-string formatting

print('Another way by using the format method: {}.'.format(variableOne)) # <-- .format( ) method

print(' Last but not least another way using concatenation: ' + variableOne) # <-- concatenation 

# ===============================================================
# You cannot concatenate an integer data type into a string data type without converting the integer into a string data type.
# You can use the int() function to convert to an integer from a string and use the str() function to convert to a string. 
# ===============================================================
# Example:

variableWord = 'Word'
variableNumber = 1

variableWord + variableNumber #<---- Error

print(variableWord + str(variableNumber)) #<--- evaluates to 'word1'

player1Ammo = '8'
player1Ammo = int(player1Ammo) - 3
print(player1Ammo)

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
# You can loop through strings printing out each character. Use the end='' print argument to evaluate across the screen
# rather than down it.
# ===============================================================
# Example:

var = 'A sentence is a set of words that is complete in itself'
for letter in var:
    print(letter, end='')

# ===============================================================
# To get the length of a string you can use the len() function.
# ===============================================================
# Example:

print(len('A sentence is a set of words that is complete in itself'))

# ===============================================================



