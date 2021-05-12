#!/usr/bin/env python

# #Numbers
# With any programming language you are going to use numbers for a multitude of reasons. You simply cant avoid them.
# When you instruct python to perform a calculation this is known as an expression. Expressions are made up of values connected
# by operators. When Python calculates the expression you would say Pyhton has evaluated the expression. 
# Unlike statements An expression will always evlaute to a single value. This is key to remember.
# ===============================================================
# Example

var = 2 + 4 # = 6
print(var) 
var += 5 # = 11
print(var)
var *= 2 # = 22
print(var)

# ===============================================================
# 2+4 is an expression. Expressions are made up of values (the numbers) connected by operators. 
#     =============================
#     |   2         +         4   |
#     | Value    Operator    Value|
#     =============================
#                  ||
#              Expression
# ===============================================================
# Mathematical Operators
# =========================================
# Operator         Operation    Expressions
# =========================================
#     +            Addition     2 + 2 = 4
#     -           Subtraction   3 - 1 = 2
#     *        Multiplication   2 * 3 = 6 
#     **       Exponentiation   2 ** 10 = 1024
#     /            Division     5 / 3 = 1.6666666666666666666666666666667
#     //       Floor division   5 // 3 = 1
#     %              Mod        7 % 3 = 1
# ==========================================
# ===============================================================
# Integers and Floating points
# Whole numbers like 4, 0, 99 are called integers. Numbers with fractions or decimal points (3.5 or 42.1) are floating point numbers.
# ===============================================================
# Example:

var = 5 # 5 = Integer
print(var)
var = 5.5 # 5.5 = Floating point
print(var)

# ===============================================================
# Order of Operations PEMDAS
#
# P Parentheses first
# E Exponents (ie Powers and Square Roots, etc.)
# MD Multiplication and Division (left-to-right)
# AS Addition and Subtraction (left-to-right)
#
# Divide and Multiply rank equally (and go left to right).
# Add and Subtract rank equally (and go left to right)
# ===============================================================
# Example:

var = 7 + (6 * 5**2 + 3) # = 160
print(var)

# ===============================================================
# Start with:	7 + (6 × 5^2 + 3)
# Parentheses first and then Exponents:	7 + (6 × 25 + 3)
# Then Multiply:	7 + (150 + 3)
# Then Add:	7 + (153)
# Parentheses completed:	7 + 153
# Last operation is an Add:	160
# ===============================================================

7 + (5 - 1) * ((7 + 1) / (3 - 1))
     
# Start with all parentheses first. (5 - 1) then (7 + 1) then (3 - 1)
# You then divide the evaluated value from 7 + 1 and 3 - 1 as they are in nested parentheses.
# You then multiply the evaluated value of 5 - 1 and the evaluated value from the division of 7 + 1 and 3 - 1. 
# You then add 7 to the evlauted value from the multiplication.

(5 * ((25 % 13) + 100) / (2 * 13)) // 2

# Start with (25 % 13) = 12
# Add a 100 = 112 and multiply by 5 = 560
# complete (2 * 13) = 26
# divide 560 by 26 = 21.xxxxxxx
# finish off by dividing with the floor operator 21 // 2 = 10.0

# ===============================================================
# The exponent of a number says how many times to use the number in a multiplication.
# ===============================================================
# Example:

# In 8^2 the "2" says to use 8 twice in a multiplication,
# so 8^2 = 8 × 8 = 64

exponent = 8 ** 2
print(exponent) 

# In words: 5^3 could be called "5 to the third power", "5 to the power 3" or simply "5 cubed"
# 5 x 5 x 5 = 125
# 5 x 5 = 25 x 5 = 125

exponent = 5 ** 3
print(exponent)

# The exponentiation operator uses right-sided binding.
2 ** 2 ** 3 # = 256

# 2 ** 3 = 8
# 2 ** 8 = 256

# ===============================================================
# A prime number is a whole number that cannot be made by multiplying other whole numbers.
# if we can make it by multiplying other whole numbers it is a Composite Number And 1 is not prime and also not composite.
# If you divide the number by 2 and are left with a remainder then it is a prime number. If it does not have a remainder it is a 
# composite.
# ===============================================================
# Example:

4 / 2 # = composite
5 / 2 # = prime 
6 / 2 # = composite
7 / 2 # = prime 

# ===============================================================
# PrimeNumber application. Full application is in MyPythonApplications Git repo
# ===============================================================
# Example:

