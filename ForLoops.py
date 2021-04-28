#!/usr/bin/env python

# For loop statement 
# The for loop statement is very good at looping over a string or list of values. This is different to the while statement. which loops
# as long as a certain condition is True. A for statement has 6 parts.  


# 1. The keyword for
#   | 
#   |    |----------2. The variable name 
#   |    |    |----------------------3. The keyword in
# for value in values: -----------------------------5. Colon
#   some_code_here -|---------------------6. A block of code
#                   |
#                  4. A string or variable containing a string


# The for loop is very similar to the while loop, but when you only need to iterate over characters in a string. 
# using the for loop is much less code to type. You can make a while loop act as a for loop but with much more code.  
# ===============================================================
# Example:

for letter in 'ElliotComputerGuy':
    print('The letter is :', letter)

# ===============================================================
# Multiply numbers.

# ===============================================================
# Example:

num = input('Enter a number to multiply:')
num = int(num)
# If you use int() function on the input() function. You will need to convert integer to string with str() before passing to print() function.
# Your notice a 11 instead of a 10. This is due to the range() function. It will not go up to the last range value. 
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# ===============================================================
# Grow a list using a for loop statement and range() function. It will only reach to 9 due to the range() function.
# ===============================================================
# Example:

myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

# ===============================================================
# Counting with a for loop using range() function
# when you give the range function 3 arguments. It will treat them as a start point, an end point and the nuber by which to count.
# The start point is always the first value, the end point is never included. The below example will only reach 45.  
# ===============================================================
# Example:

print('\n\nCounting in fives:')
for i in range(0, 50, 5):
    print(i, end=' ')

# ===============================================================
# the last argument in the range() function call is -1. This tells the function to go from start point to end point by -1 each time.
# This is the same as saying subtract 1 on each itteration. The loop counts down from 10 to 1 and does not include 0. 
# ===============================================================
# Example:

print('\n\nCounting backwards:')
for i in range(20, 0, -1):
    print(i, end=' ')

# ===============================================================
# Enumerate() function technique can be used to obtain the integer value of the index and items in the list.
# This is a replacement for using the range(len(yourList)). When passing index to the string ensure to wrap it in a string datatype.  
# ===============================================================
# Example:

sneakers = ['Jordan 1 High\'s Bred', 'Nike Air Max 90', 'Yeezy v350 bred', 'Adidas pharrell Tennis Hu']
for index, sneaker in enumerate(sneakers):
    print(f'Index {str(index)} in stock is {sneaker}')
