#!/usr/bin/env python


# String Imutability
# Sequences fall into one or two categories. mutable or immutable. A sequence that is mutable is one that can change. 
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