def primeNumbers(maxCount, file):
    # import pathlib, sys and time modules
    import pathlib
    ''' Count as many Prime numbers as you like, just give me a number to count to and a file to write to. ''' #<-- Doc String 
    # initalize variables
    iterator = 2 # iterator in while loop for prime 
    primeList = [] # prime number list
    compositeList = [] # non prime number list
    # create absolute path
    path = pathlib.Path.home() / file
    # check if file exists. If user does not change value of file then use default parameter value.
    if path.exists():
        # if user does not specify a maxCount value. use default parameter value of 100.
        while iterator <= maxCount:
            # when you mod by 2 it only evaluates to either a 0 or 1.
            # If it is a 0 it is not prime. If it is 1 it is prime.
            if iterator % 2 == 0:
                compositeList.append(iterator)
                iterator += 1
            else:
                primeList.append(iterator)
                iterator += 1
        # insert -1 into the list on every iteration of 10 with for loop.
        for i in range(0, maxCount, 11):
            primeList.insert(i, -1)
        # convert list into string and repalce -1 with a new line break and remove commas and brackets.
        primeList = ''.join(str(primeList)).replace('-1', '\n').replace(',', '').replace('[', '').replace(']','').strip()
        # insert -1 into the list on every iteration of 10
        for i in range(0, maxCount, 11):
            compositeList.insert(i, -1) 
        # convert list into string and repalce -1 with a new line break and remove commas and brackets.
        compositeList = ''.join(str(compositeList)).replace('-1', '\n').replace(',', '').replace('[', '').replace(']','').strip()
        with path.open(mode='w', encoding='utf-8') as fileObject:
            fileObject.write(f'\n\t\tPrime Numbers\n\n{primeList}\n\n\t\tComposite\n\n{compositeList}')
            completed = f'[+] prime numbers and composite numbers have been created up to {maxCount}'
        return completed
    else:
        return f'[-] Could not locate {file}. Exiting...'

print(primeNumbers(100, 'PrimeNumberFile.txt'))

# ===============================================================
# Underscores in numbers are useful when writing long numbers to be more readable.
# ===============================================================
# Example:

universe = 13_700_000_000
print(universe) # = 13700000000

# ===============================================================
# You can use multiple assigments using a single line. This can be used When initalizing a set of numbers.
# But can also be used with strings
# ===============================================================
# Example:

x, y, z = 0, 0, 0
print(x, y, z)

x, y, z = 'hello', 'world', 'again'
print(x, y, z)

# ===============================================================
# You cannot pass an integer into a string value without converting to a string data type.
# You can use the int() function to convert to an integer from a string or use the str() function to convert to a string. 
# ===============================================================
# Example:

from datetime import date

import datetime
year = datetime.date.today().year

userDob = input('Please enter your date of birth:')
currentAge = str(int(year) - int(userDob))
futureYear = str(int(year + 10))
print(futureYear)
print('Your age is ' + str(currentAge) + '\nYou will be ' + str(int(futureYear) - int(userDob)) + ', 10 years from now in the year ' + str(futureYear))

# ===============================================================
# If you have a number with a decimal point you can use the float() function. 
# ===============================================================
# Example:

myNumber = 2021.4
print(float(myNumber))

# ===============================================================
# #The math.ceil(), math.floor() and round() functions
# When you divide number using the / operator, the expression returns a floating point number. This happens even if the number divides 
# evenly. For example, 21 / 7 will evaluate to 3.0, not 3. 
# round() will round to the nearest integer. 

# The below examples demonstrates that the arguments given 5.5 will return a rounded value of 6.
# The second argument 5.4 will return a rounded value of 5 as 5.4 is closer to 5 than it is 6.
# ===============================================================
# Example:

mathVar = round(5.6) # = 6
print(mathVar)

mathVar = round(5.5) # = 6
print(mathVar)

mathVar = round(5.4) # = 5
print(mathVar)

# ===============================================================
# The math.ceil() function will evaluate to the highest value. The below will go to 6. 
# If the argument was 5.4 it will still evaluate to 6 rather than 5 as the round() function would.
# ===============================================================
# Example:

import math

mathVar = math.ceil(5.4) # = 6
print(mathVar)

mathVar = math.ceil(5.5) # = 6
print(mathVar)

# ===============================================================
# The math.floor() function will evaluate to the lowest value. The below example will evaluate to 5
# If the argument was 5.6 it will still evaluate to 5 rather than 6 as the round() function would.
# ===============================================================
# Example:

mathVar = math.floor(5.7) # = 5
print(mathVar)

mathVar = math.floor(5.5) # = 5
print(mathVar)

# ===============================================================
# The pow() function allows you to raise a number to a power just as the mathematical ** power operator.
# ===============================================================
# Example:

print(pow(2, 5)) # = 32

# ===============================================================
# The absolute value of a number is just the number if it is positive. Where as the number if negative
# will be evaluate to a positive number. 
# ===============================================================
# Example:

print(abs(-10))

print(abs(10))

# ===============================================================
# 
# ===============================================================
# Example:


