#!/usr/bin/env python

# Python exception objects are designed to manage errors that present themselves during the execution of a program. 
# To ensure that your program does not crash you can create exception objects to handle errors and prevent tracebacks.
# The try except blocks are used to handle exceptions. Your program will continue to run using the try except exception handlers. 
# If you do not know what the python exception object will be you can just use the except keyword.
# ===============================================================
# Example

myString = 'string'
myNumber = 1
try:
    print(myString + myNumber)
except: 
    print('Error, you cannot concatenate a str() to an int() data type. You must convert to str()') 

# ===============================================================
# By using exception blocks you prevent your program from crashing and further prevent any threat actors from learning anything 
# about your code. Usong the else block will allow you to continue with your code. If the try block does not error the else block will
# continue to execute your code.
# ===============================================================
# Example

intInput = None
while not intInput:
    try:
        intInput = int(input('Enter a number:'))
    except:
        print('That was not a integer value?')
    else:
        print(f'{intInput} x 5 =', intInput * 5 )

# ===============================================================
