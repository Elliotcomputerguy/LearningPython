#!/usr/bin/env python

# Dictionaries
# Python dictionaries like lists and tuples store a multitude of different objects. Unlike tuples and lists 
# which store their information in sequences. Dictionaries store information in key value pairs. Each unique key
# is linked to a value. Key pairs are used to access their coresponding paired value. A key could link to a 
# string, a integer or a tuple or even another dictionary. You access dictionaries using brackets.
# ===============================================================
# Creating a dictionary and using the if statement to locate a key and print its value. 
# ===============================================================
# Example:

Quotes = {
'Einstein' : 'Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.',
'Einstein2' : 'Life is like riding a bicycle. To keep your balance you must keep moving.',
'Ghandhi' : 'You must be the change you wish to see in the world',
'George Bernhard Shaw' : 'A life spent making mistakes is not only more honorable, but more useful than a life spent doing nothing',
'Mary Engelbreit': 'If you don’t like something, change it. If you can’t change it, change the way you think about it',
'Helen Keller' : 'When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us',
'Abraham Lincoln' : 'I\'m a success today because I had a friend who believed in me and I didn\'t have the heart to let him down.',
}

if 'Einstein' in Quotes:
    print(Quotes['Einstein'])

# ===============================================================
# Iterating over a dicitonary with a for loop
# ===============================================================
# Example:

for i in Quotes:
    print(f'key: [{i}] Value: [{Quotes[i]}]')

# ===============================================================
# Nested dictionaries
# ===============================================================
# Example:

dictionary1 = {'key1': 'value1', 'dictionary2' : {'key2' : 'value2'}}

print(dictionary1['key1'])
print(dictionary1['dictionary2'])

# ===============================================================
# Assigning a dictionary value to a variable and changing a value in a dicitonary. 
# A Aliens interactive story game. Finish the 1st option and continue the story for the 2nd option.
# ===============================================================
# Example:
import sys
playerGunAmmoInventory = {'handgun' : 'berreta', 'bullets' : '8'}
playerHealth = {'playerHealthGood' : 'Healthy', 'playerHealthMedium' : 'Damaged', 'playerHealthBad' : 'Dead'}
playerHealthInventory = {'firstAid' : '1'}
player1Gun = playerGunAmmoInventory['handgun']
player1Ammo = playerGunAmmoInventory['bullets']
player1Health = playerHealth['playerHealthGood']
player1HealthInventory = playerHealthInventory['firstAid']

print(f'''
                               ALIENS
                               \\ \\ \\ \\

    The aliens lerk in the darkness. Ripley holds her {player1Gun} close.  
            \nslowly walking through the space ship. The sounds of bleeps and machines are all that can be heard.
            \nRipley stops and looks out through the window into the dark starry space beyond. Wondering how she 
            \ngot here in the first place. \'SMASH\' \'CRASH\' Ripley panics barely able to see into the darkness of the ships
            \nhallway. She fires her {player1Gun} shooting 3 rounds. 
''')
player1Ammo = int(player1Ammo) - 3
playerGunAmmoInventory['bullets'] = player1Ammo
print(f'''
    She runs backwards and takes cover behind a air shaft and waits. Silence. Just the beeps and machines fill the room. 
            \nRipley checks her mag in her {player1Gun}. Down to her last {player1Ammo} bullets. Her heart beating.
            \n'HIIIIISSSSS SSSSSSS' Ripley freezes. Thick saliva drips onto ripleys hand. She looks up slowly......  
''')
print('''
        0 - Exit
        1 - Shoot Gun
        2 - Run and Hide
''')
playerMenuList = ('0','1','2')
player1Move = ''
while player1Move not in playerMenuList:
    player1Move = input('Choose an option:')
if player1Move == '0':
    print('You deserted Ripley. She must go on alone.....')
    sys.exit()
elif player1Move == '1':
    print(f'''
            \nRipley doesnt move. squeezing her {player1Gun} tight, her heart beating. She slowly aims the gun
            \nupwards keeping her arms lowered to not make a sudden move. '\'BANG\' \'BANG\' \'BANG\' 
            \nThe alien lunges out with a swipe hitting Ripley. She falls to the floor. The alien hisses, 
            \ninjured scuttelling off into the darkness of the space ships dark hallway.
    ''')
    player1Health = playerHealth['playerHealthMedium']
    player1HealthInventory = int(player1HealthInventory) -1
    playerHealthInventory['firstAid'] = player1HealthInventory
    player1Ammo = int(player1Ammo) - 3
    playerGunAmmoInventory['bullets'] = player1Ammo
    print(f'''
            \nRipley; {player1Health}, reaches for a first aid pack from her pocket. Applies the first aid. 
            \nRipley has {player1HealthInventory} first aid kits left. 
    ''')

    player1Health = playerHealth['playerHealthGood']
# ===============================================================
# Because dictionaires are not ordered like lists or tuples they cannot be sliced. 
# Since Python 3.7 and later dictionaries now reemeber their insertion order of their key value pairs.
# The dictionaries are still unordered as you cannot access in their integer indexes.
# ===============================================================
# Removing key value pairs from dictionaries can be done just like we do in with lists. 
# by using del this option is only available for lists and dictionaries as tuples are immutable.

myDictionary = {'Mars': 'Mars has two moons'}
del myDictionary['Mars']

# ===============================================================
# Picking a data structure. Lists, Tuples or Dictionaries. 
# Use a list when the data is in a natural order, updates are frequent during the program and iteration is the primary purpose.
# Use a tuple when modification is not required and iteration is a primary requirement. 
# Use a dictionary when the data is not ordered and order is not mattered. Frequent updates are required and looking up values is
# a primary purpose.
# ===============================================================
