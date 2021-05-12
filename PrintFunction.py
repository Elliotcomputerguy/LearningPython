#!/usr/bin/env python

# print() is a built-in function that comes with Python. It performs the task of printing values to the screen.
# There are many different functions that come built-in with Python. 

# Functions provide effects and results. Arguments are input into a function to provde an output. Not all functions
# require an argument to return a result or create an effect. 

# When you invoke the print() function. The string or integer you pass inbetween the parentheses is called an Argument.
# There are many arguments that the print() function can handle. when you pass an expression to the print() function it only 
# stores the evaluated value of that expression. 
# ===============================================================
# Example:

# When you create an integer like the below. The value 5 is called an integer literal because the integer 
# is literally typed between the parentheses.

print(5 * 5)

# The below is a string literal as it is literally typed between the parentheses.

print('5' + '5')

# ===============================================================
# Printing Multiple string literals in the same print function. 
# ===============================================================
# Example:

print('same', 'message', 'as before')

# ===============================================================
# Printing a variable with a string is called concatanation. You use the + operator or you could use a comma. There is 
# also string interpolation but is covered in strings.
# ===============================================================
# Example:

var = 'Elliot'
print('Hello, ' + var)

# ===============================================================
# The print() function has two keyword arguments. The first is called end. The second keyword argument is sep.
# The end kwarg will print all in one line. The sep kwarg will seperate strings with any charcter value you place after the 
# assigmnt statement. Both kwargs may be in the same print function.
# ===============================================================
# Example:

print('Here', end=' ')
print('it is...', end=' ')
print('some more code')

print('My Name', 'is', 'ElliotComputerGuy', sep='-')
print('My Name', 'is', 'ElliotComputerGuy', sep='@', end= '')

# ===============================================================
# Printing triple quoted strings for menu's or titles.
# ===============================================================
# Example:

# Triple Quoted strings

print('''

|  | |=== |    |    |===|
|==| |==  |    |    |   |
|  | |=== |=== |=== |===|

''')
