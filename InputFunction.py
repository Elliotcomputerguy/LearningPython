#!/usr/bin/env python

# When the input() function is called it will wait for for user input to type some text and press Enter. 
# The text string that the user types in becomes the string value or integer value that is stored. 
# ===============================================================
# Example:

var = input('enter a string:')
print(var)

# ===============================================================
# Like expressions, function calls evaluate to a single value. The value that the function call evaluates to is called the return value.
# In the above expample, the return value of the input() functon is the string or integer value that is assigned to the variable var.
# The function input() does not need any arguments unlike the print() function which is why there is nothing between the parentheses 
# ===============================================================
# Example:

myName = input('Enter a string')
print('Hello, ' + myName)
print('Hello', myName)

# ===============================================================
# The input() function can only accept strings in order to convert to integers we can convert the variable into a integer variable 
# ===============================================================
# Example:

myNum = input('Enter a number')
myNum = int(myNum)
print(myNum)

# ===============================================================
# To only accept integer you can use the int() function
# ===============================================================
# Example:

var = int(input('Enter a number:'))
print(var)

# ===============================================================