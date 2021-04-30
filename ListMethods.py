#!/usr/bin/env python

# Methods are just like functions, except they are attached to a non-module value with a period.
# A function is not a method just because it is in a module. It can some times get confusing.

# Appending list elements via the method append() is the easiest solution rather than concatenating.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
sneakers.append('Zanotti')

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

newListName = ['Zanotti']
for element in range(len(sneakers)):
    newListName.append(sneakers[element])
print(newListName)

# ===============================================================
# If you want to insert a new item at any position you can use the insert() method. If you specify a position that is already allocated
# it will not remove the element but change the position of the element. You specify the index and then the element you want to add. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
sneakers.insert(0, 'Zanotti')
print(sneakers) # = ['Zanotti', 'Jordan', 'Nike', 'Yeezy', 'Adidas']
print(sneakers[0]) # = Zanotti
print(sneakers[1]) # = Jordan

# ===============================================================
# Sometimes you will want to use a list element after removing it from the list. The pop() method allows you do just this. 
# If you do not pass an argument into the pop() method it will remove the last element in the list. To choose which element 
# you want to remove add the index position. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
popVariable = sneakers.pop()
print(sneakers)
print(popVariable)
popVariable = sneakers.pop(0)
print(sneakers)
print(popVariable)

# ===============================================================
# How to pop in a nested list.
# ===============================================================
# Example:

sneakers = [['Nike', 'Yeezy', 'Jordan', 'Adidas', 'Zanotti'],[8, 7, 9, 6, 5]]
popped = sneakers[0].pop(0)
popped1 = sneakers[1].pop(0)
print(popped)
print(popped1)

# ===============================================================
# if you only know the value of the list element you can use the remove() method. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

removeItem = 'Adidas'

def func():
    print(f'List item located. Removing item {removeItem}')

if removeItem.upper() in sneakers:
    func()
    sneakers.remove(removeItem.upper())
elif removeItem.lower() in sneakers:
    func()
    sneakers.remove(removeItem.lower())
elif removeItem.capitalize() in sneakers:
    func()
    sneakers.remove(removeItem.capitalize())
else:
    print('Cannot locate List item')

print(sneakers)

# ===============================================================
# Most likely when items are assigned to a list they are in a unpredicable order. To sort a list alphabetically or in reverse order
# you can use the sort() method. You can either sort the list permanently or just display sorted list in the print() function. 
# When all values are not in lowercase sorting a list alphabetically is a little more complicated. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

print(sorted(sneakers)) #<-- Only print out the list in alphabetical order. If used with numbers will put them in numerical order.
print(sneakers)
sneakers.sort() #<-- Permanently sort the list alphabetically. 
print(sneakers)
sneakers.sort(reverse=True) #<-- sort list in Reverse alphabetical order. Will reverse numerical order. Good for scores by keeping highest at top.

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
for sneaker in sorted(sneakers):
    print(sneaker)

# ===============================================================
# To reverse the list you can use the reverse() method. Again there is no way to just print this and 
# will be a permanent change. To reverse it back you simply rerun the reverse() method
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']

sneakers.reverse()
print(sneakers)
sneakers.reverse()
print(sneakers)

# ===============================================================
# Index method will return the integer index position of the list element. 
# If there are duplicates of the element then it will produce the first found.
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
sneakers.index('Jordan')

# ===============================================================



