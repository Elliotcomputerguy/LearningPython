#!/bin/usr/env python

# The def statement means we are creating or defining a new function. We can call the function later in your program

# ===============================================================
# Example:

def myFunction():
    print('This is my function')
    total = 42 + 1
    print('42 plus 1 is %s' % (total))
print('start!')
myFunction()

# ===============================================================

# #Parameters
# Parameters are variables that contain the arguments passed when a function is called. Parameters are automatically deleted when the function 
# returns. A parameter is a variable name in between the parentheses in the def statement. An argument is a value that is passed in between the parentheses
# for a function call.

# ===============================================================
# Example:

def func(param):
    param = ''
var = 'name'
func(var)
print(var)

# ===============================================================

# the variable var is being passed into the function. The variable var does not change to ''. The value of var is being assigned to the
# param variable inside the function. Any changes made to the param variable inside the function will not change the var variable.
# The argument value that is passed in a function call is copied to the parameter.  
# How ever there is an exception to this rule when passing lists or dictionary values. 

# #Return values and return statements

# A return statement is the return keyword followed by the value to be returned. We can also use an expression instead of a value. 

# ===============================================================
# Example:

def addNumbers(a, b):
    return a + b
var = addNumbers(5, 10)
print(var)
# ===============================================================

# The function call addNumbers(5, 10) will evaluate to 15. The return statement in addNumbers() will evaluate the expression a + b and 
# then return the evaluated value. That is why addNumbers(5, 10) evaluates to 15. Which is the value stored in var.

# ===============================================================
# Example:

def answer(yes_or_no):
    while True:
        answer = input('yes or no:').strip().lower()
        if answer in ('yes', 'no'):
            return answer

print(answer('Yes or No'))

     