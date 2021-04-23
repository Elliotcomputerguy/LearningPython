#!/usr/bin/python

# The if statement
# An if statement can be read as "if condition is True, execute the code i the following block. Otherwise if it is False, skip the block"

passwd = input('Enter pasword:')
if passwd == 'My$3cr3tpass':
    print('Access granted')
if passwd != 'My$3cr3tpass':
    print('Access denied')
print('Done')

# Interpreting any value as True or False 
# Below your see no comparison operator but the value itself is being treated as the condition. I caled it condition. 
# When it comes to evaluating a number as a condition. 0 is False and everything else is True.

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
# the number 0, and the value None. And of course the value False evaluates to False.

condition = input('\nEnter a value to mark condition as True or hit enter to skip to mark as False:')
if condition:
    print('the interpreter reads the above as if money != 0: #%s' % ('True'))
else: 
    print('False')