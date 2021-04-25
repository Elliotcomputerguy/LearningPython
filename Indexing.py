#!/usr/bin/env python
# #Indexing is the adding of a square bracket to the end of a string value or a variable containing a string with a number 
# between them. This number is called the index, and tells python which postion in the string has the character you want. 
# The index of the first character in a string is 0. The index 1 is the second character, etc. 

# ===============================================================
# Example:

var = 'Elliot'
print(var[0],var[1],var[2],var[3],var[4],var[5])
var = 'Elliot'[0]
print(var)

# ===============================================================

# #Negative Indexes
# Negative indexes start at the end of a string and go backwards. The negative index -1 is the index of the last character in a string. 
# The index -2 is the index of the second from last character, and so on. 

#     0    1    2    3    4
#   [ i ][ n ][ d ][ e ][ x ]
#    -5   -4   -3   -2   -1

# ===============================================================
# Example:

var = 'Elliot'
print(var[-1],var[-2],var[-3],var[-4],var[-5],var[-6])

# ===============================================================

# ===============================================================
# Example:

print('------------------------------------')
import random
word = 'index'
print('The word is: %s \n' % (word))

# remember that len starts from 1! 
high = len(word)
low = -len(word)
print(high)
print(low)
for i in range(10):

    position = random.randrange(low, high) # Remeber that randrange will evaluate a value from 0. Variable high contains
    # a value of 5. But it will never go to 5 as it starts from 0 which is 0-4. You can use randint() and add a -1 
    # on the assignment statement. This way the variable high will be changed to 4 and you wont be out of range 
    print('word [ %s ] \t %s' % (position, word[position]))