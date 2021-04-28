#!/usr/bin/env python

# The range() function
# The range function takes one integer argument and returns a value of the range data type. These range values can be used in for loops to
# loop a specific number of times. 
# ===============================================================
# Example:

for i in range(5):
    print('Elliot')

# ===============================================================
# Example:

for i in range(6):
    print(i)

# ===============================================================
# You can also pass two integer arguments to the range() function. The first argument is where it should start from with the second
# argunment being where it should finish. The end argument will not be included. Will only return 7 at the end in this return
# ===============================================================
# Example:

for i in range(3, 8):
    print(i)

# ===============================================================
# Another example below where we are passing an argument into the len() function and using the return value as an argument into the range() function.
# As you cannot pass string data types into the range function. 
# ===============================================================
# Example:

LETTERS = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
for key in range (len(LETTERS)):
    print(key)

# ===============================================================
# Grow a list using a for loop statement with the range function.
# ===============================================================
# Example:

myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

# How ever it is easier to use the list() function and call the range() function. 
myList = list(range(10))
print(myList)

# ===============================================================
# when you give the range function 3 arguments. It will treat them as a start point, an end point and the nuber by which to count.
# The start point is always the first value, the end point is never included. 
# ===============================================================
# Example:

print('\n\nCounting in fives:')
for i in range(0, 50, 5):
    print(i, end=' ')

# ===============================================================
# the last argument in the range() function call is -1. This tells the function to go from start point to end point by -1 each time.
# This is the same as saying subtract 1 on each itteration. The loop counts down from 10 to1 and does not include 0. 
# ===============================================================
# Example:

print('\n\nCounting backwards:')
for i in range(20, 0, -1):
    print(i, end=' ')

# ===============================================================

