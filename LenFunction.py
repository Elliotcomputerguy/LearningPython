#!/usr/bin/env python

# The Len() function accepts a string value argument and returns an integer value of how many characters are in the string. 
# Unlike the range() function or indexing; Len() starts from 1 not 0. 
# ===============================================================
# Example:

var = len('Hello World')
print('length of characters stored in var =', var)

# ===============================================================
# You can use the above to get the last character in a string. 
# You can get the length of a List or a tuple. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(len(sneakers))

sneakers = ('Jordan', 'Nike', 'Yeezy', 'Adidas')
print(len(sneakers))

# ===============================================================
# passing the return value from a len() function into a range() function
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

for i in range(len(sneakers)):
    print(i) #<----------------- will output the integer of how many items are in the list. 

for i in range(len(sneakers)):
    print(sneakers[i]) #<----------------- will output the items in the list. 

# ===============================================================    