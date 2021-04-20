#!/usr/bin/python

# #The List data type

# A list value can contain other values. Just like a string begin and end with quotes. 
# A list value begins with a [ open bracket and ends with a closing bracket ]. The value stored inside the list are typed within the brackets.
# If ther is more than one value in the list, the values are seperated by commas. 

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakers)

# You can index and slice lists as you would strings. Remeber indexes start from 0

print(sneakers[0])
print(sneakers[:2])

# you can interate through a list with a for loop statement

for sneaks in sneakers:
    print('My favourite sneakers are', sneaks)

# Using the list() function to convert range objectsto lists
# if you need a list value that has increasing integer amounts, you could have code like the below to build a list. 

myList = []
for i in range(10):
    myList = myList + [i]
print(myList)

# How ever it is easier to directly make a list from a range argument that range() function returns by using list() function. 
print('------------------------------')
myList = list(range(10))
print(myList)

print('------------------------------')
def main():
    myList = list(range(10))
    print(myList[0])
    print(myList[1])
    print(myList)

main()

# The list() can also convert strings into list value's. 
def func():
    myList = list('Elliot')
    print(myList[0])
    print(myList)

func()

# #Reassigning the items in Lists. The items inside a list can be modified. You use the index to with a an assignemnt statement.
print('--------------------------------')
sneakers = ['jordan', 'nike', 'yeezy', 'addidas']
sneakers[3] = 'Reebok'
print(sneakers)

print('---------------------------------')
def func2():
    sneakers = 'jordan' + 'nike' + 'yeezy' + 'addidas'
    myList = list(sneakers)
    print(myList)
func2()

# #lists of lists
# list values can also contain other list values. 
print('----------------------------------------')
def func3():
    listInList = [['dog', 'cat'], [1, 2, 3]]
    print(listInList[0]) #= value dog,cat
    print(listInList[0] [0]) # = value dog
    print(listInList[1]) # = value 1,2,3
    print(listInList[1][2]) # = value 3
func3()

# You can also use the len() function to tell how many values are in the list

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
print(len(sneakers)) 

# You can also use the in or not in operator 

for i in sneakers:
    print(i.title()) # .title is another method i learned (:

if 'rebok' not in sneakers:
    print('True')
else:
    print('False')

# List Concatenation and Replication with the + an * Operator
# Just like how + and * operators can concatenate and replicate strings, the same operators can concatenate and replicate lists. 

var = ['hello'.title()]
var2 = ['world'.title()]
var = var + var2
var = var * 5
print(var)

