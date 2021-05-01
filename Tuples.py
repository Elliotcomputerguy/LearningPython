#!/usr/bin/env python

# A tuple is similar to a list which can contain a multitide of different data types. Anything that can be assigned to a variable 
# can be injected into a tuple. Tuples are accessed the same as lists via indexing and slices. The tuple data type is immutable.
# The Python interpreter can execute tuples faster than lists.
# ===============================================================
# Creating an empty tuple
# ===============================================================
# Example:

inventory = ()

# ===============================================================
# If you are adding one element to a tuple you must define the trailing comma.
# ===============================================================
# Example:

myTuple = ('value',) #<--- Take away both commas and you will end up with value1valuevaluevaluevaluevalue
newTuple = ('value1',) #<---- Take away either one of the commas and you will get an error 'can only concatenate tuple (not "str") to tuple'
for i in myTuple:            
    newTuple += myTuple
print(newTuple)

myTuple = ('value',)
newTuple = ('value1')
print(myTuple[0]) #<------- As we have added the comma you will see the expression evaluate to 'value'
print(newTuple[0]) #<------ As we have not added the trailing comma the expression will evaluate to 'v'

# ===============================================================
# Treating a tuple as a condition
# As a condition an empty tuple is False. As the tuple has no elements this means that the if not inventory is True. 
# ===============================================================
# Example:

if not inventory:
    print('The tuple is empty')

# ===============================================================
# building the tuple
# ===============================================================
# Example:

inventory = ('value1', 'value2', 'value3')

# ===============================================================
# loop through a tuple
# ===============================================================
# Example:

for i in inventory:
    print(i, end=' ')

# ===============================================================
# get the length of your tuple
# ===============================================================
# Example:

print(len(inventory))
# pass the length of your tuple into the range function and loop.
for i in range(len(inventory)):
    print(i)

# ===============================================================
#  using the not in and in operators
# ===============================================================
# Example:

if 'value1' in inventory:
    print('value1 is in inventory')
if 'value5' not in inventory:
    print('value5 not in inventory')

# ===============================================================
# indexing tuples
# ===============================================================
# Example:

print(inventory[0])

# ===============================================================
# slice tuples
# ===============================================================
# Example:

print(inventory[0:1])

# ===============================================================
# blank slice indexing
# ===============================================================
# Example:

print(inventory[1:])

# ===============================================================
# tuple immutablility
# like strings tuples are immutable. 
# Although you cannot change tuples, like strings, you can create new tuples from existing ones.
# ===============================================================
# Example:

tuple1 = ('value1', 'value2')
tuple2 = ('value3', 'value4')
tuple1 += tuple2

# ===============================================================
# Multiple assigment trick also known as tuple unpacking is a shortcut that allows you
# to assign multiple variables with values in a list in one line. You have the correct amount 
# of variables or an error will be thrown
# ===============================================================
# Example:

sneakers = [('Jordan', 'Nike'), ('Yeezy', 'Adidas')]
for sneaker in sneakers:
    tupleElement1, tupleElement2 = sneaker
    print(f'{tupleElement1} {tupleElement2}')

# ===============================================================
# Changing the tuple datatype to a list datatype can be achieved with the list() function
# or if you want to change from a list to a tuple you can use the tuple() function. This also works for dictionaries.
# As dictionaries are not ordered and if your program wants to use random to iterate over the dictionary to bring back a value
# or key you can convert to a list.
# ===============================================================
# Example:

sneakerList = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakerList, '\n')
print(tuple(sneakerList), '\n') #<---- Print the list as a tuple datatype

sneakerTuple = tuple(sneakerList) #<--- Create a new tuple datatype with all the list elements. 
print(sneakerTuple, '\n')

jordan1SneakerBred = {
    'Jordan' : 'Jordan 1 high Bred',
    'Size'   : '8.5 US',
    'Quantity' : '5',
    }
import random
variable = random.choice(list(jordan1SneakerBred.values())) #<---- Print all the dictionary values as a list datatype
print(variable)

newlist = list(jordan1SneakerBred.values()) #<--- Create a new list datatype with all the dictionary values.  
print(newlist)                                    # If you do not specify a method only the keys will be returned.

# ===============================================================
# If you have multiple entries in a dictionary or list or tuple and you do not want to ommit all duplicated values 
# you can use the set() function.
# ===============================================================
# Example:

playerGunAmmoInventory = ('8', '8')
for value in set(playerGunAmmoInventory):
    print(value)

# ===============================================================
# Picking a data structure. Lists, Tuples or Dictionaries. 
# Use a list when the data is in a natural order, updates are frequent during the program and iteration is the primary purpose.
# Use a tuple when modification is not required and iteration is a primary requirement. 
# Use a dictionary when the data is not ordered and order is not mattered. Frequent updates are required and looking up values is
# a primary purpose.
# ===============================================================




