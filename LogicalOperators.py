#!/usr/bin/env python

# and, or, not are logical operators. When combined with simple conditions they become compound conditions 
# In the while loop below the logical not operator is used. it works alot like the word not. Putting the not in front of a condition
# creates a new condition that evaluates to the opposite of the original. This means not username is True and the loop will run. 
# Since username is intialized to an empty string, it starts out as False. That makes the not username True. If the user enters no value 
# the condition is still True and will continue to loop. 
# not username is True when username is False. And not username is False when username is True. 
# when the logical operator and is used it will be joining simple conditions together making a compound condition. 
# the compound condition is True when both simple conditions that the logical operator concatenates evaluate to True.  
# A compound condition created with an or logical operator is True as long as at least one of the simpler conditions is True. 
# ===============================================================
# Example:

users = ['root','admin','user']
pword = ['password1','password2','password3']
username = ''
while not username:
    username = input('username:')
    if username in users or username == 'secretuser':
        passwd = input('password:')
        if passwd in pword and passwd == pword[0]:
            print('Access granted')
    else:
        print('Access denied')
# ===============================================================