#!/usr/bin/env python

# #The List data type

# A list can contain a multitude of differnt elements. Strings, integers, tuples. Pretty much anything goes into a list. 
# Just like a string begins and ends with quotes. A list begins with a [ open bracket and ends with a closing bracket ]. 
# The elements stored inside a list are typed within the brackets. If there are more than one element in a list, 
# the elements are seperated by commas. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakers)

# ===============================================================
# Lists are ordered collections. You access the list by using a index. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakers[0]) # = Jordan
print(sneakers[3]) # = Adidas
# ===============================================================
# Just like in strings when we want to use a variable value in our string we can do the same for lists using string interpolation. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(f'I just got the latest Off White {sneakers[0]} 4\'s from the {sneakers[1]} drop on the sneakers app')

# ===============================================================
# Unlike tuples, lists are mutable. changing elements can be achieved with indexing, slicing or methods.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
sneakers[0] = 'zanotti' # You cannot assign a new element this way. If you was to specify sneakers[4] it would produce an error.
print(sneakers) # = ['zanoti', 'Nike', 'Yeezy', 'Adidas']
sneakers[0:1] = ['Christian Louboutin'] 
print(sneakers) # = ['Christian Louboutin', 'Nike', 'Yeezy', 'Adidas']
sneakers = sneakers[:0] + ['zanotti'] + sneakers[1:]
print(sneakers) # = ['zanoti', 'Nike', 'Yeezy', 'Adidas']

# ===============================================================
# to add to a list you can use the addition operator or use the append() method. 
# or use a for loop. Methods are coverd in List Methods. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
sneakers += ['zanotti']
print(sneakers) # = 'Jordan', 'Nike', 'Yeezy', 'Adidas' 'zanoti'

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
for i in range(len(sneakers)):
    sneakers[i] = ('item' + str(i))
    print(sneakers)

# ===============================================================
# We can get the length of a list by using the len() function. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(len(sneakers)) # = 4 (Remember Len() starts from 1. Indexing starts from 0.)

# ===============================================================
# You can index and slice lists as you would strings. Remember indexes start from 0
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(f'At index 1 in list sneakers is {sneakers[1]}') # = nike
print(f'using blank slicing with slice postion [2:] = {sneakers[2:]}') # = 'Yeezy', 'Adidas'
print(f'using blank slicing with slice postion [:2] = {sneakers[:2]}') # = 'Jordan', 'Nike' 
print(f'using negative indexing with index positon [-1] = {sneakers[-1]}') # = Adidas

# ===============================================================
# Using for loops to iterate over a list and looping through a slice.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
counter = 1
for element in sneakers:
    print(f'My favourite sneakers are [{counter}]: {element}'.capitalize())
    counter += 1

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
counter = 1
for element in sneakers[:3]:
    print(f'My favourite sneakers are [{counter}]: {element}'.capitalize())
    counter += 1

# ===============================================================
# concatenating lists and replication. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName = ['Zanotti']
for element in range(len(sneakers)):
    newListName += [sneakers[element]] #<-- Concatenation
print(newListName)

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName = ['Zanotti']
newListName += sneakers #<-- Concatenation

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName = []
for element in range(len(sneakers)):  #<-- Replication
    newListName += sneakers
print(newListName)

newListName = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName *= 5  #<-- Replication
print(newListName)

# ===============================================================
# To delete an element in a list you can use the del keyword. Methods are also available but covered in list methods.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
del sneakers[3]
print(sneakers) # = ['Jordan', 'Nike', 'Yeezy']
del sneakers[0:1]
print(sneakers) # = ['Nike', 'Yeezy']

# ===============================================================
# Lists can contain other lists or tuples. This is known as nested sequences. Genreal rule of thumb you wont most
# likely go deeper than two lists. It gets very confusing very fast when going deeper. Some examples below.
# ===============================================================
# Example:

