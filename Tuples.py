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
# Converting the tuple datatype to a list datatype can be achieved with the list() function
# or if you want to convert from a list to a tuple you can use the tuple() function.
# ===============================================================

sneakerList = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakerList, '\n')
print(tuple(sneakerList), '\n')

SneakerTuple = tuple(sneakerList)
print(SneakerTuple)




