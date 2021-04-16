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
# #Escape characters
# Sometimes we migth want to use a character that cannot be easily typed into a string value. We might want to use a single qute character 
# as part of a string. This is where escape characters come in.

# ========================================================================
# Escape Character                      What is printed
# ========================================================================
#       \\                               Backslash (\)
#       \'                               Single quote (')
#       \"                               Double quote (")
#       \n                                  NewLine
#       \t                                    Tab
# ========================================================================

# print('He flew away in a green\\teal helicopter.')

# #Quotes and Double Quotes
# Strings dont always have to be in between two single quotes they can be double quotes instead. 
# 
# Print("Hello World")
# But you cannot mix them. 
# Print('Hello world") Will lead to a syntax error
# You do not need to escape double quotes inside single quote strings as you dont need to escape from single quotes inside double quote strings.
# 
# #Indexing
# Indexing is the adding of a square bracket to the end of a string value or a variable containing a string with a number 
# between them. This number is called the index, and tells python which postion in the string has the character you want. 
# The index of the first character in a string is 0. The index 1 is the second character, etc. 
#  
# var = 'Hello'
# var[0] 
# output = H
# Notice that the expression var[0] evaluates to the string value 'H', since the H is the first character in the string.

# var = 'Elliot'[3]
# The expression Elliot[3] will evaluate to the string datatype character 'i' and the assigment operator will assign it to the variable called var
# known as an assignment statement.

# If you enter an index that is too large for the string, python will display an "index out of range" error message. 

# #Negative Indexes
# Negative indexes start at the end of a string and go backwards. The negative index -1 is the index of the last character in a string. 
# The index -2 is the index of the second from last character, and so on. 

# var = 'Elliot'
# print(var[-1],var[-2],var[-3],var[-4],var[-5], var[-6])
#
 
# #Slicing 
# If you want to get more than once character from a string, you can use slicing of indexing.
# A slice also uses the [ and ] square brackets but has two integer indexes instead of one.
# The two indexes are seperated by a colon : 

# var = 'Elliot'[0:3]
# print(var)
# var = 'Hello World'[0:5]
# print(var)
# var = 'Hello World'[-11:-6]
# print(var)
# var = 'Hello world'[0]
# print(var)
# var = 'Hello world'[-0]
# print(var)

# Notice how 0 and -0 are the same. Remember that -1 is the last character in negative indexes
# Unlike indexes, slicing will never give you an error if you give it too large of an index for the string.

# var = 'Hello world'[0:999]
# var = 'Hello world'[2:999]
# var = 'Hello world'[1000:2000]

# #Blank Slice Indexes
# If you leave out the first index of a slice, python will automatically think you want to specify index 0 for the first index. 
# The expression 'Hello'[0:3] and 'Hello'[:3] evaluate to the same string.

# var = 'Hello world'[:3]
# print(var)

# If you leave out the second index, python will automatically think you want to specify the rest of the string. 
# 'Hello'[2:] evaluates to the value 'llo world'

# var ='Hello world'[2:]
# print(var)

# Slicing is a simple way to get a substring from a larger string. 

# #Functions
# A function is kind of a mini program inside your program. It contains lines of code that are executed from top to bottom.
# Python provides some built-in functions that we can use. We have already used the print() function.

# A function call is a piece of code that tells your program to run the code inside a function. Your program can call the print() function
# when ever you want to display a string on the screen. The print () function takes the value you type inbetween the parenthesis as input and
# diplays the text on the screen. You add parenthesis to the end of function names to make it clear that we're referring to a function,
# not a variable. 
# 

# #The Input Function
# When the input() function is called it will wait for for user input to type some text and press Enter. 
# The text string that the user types in becomes the string value or integer value that is stored. If we create am assignment statement. 

# var = input()

# Like expressions, function calls evaluate to a single value. The value that the function call evaluates to is called the return value.
# In the above expample, the return value of the input() functon is the string or integer value that is assigned to the varibale var.
# The function input() does not need any arguments unlike the print() function which is why there is nothing between the parentheses 

# myName = input()
# print('Hello, ' + myName)
#  