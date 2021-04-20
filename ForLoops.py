#!/usr/bin/python

# For loop statement 
# The for loop statement is very good at looping over a string or list of values. This is different to the while statement. which loops
# as long as a certain condition is True. A for statement has 6 parts.  


# 1. The keyword for
#   | 
#   |    |----------2. The variable name 
#   |    |    |----------------------3. The keyword in
# for symbol in message: -----------------------------5. Colon
#   some_code_here -|---------------------6. A block of code
#                   |
#                  4. A string or variable containing a string


# The for loop is very similar to the while loop, but when you only need to iterate over characters in a string. 
# using the for loop is much less code to type. You can make a while loop act as a for loop but with much more code.  

for letter in 'Elliot':
    print('The letter is :', letter)

# Multiplication table (from 1 to 10)
num = input('Enter a numner to multiply from 1 to 10:')
# convert string into integer
num = int(num)
# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# Grow a list using a for loop statement
myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

