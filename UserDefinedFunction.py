#!/bin/usr/env python

# User defined functions break code down into smaller segments and are purposely desgined to perfrom specific actions. 
# Instead of repeating your code further down in your program to execute the same task you would call your function. 
# Python has built-in functions like print() range() len() etc. They all return a value when you pass an arguemnt inbetween
# the parenteses. Range() can take up to three arguments. Functions are made up of two parts known as the function signature 
# which defines the name of the function with the keyword def and expected parameters inside of the parentheses. 
# This will be the first line of the function. The function body contains the block of code that will execute everytime 
# the function is called. When you want to find out what a function does you can call the help() function with the function inside
# the parentheses. In order to let other people know what your function does you would create a docstring which is a triple quoted string
# at the top of your function. A function does not have to have any paramaters. Functions can be Idempotent or non Idempotent. 
# Basically in a nutshell a function that returns the same result everytime it is called, regardless of how many times it is called. 
# It is Idempotent. If different results return then this is non Idempotent and is also called a side effect. Test your functions with all
# input calls to ensure that your function provides the desired outcome every time regardless of what calls are made to it.
# ===============================================================
# Example:

def MyMagicBall(fortuneReply):
    ''' A return value of yes/no or maybe to a users input ''' #<--- This is called a docstring for the help() function.
    import random                                                    # By placing a docstring into the fucntion it will help
    dict = {                                                         # other developers understand what the function does.                                                                          
        'Yes': 'Yes, your chances are highly likely',                #  help(myMagicBall)
        'No' : 'No, it is not probable',
        'Maybe' : 'Maybe, the forces are unclear',
    }
    answer = random.choice(list(dict.values())) #<-- As a dictionary is not ordered we convert it to a list so the random.choice()                                                
    return answer                               # function can iterate over the list.

userFortuneQuestion = input('Ask your question:')
print(MyMagicBall(userFortuneQuestion)) #<-- This line calls the function and passes in the argument from the above input() function.
                                        # It then returns the expression of a random choice from the dictionary of answers. 

# ===============================================================
# Parameters are variables that contain the arguments passed when a function is called. Parameters are automatically deleted when 
# the function returns. A parameter is a variable name in between the parentheses in the def statement. 
# In other words an argument is the value that is assigned to a variable which are called parameters between the parentheses of a function.
# Arguments can be passed into a function in multiple ways. Keyword arguments use assignment statements directly assigning the 
# argument (value) to the variable (parameter) inside the function call. 
# ===============================================================
# Example:

def userProfile(forename, surname, age):
    
    dict = {} #<---- Local scope
    dict.setdefault('forename', forename)
    dict.setdefault('surname', surname)
    dict.setdefault('age', age)

    return print('Hello', dict['forename'], 'your information has been stored...')
    
name = input('name>')
surname = input('surname>')
age = input('age>')

userProfile(name, surname, age)

# ===============================================================
# You can assign default values for each parameter if the arguments are not passed into the function call.
# If you have a parameter that is not using a default value it will need to be placed after any parameter with default values.
# You can also make arguments optional by using an assignment operator to an empty string.
# ===============================================================
# Example:

def userProfile1(forename='firstName', surname='SecondName', age=''): #<--- Default values with age as a optional value.
    dict = {}             
    
    if age:                                                        # REMEMBER any parameter using default or optional values
        dict.setdefault('forename', forename.title())              # must come ater any parameters not using default or optional values!
        dict.setdefault('surname', surname.title())                # The if condition will evaluate to True if age is True. 
        dict.setdefault('age', age)                                # else it will only write the forename and surname to the dictionary. 
        userInfo = f'hello {forename} {surname} {age} your information has been stored'  
    else:
        dict.setdefault('forename', forename.title())  
        dict.setdefault('surname', surname.title())
        userInfo = f'hello {forename} {surname} your information has been stored'
    return userInfo

userProfileArgrument = userProfile1(surname='stenning') #<--------- The forname variable is not included in the parenteses and will use the default value.
print(userProfileArgrument)

# ===============================================================
# You then have positional arguments which need to be input into the function in the same order the parameters were written. 
# If your function is taking first names as the first argument and then surnames as the second name. It has to be in order. 
# If these positional arguments are mixed up then your have a first name as the surname and a surname as the first name.
# ===============================================================
# Example:

# is using global scope and using positional parameters

userProfileList = []  #<---------- Global scope
def userProfile0(forename, surname, age):
    
    userProfileList.append(forename.title().strip()) #<---------- Global scope
    userProfileList.append(surname.title().strip())  #<---------- Global scope
    userProfileList.append(age)                      #<---------- Global scope

    if forename and surname and age in userProfileList:
        userInfo = 'Hello, %s, your information has been stored...' % (forename)
        return userInfo

userProfileName = input('name:')
userProfileSurname = input('surname:')
userProfileAge = input('Age:')
userProfileArgument = userProfile0(userProfileName, userProfileSurname, userProfileAge)
print(userProfileArgument)

userProfileArgument = userProfile0('Jack', 'Daniels', '104')
print(userProfileArgument)

# ===============================================================
# You can also pass an arbitrary number of arguments into a function from the calling statement. 
# using the *args parmameter for positional or **kwargs for keyword arguments. Your arguments dont have to be 
# named args or kwargs but must have the * for positional and ** for keyword arguments next to the name of choice.
# All arguments will be placed inside of a tuple.
# ===============================================================
# Example:

