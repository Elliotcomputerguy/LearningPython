#!/usr/bin/env python

# Python exception objects are designed to manage errors that present themselves during the execution of a program. 
# To ensure that your program does not crash you can create custom exception objects to handle errors and prevent tracebacks.
# The try except blocks are used to handle exceptions. Your program will continue to run using the try except exception handlers.
# Python has built-in exceptions that capture multiple differnt errors and returns what are called tracebacks. 
# Going through them you have TypeErrors. TypeErrors will trigger when a task is being carried out on the wrong datatype.
# ValueErrors are produced when attempting to convert a datatype into a datatype that is not convertable to the requested datatype.
# OverFlowErrors occur when a result is to large. This happens with float datatypes as integers have unlimited precision.
# NameError tracebacks are raised when a variable has not been defined. ZeroDivisionError tracebacks are thrown when the divisor is a
# zero in a division expression. 
# ===============================================================
# Example

def addFunc(a, b):
    try:
        print(a + b)
    except (TypeError):
        print('Error occured!')

addFunc(1559, 'string')

# ===============================================================
# In the event a different exception event could occur. You can handle multiple exception types by expressing them in
# parentheses seperated by a comma.
# ===============================================================
# Example

def dev(a, b):
    try:
        print(a / b)
    except (TypeError, ZeroDivisionError):
        print('You either did not enter a number or you attempted to devide by zero')

dev(10, 0)

# ===============================================================
# You can use multiple except blocks to help identify the error more clearly rather than combine errors in one exception block.
# ===============================================================
# Example

def dev(a, b):
    try:
        print(a / b)
    except (TypeError):
        print('Arguments must both be numbers.')
    except (ZeroDivisionError):
        print('You cannot set the devisor as 0.')

dev('10', 5)

# ===============================================================
# An else clause can be used if the try clause does not raise an exception. Else block will execute only when no exception occurs.
# ===============================================================
# Example

def dev(a, b):
    try:
        evaluated = a / b
    except (TypeError):
        print('Arguments must both be numbers.')
    except (ZeroDivisionError):
        print('You cannot set the devisor as 0.')
    else:
        print(f'{a} / {b} = {evaluated}')

dev(10, 5)

# ===============================================================
# The finally keyword is provided to execute after try and except blocks. The finally block always 
# executes after the processing of the try block or after try block terminates due to an exception.
# ===============================================================
# Example

def dev(a, b):
    try:
        evaluated = a / b
    except (TypeError):
        print('Arguments must both be numbers.')
    except (ZeroDivisionError):
        print('You cannot set the devisor as 0.')
    else:
        print(f'{a} / {b} = {evaluated}')
    finally:
        print('this code would execute regardless of an exceptevent is triggered.')

dev('10', 5)

# ===============================================================
