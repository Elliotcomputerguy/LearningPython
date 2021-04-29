#!/usr/bin/env python

# Each character in a string or element in a List/Tuple has a numbered position.   
# This numbered position is called an index. Accessing characters in different datatypes use brackets.  
# The index of the first character in a string starts from 0 unlike the len() function. 
# You can place then on the end of strings or variables.  
# ===============================================================
# Example:

var = 'ElliotComputerGuy'
for i in range(len(var)):
    print(var[i], end='')

var = 'ElliotComputerGuy'[0]
print(var)

# ===============================================================
# Negative indexing starts from where the string or list/tuple ends. The negative index starts with a -1 
# which is the last index of the last character in a string, list or tuple.
# The index -2 is the index of the second from last character, and so on. 
# The below example will reverse a string. 
# ===============================================================
# Example:

#     0    1    2    3    4
#   [ i ][ n ][ d ][ e ][ x ]
#  -5   -4   -3   -2   -1

var = 'ElliotComputerGuy'
reversedWord = ''
for i in range(len(var) +1):
   if i == 0:
       reversedWord = var[-1]
   else:
        reversedWord = var[-i]
        print(reversedWord, end=' ')
print('')

# ===============================================================
# Randomly printing out index from string
# ===============================================================
# Example:

import random
word = 'index'
print('The word is: %s \n' % (word))

# remember that len starts from 1! 
high = len(word)
low = -len(word)
print(high)
print(low)
for i in range(len(word)):

    position = random.randrange(low, high) # Remember that randrange will evaluate a value from 0. Variable high contains
    # a value of 5. But it will never go to 5 as it starts from 0 which is 0-4. You can use randint() and add a -1 
    # on the assignment statement for high. This way the variable high will be changed to 4 and you wont be out of range 
    print('word [ %s ] \t %s' % (position, word[position]))

# ===============================================================
# Enumerate() function technique can be used to obtain the integer value of the index and items in the list.
# This is a replacement for using the range(len(yourList)). When passing index to the string ensure to wrap it in a string datatype.  
# ===============================================================
# Example:

sneakers = ['Jordan 1 High\'s Bred', 'Nike Air Max 90', 'Yeezy v350 bred', 'Adidas pharrell Tennis Hu']
for index, sneaker in enumerate(sneakers):
    print(f'Index {str(index)} in stock is {sneaker}')