def sneakerStock(*args):
    sneakers = {

        'model' : 'Jordan 1 Retro High Travis Scott',
        'stock' : '5',
        '7' : '0',
        '8' : '1',
        '9' : '1',
        '10' : '2',
        '11' : '1',
    }

    for sneaker in range(len(args)): #<-- For range of tuple iterate over items.
        if args[sneaker] in sneakers: #<-- if the tuple element exist in the dictionary then proceed
            lookup = sneakers.get(args[sneaker], 'Invalid Lookup') #<--- get items from dictionary
            print(lookup)   #<------ print items

sneakerStock('model', 'stock', '7')

# ===============================================================
# When a function is called, a local scope is created. Variables created during a function call exist in the local scope.
# Parameters always exist in a local scope. When a function returns, the local scope is destroyed and all variables are forgotten. 
# A variable in the local scope is still a sperate variable from a global scope variable even if the two variables have the same name.
# Variables created outside of every function exist in a global scope. When the program exits, the global scope is destroyed and all
# variables in the program are forgotten. 
# If you want a variable that is inside of a function to be a global variable you use the global statement with the variable name as the
# first line after the def statement. 

# Rules

# 1) Variables outside of all functions are always global variables.
# 2) If a variable in a function is never used in an 'assigment statement', it is a global variable.
# 3) If a variable in a function is not used in a 'global statement'; but is used in an assigment statement, it is a local variable
# 4) If a variable in a function is used in a 'global statement' it is a global variable when used in that function.
# ===============================================================
# Example:

def Yes_Or_No(param):
    answerTuple = ('yes', 'no') #<----------- Local scope
    for i in range(len(answerTuple)):
        if param.lower().strip() == answerTuple[i]:
            answer = answerTuple[i]
            global var #<-------------------------------Global scope
            print(var)
            return answer

var = 'i am a global variable'
userQuestion = input('Enter Yes or no:') #<------ Global scope
print(Yes_Or_No(userQuestion))

# ===============================================================
# Functions help segement code blocks and make code clearer to read. You can further this readability by storing your functions as 
# modules in a seperate py file and then import them as modules into your main program. There are ways to achieve this. 
# You save your functions to seperate .py files in the same directory to the py file you call the modules from. You would type the 
# import statement as you would if you were importing math or range. Python would read the line and open the file and copy the functions
# across making it available. When calling the function from the imported module you would enter the name of the module that 
# you imported followed by the name of the function, seperated by a dot. moduleName.functionName() 
# The second method is to import a specific function from the module. At the top of your program that you wish to import
# the modules into. You would type 'from moduleName import functionName' You can import as you want by sperating by a comma. 
# Using this syntax you do not need to use the dot notation when you call a function. Because we have explicitly imported the function.
# With the second way we can specify an alias if the function name provides any confliction. 'from module import function as alias'
# If you wist to import all functions in a module you can specify the * wildcard. 'from moduleName import *'
# ===============================================================
# Example:

# [1] save below function as passwordCreator.py in a directory of choice. 
# [*] As passwordCreator() calls jumbleWord() you import jumbleWord() inside the passwordGenerator() function.
# [2] save the second function marked with [2] as jumbleWord.py in the same directory.
# [3] create a new file .py and import passwordCreator and then call it. 

def passwordCreator():
   # from jumbleWord import jumbleWord
    ''' Generate a number of choice of randomized passwords with the choice of password length '''
    print('''
        
██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████       ██████  ███████ ███    ██ ███████ ██████   █████ ████████  ██████  ██████  
██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██   ██    ██    ██ ██   ██ 
██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██     ██   ███ █████   ██ ██  ██ █████   ██████  ███████   ██    ██    ██ ██████  
██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██   ██    ██    ██ ██   ██ 
██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████       ██████  ███████ ██   ████ ███████ ██   ██ ██   ██   ██     ██████  ██   ██ 

        
        ''')

    userPasswordLength = int(input('[+] Please enter the length size 0 - 50:>')) #<---------- Local scope
    userGeneratedPasswords = int(input(' [+] How many passwords would you like to create:>')) #<---------- Local scope
    userPassList = [jumbleWord(userPasswordLength) for _ in range(userGeneratedPasswords)] #<---------- Local scope
    generatedPasswordList = f' [+] Your list has been created using {userPasswordLength} as your pass length\n {userPassList}' #<---------- Local scope
    return generatedPasswordList

# [2] save below function as jumbleWord.py

def jumbleWord(lengthNumber):
    ''' jumbleWord creates a random string from the character set abcdefghijklmnopqrstuvwxyz1234567890!"£$%&*()@?~#:;
        The function expects an integer argument to return a string size from the character set. 
        Example: jumbleWord(10) will return a randomized string size of 10 characters from the above character set. 
    '''
    import random
    passLength = lengthNumber #<---------- Local scope
    jumbledWord = '' #<---------- Local scope
    CHARACTERS = 'abcdefghijklmnopqrstuvwxyz1234567890!"£$%&*()@?~#:;'
    for characters in CHARACTERS:
        randomizer = random.choice(CHARACTERS)
        if len(jumbledWord) < passLength:
            jumbledWord += randomizer
    return jumbledWord

# [3] Create a new file .py and add the below.

# from passwordCreator import passwordCreator

print(passwordCreator())

# ===============================================================
# Refactoring is where your code is working but you want to improve the logic or break it into functions. 
 # refactoring makes your code more readable easier to extend. 
# ===============================================================
