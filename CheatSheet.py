# Learning Python Cheat Sheet #

# Python is a intermediate byte code language rather than a compiled or interpreted language.

# #Python operators

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
#       \a                               Bell. Sounds the system bell
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

# #Len Function
# The Len() function accepts a string value argument and returns an integer value of how many characters are in the string. 
# The Len() function will start from 1 as indexing starts from 0 so you will have to either use slicing or -1 to not get a out of range
# when indexing a len() retun value

# #While statement
# A while statement tells python to check what the condition evalutes to. If the condition evaluates to True, the program execution enters 
# the block following the while statement from looking at the indentation. When it reaches the bottom of the block, the programs execution
# jumps back to the while statement and checks the condition again. If the condition is still True it jumps back into the block again. 
# 
# If the condition evaluates to False then the programs execution
# will skip the code in the block and will jump down to the next line outside of the block. 
#  
# A while statement is made of four parts:
# 1 The while keyword
# 2 An expression(also called a condition) that evaluates to the boolean values True or False
# 3 A colon
# 4 A block of indented code that comes after it. 

# 1: while keyword
#    |  2: A condition
#    |     |
# while i >=0: -- 3: colon
#   translated = translated + message[i]
#   i = i - 1 -- 4: A block of code

# #The Bollean Data Type
# The boolean data type has only two values True or False. These values are case sensitive. 

# #Comparison Operators
# The expression that follows the while keyword (the i >= 0 part) contains two values (the value in the variable i, and the integer value 0)
# connected by an operator (the >= sign, called the "greater than or equal" operator). The >= operator is called a comparison operator.
# The comparison operator is used to compare values and evaluate to a True or a False Boolean value. 


#=================================================================#
#         Operator Sign                  Operator Name            #
#=================================================================#
#              <                          Less than               #
#              >                          Greater than            #
#              <=                         Less than or equal to   #
#              >=                         Greater than or equal to#
#              ==                         Equal to                #
#              !=                         Not equal to            # 
#=================================================================#

# #Conditions
#
# A condition is another name for an expression when it is used in a while or if statement. Conditions usually have comparison operators,
# but conditions are still just expressions. 

# #Blocks
# A block is one or more lines of code group together with the same minimum amount of indentation. You can tell where a block begins and ends by
# looking at the line's indentation. 

# #Importing modules with import statement
# Some functions exist in seperate programs called modules. Modules are python programs that contain additional functions that can be used
# by your programs. The import statement is made up of the import keyword followed by the module name. 

# #Constants
# Constants are variables whose value does not change. This is a standard accepted convention to put any comstants into upper case.

# #The upper() and lower() string methods
# Methods are just like functions, except they are attached to a non-module value with a period.
# Examples of a string method is upper() and lower().
# 
# A function is not a method just because it is in a module. It can some times get confusing. Example; pyperclip.copy() is not a method but
# indeed a module. It is a function that is inside the pyperclip module. Most data types like strings have methods. Upper() and lower() 
# will evaluate to an upper or lower case version of that string.

# var = 'Hello world'.upper()
# print(var)
# var = var.lower()
# print(var)
# print(var.upper())
# print(var)

# #For loop statement 
# The for loop statement is very good at looping over a string or list of values. This is different to the while statement. which loops
# as long as a certain condition is True. A for statement has 6 parts.  


# 1. The keyword for
#   | 
#   |    |----------2. The variable name 
#   |    |    |----------------------3. The keyword in
# for symbol in message: -----------------------------5. Colon
#   some_code_here -|---------------------6. A block of code
#                   |
#                  4. A string or variable containing a string


# The for loop is very similar to the while loop, but when you only need to iterate over characters in a string. 
# using the for loop is much less code to type. You can make a while loop act as a for loop but with much more code.  

# for letter in 'Elliot':
#    print('The letter is :', letter)

# #The if statement
# An if statement can be read as "if condition is True, execute the code i the following block. Otherwise if it is False, skip the block"
 
# passwd = input('Enter pasword:')
# if passwd == 'My$3cr3tpass':
#     print('Access granted')
# if passwd != 'My$3cr3tpass':
#     print('Access denied')
# print('Done')

