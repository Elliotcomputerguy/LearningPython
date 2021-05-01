#!/bin/usr/env python

# User defined functions break code down into smaller segments and are purposely desgined to perfrom specific actions. 
# Instead of repeating your code further down in your program to execute the same task you would call your function. 
# Python has built-in functions like print() range() len() etc. They all return a value when you pass an arguemnt inbetween
# the parenteses. Range() can take up to three arguments. The function is made up of two parts known as the function signature 
# which defines the name of the function with the keyword def and expected parameters inside of the parentheses. 
# This will be the first line of the function. The function body contains the block of code that will execute everytime 
# the function is called. When you want to find out what a function does you can call the help() function with the function inside
# the parentheses. In order to let other people know what your function does you would create a docstring which is a triple quoted string
# at the top of your function. A function does not have to have any paramaters. Side effects are known as unexpected return values that
# are not intended. 
# ===============================================================
# Example:

def MyMagicBall(fortuneReply):
    ''' A return value of yes/no or maybe will be returned to a users input ''' #<--- This is called a docstring for the help() function.
    import random                                                               # By placing a docstring into the fucntion it will help
    dict = {                                                                    # other developers understand what the function does.                                                                          
        'Yes': 'Yes, your chances are highly likely',                           #  help(myMagicBall)
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
# In other words an argument is the value that is assigned to a variable between the parentheses of a function.
# Arguments can be passed into a function in multiple ways. Keyword arguments use assignment statements directly assigning the 
# argument (value) to the variable (parameter) inside the function call. 
# ===============================================================
# Example:

def userProfile(forename, surname, age):
    dict = {}
    dict.setdefault('forename', forename)
    dict.setdefault('surname', surname)
    dict.setdefault('age', age)

    userInfo = print('Hello', dict['forename'], 'your information has been stored...')
    return userInfo
    
userProfile(forename='Elliot', surname='Stenning', age='35')



# There is positional arguments which need to be in the same order the parameters were written. 
# If your function is taking first names as the first argument and then surnames as the second name. It has to be in order. 
# If these positional arguments are mixes up then your have a first name as the surname and a surname as the first name.
#  
# ===============================================================
# Example:

def Yes_Or_No(param):
    answerTuple = ('yes', 'no')
    if param in answerTuple[0]:
        return answerTuple[0]
    elif param in answerTuple[1]:
        return answerTuple[1]
    else:
        answer = ('You did not enter yes or no!')
        return answer
    
userQuestion = input('Enter Yes or no:').lower().strip()
print(Yes_Or_No(userQuestion))

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



# Convert Temprature functions.
# ===============================================================

def convert_cel_to_far(c):
    f = c * 9/5 + 32
    return float(f)

userCelciusConvert = int(input('Enter a Celsius temprature to convert to Farneheit:'))
print(convert_cel_to_far(userCelciusConvert))

def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    return float(c)

userFarneheitConvert = int(input('Enter a Farenheit temprature to convert to Celsius:'))
print(convert_far_to_cel(userFarneheitConvert))









     