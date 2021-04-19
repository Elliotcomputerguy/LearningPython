#!/usr/bin/python

# The range() function
# The range function takes one integer argument and returns a value of the range data type. These range values can be used in for loops to
# loop a specific number of times. 

for i in range(5):
    print('Elliot')

for i in range(6):
    print(i)

# You can also pass two integer arguments to the range() function. The first argument is where it should start from with the second
# argun=ment being where it should finish. 
print('---------------------------')
for i in range(3, 8):
    print(i)

# Another example below where we are passing an argument into the len() function and using the return value as an argument into the range() function.

print('-----------------------------')
LETTERS = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
print(len(LETTERS))
print('-----------------------------')
for key in range (len(LETTERS)):
    print(key)
