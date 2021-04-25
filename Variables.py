#!/usr/bin/env python

# variables are like containers in which they contain a value. You use the assignment operator = 
# to assign the value. This instruction is what is called an assignment statement.  
# Every variable is connected to a value, which is the information associated with that variable. 
# Variables can contain only letters, numbers and underscores. They can start with a letter or an underscore, but not a number. 
# Spaces are not allowed in variable names, but underscores can be used to seperate words. Best practice is to use camelcase.
# Avoid using python keywords and function names as variable names. 
# As best practice variable names should be short but descriptive. Variable names are case sensitive.
# You should always use lower case in your variable names unless you are declaring a constant which is a variable that is static.

#    ===============================================
#    |   var                =             11 + 6   |
#    | Variable   Assigment operator    Expression |
#    ===============================================
#                           ||
#                  Assigment statement

# Key thing to remember is if a python instruction evaluates to a single value, it is an expression. Otherwise it is a statement.
# variables store single values not expressions. The evaluated value from the expression is stored in the variable.
# ===============================================================
# Example:

var = 'Hello World'
print(var)

# ===============================================================
# Constant variables are just the same as normal variables but the vaue is static and does not chnage. 
# standard convention is to use all uppercase in the variable name.
# ===============================================================
# Example:

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# ===============================================================
# You can use multiple assigment using a single line. This can be used When initalizing a set of numbers.
# But can also be used with string objects as well.
# ===============================================================
# Example:

x, y, z = 0, 0, 0
print(x, y, z)

x, y, z = 'hello', 'world', 'again'
print(x, y, z)

