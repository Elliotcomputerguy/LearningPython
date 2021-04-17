#!/usr/bin/python
# #The Input Function
# When the input() function is called it will wait for for user input to type some text and press Enter. 
# The text string that the user types in becomes the string value or integer value that is stored. If we create am assignment statement. 

var = input()
print(var)

# Like expressions, function calls evaluate to a single value. The value that the function call evaluates to is called the return value.
# In the above expample, the return value of the input() functon is the string or integer value that is assigned to the varibale var.
# The function input() does not need any arguments unlike the print() function which is why there is nothing between the parentheses 

myName = input()
print('Hello, ' + myName)
print('Hello', myName)

# The input() function can only accept strings in order to convert to integers we can convert the variable into a integer variable 

myNum = input()
myNum = int(myNum)
print(myNum)