# #The else statement 
# An else statement can be used after an if statement's block, and its block of code will be executed if the if statement's condition is False.
# You can read the code as "if this condition is True, execute this block, or else execute this block"

# passwd = input('Enter your password:')
# if passwd == 'password':
#     print('Access granted')
# else:
#     print('Access denied')
# print('Done')

# #elif statement
# the elif statement like a if statement has a condition, like an else statement it follows an if (or another elif) statement and executes
# if the revious if (or elif) statement's condition is False. You can read a if,elif and else statement as "if this condition is true, run this block \n
# Or else, check if this next condition is True. Or else, run this last block." 

# numberOfCars = input('How many cars do you own:')
# numberOfCars = int(numberOfCars)
# if numberOfCars < 2:
#     print('You dont have many cars.')
# elif numberOfCars < 6:
#     print('You have quite a collection.')
# elif numberOfCars < 12:
#     print('You got a lot of cars!.')
# else:
#     print('You earn to much money!')

# #The in and not in Operators
# An expression of two strings connected by the in operator will evaluate to True if the first string is inside the second string
# Otherwise the expression evaluates to False. Notice that the in and the not in operators are case sensitive. 

# var = 'Hello world'
# if 'Hello' in var:
#    print('True')
# else:
#    print('False')

# #The find() string method
# Just like upper() lower() method can be called on sting values, the find() method is a string method. The find() method takes one
# string argument and returns the integer index of where that string appears in the method's string.
# 
# 'Hello'.find('e') = 1
# var = 'Hello'
# var.find('H') = 0 

# The range() function
# The range function takes one integer argument and returns a value of the range data type. These range values can be used in for loops to
# loop a specific number of times. 

# for i in range(5):
#     print('Elliot')

# for i in range(6):
#     print(i)

# You can also pass two integer arguments to the range() function. The first argument is where it should start from with the second
# argun=ment being where it should finish. 

# for i in range(3, 8):
#     print(i)

# #String formatting 
# also known as string interpolation. String formatting with the %s text is a way of placing one string inside another one.
# The first %s text in the string gets replaced by the first value in the parentheses after the % at the end of the string. 

# var1 = 'dog'
# var2 = 'cat'
# var3 = 'rat'
# print('the %s ate the %s that ate the %s.' % (var1, var2, var3))

# #The def statement means we are creating or defining a new function. We can call the function later in your program

# def myFunction():
#     print('This is my function')
#     total = 42 + 1
#     print('42 plus 1 is %s' % (total))
# print('start!')
# myFunction()

# #Parameters
# Parameters are variables that contain the arguments passed when a function is called. Parameters are automatically deleted when the function 
# returns. A parameter is a variable name in between the parentheses in the def statement. An argument is a value that is passed in between the parentheses
# for a function call.

# def func(param):
#     param = ''
# var = 'name'
# func(var)
# print(var)

# the variable var is being passed into the function. The variable var does not change to ''. The value of var is being assigned to the
# param variable inside the function. Any changes made to the param variable inside the function will not change the var variable.
# The argument value that is passed in a function call is copied to the parameter.  
# How ever there is an exception to this rule when passing lists or dictionary values. 

# #Variables in the global and local scope
# Every time a function is called, a local scope is created. Variables created during a function call exist in the local scope.
# Parameters always exist in a local scope. When a function returns, the local scope is destroyed and all variables are forgotten. 
# A variable in the local scope is still a sperate variable from a global scope variable even if the two variables have the same name.
# Variables created outside of every function exist in a global scope. When the program exits, the global scope is destroyed and all
# variables in the program are forgotten. 

# #Global Statement
# If you want a variable that is inside of a function to be a global variable you use the global statement with the variable name as the
# first line after the def statement. 

# Rules

# 1) Variables outside of all functions are always global variables.
# 2) If a variable in a function is never used in an assigment statement, it is a global variable.
# 3) If a variable in a function is not used in a global statement; but is used in an assigment statement, it is a local variable
# 4) If a variable in a function is used in a global statement, it is a global variable when used in that function.

# A list value can contain other values. Just like a string begin and end with quotes. 
# A list value begins with a [ open bracket and ends with a closing bracket ]. The value stored inside the list are typed within the brackets.
# If ther is more than one value in the list, the values are seperated by commas. 