listWithStringsIntegersTuplesLists = ['string', 2, ('tupleItem1', 'tupleItem2'), ['listItem1','listItem2']]
#                                    0   0      1               2                            3         
print(listWithStringsIntegersTuplesLists[0]) #= 'string'
print(listWithStringsIntegersTuplesLists[0][0]) # = 's'
print(listWithStringsIntegersTuplesLists[1]) # = 2
print(listWithStringsIntegersTuplesLists[2]) # = ('tupleItem1', 'tupleItem2')
print(listWithStringsIntegersTuplesLists[2][1]) # = ('tupleItem2')
print(listWithStringsIntegersTuplesLists[3]) # = ['listItem1','listItem2']
print(listWithStringsIntegersTuplesLists[3][1]) # = 'listItem2'

sneakers = [['Jordan', 'Nike'], ['Yeezy', 'Adidas']]
#                    0                  1 
print(sneakers[0]) #= ['Jordan', 'Nike']
print(sneakers[0][0]) # = 'Jordan'
print(sneakers[1]) # = ['Yeezy', 'Adidas']
print(sneakers[1][1]) # = 'Adidas'

sneakers = ['listitem0',[['Jordan', 'Nike'], ['Yeezy', 'Adidas']]]
#          0            1         0          1       1                                 
print(sneakers[0]) # = 'listitem0'
print(sneakers[1]) # = ['Jordan', 'Nike'], ['Yeezy', 'Adidas']
print(sneakers[1][0]) # = ['Jordan', 'Nike']
print(sneakers[1][0][0]) # = 'Jordan'
print(sneakers[1][1]) # = ['Yeezy', 'Adidas']
print(sneakers[1][1][0]) # = 'Yeezy'

sneakers = ['listitem0',['value1', 'value2'], [['Jordan', 'Nike'], ['Yeezy', 'Adidas']]]
#          0            1                     2         0          2        1            
           
print(sneakers[0]) # = 'listitem0'
print(sneakers[1]) # = ['value1', 'value2']
print(sneakers[2][0]) # = ['Jordan', 'Nike']
print(sneakers[2][1]) # = ['Yeezy', 'Adidas']

# ===============================================================
# in and not in operators are expressions of two strings connected by the in or not in operator that will evaluate to True 
# if the first string is inside the second string or in the case of the not in operator not in the second string. 
# Else the expression evaluates to False.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

for i in sneakers:
    print(i.title()) 

if 'rebok' not in sneakers:
    print('True')
else:
    print('False')

# ===============================================================
# populating lists with integers using the range() function and the list() function.
# ===============================================================
# Example:

myNumberList = []
for i in range(10):
    myNumberList += [i]

myNumberList = list(range(10))

# ===============================================================
# If your list is full of uppercase and lower case strings you can use
# the list() function with the map() function to change them. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

sneakers = list(map(str.lower, sneakers))
print(sneakers)

# ===============================================================
# List comprehensions allows you to generate a list in just one line of code. A list comprehension combines
# the for loop and the creation of new elements. This is a cleaner approach. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName = [sneakers[element] for element in range(len(sneakers))]
print(newListName)

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
newListName = [sneakers.lower() for sneakers in sneakers] #<-- This will convert the list to lowercase. This is using list comprehension
print(newListName)                                        #    rather than the map() function. 

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
# Example:

sneakerTuple = ('Jordan', 'Nike', 'Yeezy', 'Adidas')
print(sneakerTuple, '\n')
print(list(sneakerTuple), '\n')

sneakerList = list(sneakerTuple)
print(sneakerList, '\n')

# ===============================================================
# Picking a data structure. Lists, Tuples or Dictionaries. 
# Use a list when the data is in a natural order, updates are frequent during the program and iteration is the primary purpose.
# Use a tuple when modification is not required and iteration is a primary requirement. 
# Use a dictionary when the data is not ordered and order is not mattered. Frequent updates are required and looking up values is
# a primary purpose.
# ===============================================================