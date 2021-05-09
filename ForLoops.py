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

# iterate over a string
for letter in 'ElliotComputerGuy':
    print('The letter is :', letter)

# or

#setup a file to read for the below for loop. 
import pathlib
path = pathlib.Path.home() / 'file.txt'
path.touch()
with path.open(mode='w', encoding='utf-8') as fileObj:
    fileObj.writelines('hello world\nhello world')

# iterate over a file and read the lines. 
with path.open(mode='r', encoding='utf-8') as fileObj:
    for line in fileObj.readlines():
        print(line.rstrip())

# ===============================================================
# Just as in while loops the for loop has the abiity to break out of the iteration cycle using the break statement. 
# Again the break statment is used sparingly. Any for loop created can be created without one. 
# ===============================================================
# Example:

NUMBERS = '1234567890'
for index, number in enumerate(NUMBERS):
    if number in NUMBERS:
        print(number)
        if index == 4:
            break
print('done')

#or

NUMBERS = '1234567890'
for i in range(len(NUMBERS)):
    if NUMBERS[i] in NUMBERS:
        print(i)
        if i >= 5:
            break
print('done')

# ===============================================================
# As with the break statement from a while conditional you can also use the continue statement to skip any 
# code below and go back to the top of the for loop.
# ===============================================================
# Example:

NUMBERS = '1234567890'
for i in range(len(NUMBERS)):
    if NUMBERS[i] in NUMBERS:
        print(i)
        if i == 5:
            continue
        elif i >= 6:
            break
print('done')

# ===============================================================
# As in the if and elif you use the else statement to do something else if the if and elif statements are not True. You can
# also use the else statement in the for loop. 
# ===============================================================
# Example:

STRING = 'HELLO-WORLD'
for i in STRING:
    if i in STRING:
        if i == 'A':
            break
else:
    print(f'A was not in {STRING}')

# ===============================================================
# Using the range() function in a for loop to print out a multiplication.
# ===============================================================
# Example

num = input('Enter a number to multiply:')
num = int(num)
# If you use int() function on the input() function. You will need to convert integer to string with str() before passing to print() function.
# Range() will only iterate 10 times. Regardless of the end point argument being 11. Range() will only iterate up to the last integer. 
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# ===============================================================
# Grow a list using a for loop statement with the range() function. It will only reach to 9 due to the range() function.
# ===============================================================
# Example:

myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

# ===============================================================
# Counting with a for loop using the range() function.
# when you give the range function 3 arguments. It will treat them as a start point, an end point and the number by which to count.
# The start point is always the first value, the end point is never reached. The below example will only reach 45.  
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

# ===============================================================