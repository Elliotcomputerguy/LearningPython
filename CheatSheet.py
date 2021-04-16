# Learning Python Cheat Sheet #

# Python is a intermediate byte code language rather than a compiled or interpreted language.

# #Python operators

# ===========================#
# Operator         Operation #
# ===========================#
#     +            Addition  #
#     -           Subtraction#
#     *        Multiplication#
#     /            Division  #
# ===========================#

#Operators tell the computer to perform an operation on the numbers surrounding them.   

# #Integers and Floating points
#Whole numbers like 4, 0, 99 are called integers. Numbers with fractions or decimal points (3.5 or 42.1) are floating point numbers.
#5 = Integer
#5.5 = Floating point

# #Expressions
#2+2 is an expression. Expressions are made up of values (the numbers) connected by operators. 
#     =============================
#     |   2         +         2   |
#     | Value    Operator    Value|
#     =============================
#                  ||
#              Expression

# #Order of Operations
# multiplication * has a higher priority over addition +. If an expression has both * and + operators, the * is evaluated first.
# 2 + 4 * 3 + 1 = 15 4*3=12+2+1=15 You can use parenthesis to change which operation should happen first.
# (2 + 4) * (3 + 1) = 24 
# 
# #Evaluating Expressions
# When a computer solves the expression 10 + 5 and gets the value 15, we say it ha evaluated the expression. 
# An expression will always evaluate (that is, shorten down to) a single value.
# 
# #Data Types 
# Every value has a data type. Integer, floating points are known as data types. Every value has a data type.
# 
# #Variables
# Varibles are containers that hold a value. 
#
# #Storing values inside Variables with Assigment Statements
# The instruction with an = assigment operator called an assigment statement creates a variable and stores the value in it. 
# Unlike expressions, statements are intructions that do not evaluate to any value, they just perform some action.
# Key to understanding the difference between a statement and an expression is that if a Python instruction evaluates to a single value
# it is a expression. If a Python instruction does not, then it is a statement.
#  
#    ===============================================
#    |   spam               =             10 + 5   |
#    | Variable   Assigment operator    Expression |
#    ===============================================
#                           ||
#                  Assigment statement
#
#  Variable store single values, not expressions. The above statement spam = 10 + 5, the expression 10 + 5 will first be evaluated
#  to 15 and the value 15 would be stored in the variable spam. 
# 
# #Overwriting Variables  
# You can change the value stored in a variable by entering another assigment statement.
#
# spam = 15
# spam + 5
# spam = spam + 5

# #Variable Names 
# The computer does not care what you name your variables, but you should. They are case sensitive. spam Spam SPAM sPAM are 
# considered 4 different variables. Naming your variables you should name them matching the values they contain to make it 
# easier for others to read. 
#
# #Camel Case
# Although optional it is a programming standard way of doing things. myVariableName is easier to read than myvariablename. 
# 
# #Strings
# 
# strings are text values. You can store string values inside variables like integer and floating point values. 
# strings are put in two single quotes (') to show where the string starts and ends.
# spam = 'Hello'

# #String Concatenation with the + Operator
# String concatenation can be achieved with the + operator. You can add together two string values
# by using the + operator. 

# #String Replication with the * Operator
# You can also use the * operator on a string and an integer data type to do string replication. 
# 'Hello' * 3
#Result = HelloHelloHello

# #Printing values with Print() Function
# There is anther python instruction called a print() function call. It performs a task to print values to the screen.
# There are many different functions that come with Python. To call a function means to execute the code that is inside
# the function ().
# A value that is passed into the function call are called arguments. Arguments are the same as values but are only called 
# arguments when they are passed to function calls. You can also pass an expression to the print() function call instead of a
# single value. This is becasue the value that is actually passed to the print() function is the evaluated value of that expression.
#
# var = 'Elliot'
# print('Hello, ' + var)
# 


