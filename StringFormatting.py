#!/bin/usr/python

# String formatting also known as string interpolation. String formatting with the %s text is a way of placing one string inside another one.
# The first %s text in the string gets replaced by the first value in the parentheses after the % at the end of the string. 

var1 = 'dog'
var2 = 'cat'
var3 = 'rat'
print('the %s ate the %s that ate the %s.' % (var1, var2, var3))
