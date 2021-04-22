#!/usr/bin/python
# If you want to get more than once character from a string, you can use slicing of indexing.
# A slice also uses the [ and ] square brackets but has two integer indexes instead of one.
# The two indexes are seperated by a colon : 

var = 'Elliot'[0:3]
print(var)

var = 'Hello World'[0:5]
print(var)
var = 'Hello World'[-11:-6]
print(var)
var = 'Hello world'[0]
print(var)
var = 'Hello world'[-0]
print(var)


# Notice how 0 and -0 are the same. Remember that -1 is the last character in negative indexes 

# Unlike indexes, slicing will never give you an error if you give it too large of an index for the string.

var = 'Hello world'[0:999]
print(var)
var = 'Hello world'[2:999]
print(var)
var = 'Hello world'[1000:2000]
print(var)

# #Blank Slice Indexes
# If you leave out the first index of a slice, python will automatically think you want to specify index 0 for the first index. 
# The expression 'Hello'[0:3] and 'Hello'[:3] evaluate to the same string. 'Hel'

# to help make it more visibly clearer. Put a 0 in if the slice is after the colon. Then take it out. 
var = 'Hello world'[:3] # <-- Get only characters before 3 = 'Hel'
print(var)

# If you leave out the second index, python will automatically think you want to specify the rest of the string. 
# 'Hello'[2:] evaluates to the value 'llo world'

var ='Hello world'[2:] # <-- Get characters only After 2 = 'llo world'
print(var)


# #Reassigning characters in strings
# While you can reassign items in a list, you cannot assign a character in a string value. You have to use slicing instead

var = 'Hello'
var = var[:0] + 'G' + var[1:]
print(var)

print('--------------------------')
var = 'string'
var = var[:4] + 'x' + var[5:]

# Slicing is a simple way to get a substring from a larger string.

# 0    1    2    3    4   5
# [ p ][ i ][ z ][ z ][ a ]
# -5  -4    -3   -2   -1   
# 
print('--------------------------')

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
