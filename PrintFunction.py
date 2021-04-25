#!/usr/bin/env python
import random

# There is another python instruction called a print() function call. It performs a task to print values to the screen.
# There are many different functions that come with Python. To call a function means to execute the code that is inside
# the function parenthesis().
# A value that is passed into the function call are called arguments. Arguments are the same as values but are only called 
# arguments when they are passed to function calls. You can also pass an expression to the print() function call instead of a
# single value. This is because the value that is actually passed to the print() function is the evaluated value of that expression.

# ===============================================================
# Example:

print('Hello, ')

# ===============================================================
# Example:

# Printing Multiple Values
print('same', 'message', 'as before')

# ===============================================================
# Example:

var = 'Elliot'
print('Hello, ' + var)

# ===============================================================
# Example:

print('just',
'a bit',
'bigger')

# ===============================================================
# Example:

# Final string to print

print('Here', end=' ')
print('it is...', end=' ')
print('some more code')

# ===============================================================
# Example:

for i in range(5):
    print(random.randint(1, 100,),end='' + '\n') # See what i did to get the value in a straight line. Rather than down the screen.

# ===============================================================
# Example:

# Triple Quoted strings

print('''

|  | |=== |    |    |===|
|==| |==  |    |    |   |
|  | |=== |=== |=== |===|

''')
