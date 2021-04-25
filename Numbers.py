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
#2+4 is an expression. Expressions are made up of values (the numbers) connected by operators. 
#     =============================
#     |   2         +         4   |
#     | Value    Operator    Value|
#     =============================
#                  ||
#              Expression
# ===============================================================
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
# #Integers and Floating points
#Whole numbers like 4, 0, 99 are called integers. Numbers with fractions or decimal points (3.5 or 42.1) are floating point numbers.
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
# Underscores in numbers are useful when writing long numbers to be more readable.
# ===============================================================
# Example:

universe = 13_700_000_000
print(universe) # = 13700000000

# ===============================================================
# You can use multiple assigment using a single line. This can be used When initalizing a set of numbers.
# But can also be used with any value. 
# ===============================================================
# Example:

x, y, z = 0, 0, 0
print(x, y, z)

x, y, z = 'hello', 'world', 'again'
print(x, y, z)

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
