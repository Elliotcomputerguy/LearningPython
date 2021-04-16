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

