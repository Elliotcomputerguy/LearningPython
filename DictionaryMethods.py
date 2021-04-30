#!/usr/bin/env python

# Like lists dictionaries also have quite a number of methods to access and view dictionary keys with their associated values.
# You would use the keys() method to locate a key. The values() method to locate a value and items() method to locate all
# items in a list. 
# ===============================================================
# Example:

jordan1SneakerBred = {
    'Jordan' : 'Jordan 1 high Bred',
    'Size'   : '8.5 US',
    'Quantity' : '5',
    }

for sneakerKey in jordan1SneakerBred.keys():
    print(sneakerKey)

if 'jordan' in jordan1SneakerBred.keys():
    print('Located key')
else:
    print('Cannot locate key')

for sneakerValue in jordan1SneakerBred.values():
    print(sneakerValue)

if 'Jordan 1 high Bred' in jordan1SneakerBred.values():
    print('Located value')
else:
    print('Cannot locate value')

for sneakerItems in jordan1SneakerBred.items():
    print(sneakerItems)

if 'Jordan 1 high Bred' in jordan1SneakerBred.items():
    print('Located value')
else:
    print('Cannot locate value')

# ===============================================================
# When looking for keys in a dictionary with brackets dictionary['sneaker'] if it does not exist.
# an error will be returned. In order to not get an error the get() method is used to provide an alternative return
# value if the key cannot be located. 
# ===============================================================
# Example: 

jordan1SneakerBred = {
    'Jordan' : 'Jordan 1 high Bred',
    'Size'   : '8.5 US',
    'Quantity' : '5',
    }

print(jordan1SneakerBred.get('Yeezy', 'Key Does not exist'))

# ===============================================================
# The setdefault() method can be used for simplicity rather than using the assigment operator 
# to assign a new key and value to a dict. Unlike the assignment statement where you will overwrite a key if 
# you assign the same key name the setdefault() method will not overwrite.
# ===============================================================
# Example: 

jordan1SneakerBred = {
    'Jordan' : 'Jordan 1 high Bred',
    'Size'   : '8.5 US',
    'Quantity' : '5',
    }

jordan1SneakerBred.setdefault('colour', 'black')
print(f'\n{sorted(jordan1SneakerBred.items())}')
print(f'\n{jordan1SneakerBred}')
jordan1SneakerBred.setdefault('colour', 'blue')
print(f'\n{sorted(jordan1SneakerBred.items())}')
print(jordan1SneakerBred)

# ===============================================================