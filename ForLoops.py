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

# Grow a list using a for loop statement and range() function
myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

# Counting with a for loop using range() function

# when you give the range function 3 arguments. It will treat them as a start point, an end point and the nuber by which to count.
# The start point is always the first value, the end point is never included. 
print('\n\nCounting in fives:')
for i in range(0, 50, 5):
    print(i, end=' ')

# the last argument in the range() function call is -1. This tells the function to go from start point to end point by -1 each time.
# This is the same as saying subtract 1 on each itteration. The loop counts down from 10 to1 and does not include 0. 

print('\n\nCounting backwards:')
for i in range(20, 0, -1):
    print(i, end=' ')