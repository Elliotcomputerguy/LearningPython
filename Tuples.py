#!/usr/bin/env python

# #Tuples
# Tuples are a type of sequence, like strings. But unlike strings, which can only contain characters, tuples can contain elements of any type.
# That means you can have a tuple that stores a bunch of high scores for a game. Or one that stores employee names. You can create
# tuples with both strings and integers. You can create tuples that contains a sequence of a graphic image, sound files etc. 
# What ever you can assign to a varible, you can group together and store as a sequence in a tuple. Tuples are also faster than lists.

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
    print(i, end=' ' + '\n')

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

print(tuple1)
