#!/usr/bin/python
# Indexing is the adding of a square bracket to the end of a string value or a variable containing a string with a number 
# between them. This number is called the index, and tells python which postion in the string has the character you want. 
# The index of the first character in a string is 0. The index 1 is the second character, etc. 

var = 'Elliot'
print(var[0],var[1],var[2],var[3],var[4],var[5])
var = 'Elliot'[0]
print(var)


# #Negative Indexes
# Negative indexes start at the end of a string and go backwards. The negative index -1 is the index of the last character in a string. 
# The index -2 is the index of the second from last character, and so on. 

#     0    1    2    3    4
#   [ i ][ n ][ d ][ e ][ x ]
#    -5   -4   -3   -2   -1

var = 'Elliot'
print(var[-1],var[-2],var[-3],var[-4],var[-5], var[-6])


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
    # a value of 5. But it will never go to 5 as it starts from 0 which is 5 0-4. You can use randint() and add a -1 
    # on the assignment statement. This way the variable high will be changed to 4 and you wont be out of range 
    print('word [ %s ] \t %s' % (position, word[position]))


# String Imutability
# Sequences fall into one or two categories. nutable or immutable. A sequence that is mutable is one that can change. 
# A sequence that is immutable means unchangable so it is one that cannot change.
# 
# So there is a number of ways to crack this egg. We can either use a for loop to create a new string OR 
# you can use slicing. 

message = input('Enter your message:')
new_message = ''
CHARACTERSTOREMOVE = 'aeiou'

for character in message:
    if character.lower() not in CHARACTERSTOREMOVE:
        new_message += character
        print('A new string has been created: %s' % (new_message))
print('Your message with the characters removed: \n %s' % (new_message))

# Or you can use slicing to change the characters. I want to change the character t with an X.

var = 'elliotcomputerguy'
var = var[:5] + 'X' + var[6:]
print(var)
