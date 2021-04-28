#!/usr/bin/env python

# If you want to get more than one character from a string, list or a tuple, you can use slicing of indexing.
# A slice also like indexes or lists uses the [  ] square brackets but has two integer indexes instead of one.
# The two indexes are seperated by a colon : 

#  0   1   2   3   4   5
#  +---+---+---+---+---+
#  | i | n | d | e | x |
#  +---+---+---+---+---+
#  -5 -4  -3  -2  -1

# ===============================================================
# Example:

var = 'ElliotComputerGuy'[0:3]
print(var)
var = 'Hello World'[0:5]
print(var)
var = 'Hello World'[-11:-6]
print(var)
var = 'Hello world'[0]
print(var)
var = 'Hello world'[-0]
print(var)

# ===============================================================
# Notice how 0 and -0 are the same. Remember that -1 is the last character in negative indexes 
# Unlike indexes, slicing will never give you an error if you give it too large of an index for the string.
# ===============================================================
# Example:

var = 'Hello world'[0:999]
print(var)
var = 'Hello world'[2:999]
print(var)
var = 'Hello world'[1000:2000]
print(var)

# ===============================================================
# Blank Slice Indexes is when you leave out the first index of a slice. 
# Python will automatically think you want to specify index 0 for the first index. 
# The expression 'Hello'[0:3] and 'Hello'[:3] evaluate to the same string. 'Hel'
# ===============================================================
# Example:

var = 'Hello world'[:3] # <-- Get only characters before 3 = 'Hel' Everything up to 3.
print(var)

# ===============================================================
# If you leave out the second index, python will automatically think you want to specify the rest of the string. 
# 'Hello'[2:] evaluates to the value 'llo world'
# ===============================================================
# Example:

var ='Hello world'[2:] # <-- Get characters only After 2 = 'llo world'
print(var)

# ===============================================================
# You cannot assign a character in a string value as strings are immutable.
# using slicing you can change the character of a string without assiging the variable another value. 
# ===============================================================
# Example:
#  
#  0    1    2    3    4   5
#  [ h ][ e ][ l ][ l ][ o ]
# -5  -4    -3   -2   -1   

var = 'Hello'
var = var[:0] + 'G' + var[1:]
print(var)

var = 'string'
var = var[:4] + 'x' + var[5:]
print(var)

# ===============================================================
# Slicing pizza game
# ===============================================================
# Example:

word = 'pizza'
print('''

 Slicing cheat sheet

0   1   2   3   4   5
+---+---+---+---+---+
| p | i | z | z | a |
+---+---+---+---+---+
-5 -4  -3  -2  -1

''')
start = None
while start != '':
    start = input('\nstart:')
    if start:
        start = int(start)
        finish = int(input('Finish:'))
        print('word [ %s : %s ]' % (start, finish), end=' ')
        print(word[start:finish])
print('finish')    

# ===============================================================
# remove a character from the string assigned to word using slicing
# ===============================================================
# Example:

word = 'sneakers'
print('Original variable word:', word)
word = word[:4] + '' + word[5:]
print('New word:', word)
word = word[:4] + word[(4 + 1):] 

# ===============================================================
# using slices to slice a list 
# ===============================================================
# Example:

listOfNums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
newListOfNums = listOfNums[3:8] #<---------------------- Slicing will display up to the last slice but not the last slice. 
print(newListOfNums) # = [40, 50, 60, 70, 80]

# ===============================================================
# Slice assigment
# ===============================================================
# Example:

listOfNums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
listOfNums[:4] = [11,22,33,44]
print(listOfNums)

# ===============================================================