# sneakers = ['Jordan', 'Nike', 'Yeazy', 'Adidas']
# print(sneakers)

# You can index and slice lists as you would strings. 

# print(sneakers[0])
# print(sneakers[:2])

# you can interate through a list with a for loop statement

# for sneaks in sneakers:
#     print('My favourite sneakers are', sneaks)

# Using the list() function to convert range objectsto lists
# if you need a list value that has increasing integer amounts, you could have code like the below to build a list. 

# myList = []
# for i in range(10):
#     myList = myList + [i]
# print(myList)

# How ever it is easier to directly make a list from a range argument that range() function returns by using list() function. 
# print('------------------------------')
# myList = list(range(10))
# print(myList)

# The list() can also convert strings into list value's. 
# def func():
#     myList = list('Elliot')
#     print(myList[0])
#     print(myList)

# func()

# #Reassigning the items in Lists. The items inside a list can be modified. You use the index to with a an assignemnt statement.
# print('--------------------------------')
# sneakers = ['jordan', 'nike', 'yeazy', 'addidas']
# sneakers[3] = 'Reebok'
# print(sneakers)

# #Reassigning characters in strings
# While you can reassign items in a list, you cannot assign a character in a string value. You have to use slicing instead

# var = 'Hello'
# var = var[:0] + 'G' + var[1:]
# print(var)

# print('--------------------------')
# var = 'string'
# var = var[:4] + 'x' + var[5:]

# Slicing is a simple way to get a substring from a larger string.

# #lists of lists
# list values can also contain other list values. 
# print('----------------------------------------')
# def func3():
#     listInList = [['dog', 'cat'], [1, 2, 3]]
#     print(listInList[0]) #= value dog,cat
#     print(listInList[0] [0]) # = value dog
#     print(listInList[1]) # = value 1,2,3
#     print(listInList[1][2]) # = value 3
# func3()

# You can also use the len() function to tell how many values are in the list

# sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
# print(len(sneakers)) 

# You can also use the in or not in operator 

# for i in sneakers:
#     print(i.title()) # .title is another method i learned (:

# if 'rebok' not in sneakers:
#     print('True')
# else:
#     print('False')

# List Concatenation and Replication with the + an * Operator
# Just like how + and * operators can concatenate and replicate strings, the same operators can concatenate and replicate lists. 

# var = ['hello'.title()]
# var2 = ['world'.title()]
# var = var + var2
# var = var * 5
# print(var)

# #Augmented Assignemnt Operators

# =====================================================================
#           Augmented Assigment                Equivalent Normal
#                                                 Assignment
# =====================================================================
#
#             var += 42                         var = var + 42
#             var -= 42                         var = var - 42
#             var *= 42                         var = var * 42
#             var /= 42                         var = var / 42
#
# =====================================================================

# Augmented assigment operators are shortcuts from the below.

# var = 10
# var = var + 42
# var = 'Hello'
# var =+ ' World!'

# #The special __name__ variable
# When a python program is run, there is a special variable with the name __name__ that is assigned the string value '__main__'
# before the first line of the program is run.

# This is how the program can know if it is being run as a program or imported by a different program as a module.
# When a python program is imported, the __name__ variable is set to the filename part before .py and then runs the program. 

# #Compound Conditions

# if, else, elif, and, or are known as simple conditions. You can combine simple conditions together with logical operators.
# And, Or, Not. Combined, these simple conditions become compound conditions. 

# while username:
#   username = input()    
#   password = ''
# if username == 'string' and password == 'string':
#   some_code
# elif username == 'string' or password == 'string':
#   some_code
#
# #and, or, not 
# Are logical operators. When combined with simple conditions they become compound conditions.
# 
# #The math.ceil(), math.floor() and round() function
# When you divide number using the / operator, the expression returns a floating point number. This happens even if the number divides 
# evenly. For example, 21 / 7 will evaluate to 3.0, not 3. 
# round() will round to the nearest integer 
# round(5.5) will = 6
# round(5.4) will = 5
# math.ceil(5.5) will = 6 as it will round to the highest integer
# math.floor(5.5) will = 5 as it will round to the lowest integer
#  some new line
#  another new line
# another new line
# #Python Identity Operators
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y
