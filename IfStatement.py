#!/usr/bin/python

# The if statement
# An if statement can be read as "if condition is True, execute the code i the following block. Otherwise if it is False, skip the block"

passwd = input('Enter pasword:')
if passwd == 'My$3cr3tpass':
    print('Access granted')
if passwd != 'My$3cr3tpass':
    print('Access denied')
print('Done')

