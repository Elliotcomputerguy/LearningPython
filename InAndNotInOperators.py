#!/usr/bin/python
# The in and not in Operators
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

# This while loop will not exit until username is evaluated to True. Ie a value has been entered and assigned to the username variable.
print('--------------------------------')
username = ''
while not username:
    username = input('Enter your username:')
