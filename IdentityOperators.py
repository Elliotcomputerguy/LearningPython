#!/usr/bin/env python


#Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location.
# ===============================================================
# Example:

sneakers = ['jordan', 'nike']

for i in sneakers:
    if i is i:
        print('True')
    else:
        print('False')
        
for i in sneakers:
    if i is not i:
        print('True')
    else:
        print('False')