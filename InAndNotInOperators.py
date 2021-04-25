#!/usr/bin/env python
# #The in and not in Operators
# An expression of two strings connected by the in operator will evaluate to True if the first string is inside the second string
# Otherwise the expression evaluates to False. Notice that the in and the not in operators are case sensitive. 


var = 'Hello world'
if 'Hello' in var:
    print('True')
else:
    print('False')

if 'Hello' not in var:
    print('True')
else:
    print('False')

# #The not operator
# The not operator has to evalute to the opposite of True to enter the block which makes it true. 
print('--------------------------------')
username = ''
while not username:
    username = input('Enter your username:')

username = None
while not username:
	username = input('enter a value')

