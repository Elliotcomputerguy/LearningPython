#!/usr/bin/env python

# #While statement
# A while statement tells python to check what the condition evalutes to. If the condition evaluates to True, the program execution enters 
# the block following the while statement from looking at the indentation. When it reaches the bottom of the block, the programs execution
# jumps back to the while statement and checks the condition again. If the condition is still True it jumps back into the block again. 

# If the condition evaluates to False then the programs execution
# will skip the code in the block and will jump down to the next line outside of the block. 

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

#   while (condition) == True
#   it will Loop and run the block. 
#   if it is False it will not run the loop and skip the indented block
# ===============================================================
# Example:

i = 1
timestable = int(input('Enter your times table of choice:')) #<-- Only accept int input

while i <=10:
    print(timestable, 'x', i, '=', i * timestable )
    i += 1

# ===============================================================
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. 
# Iterating over a sequence is called traversal.
# The while loop in Python is used to iterate over a block of 
# code as long as the test expression (condition) is true.
# We generally use this loop when we don't know the number of times to iterate beforehand
# ===============================================================
# Example:

# The below demonstrates the usage. The for loop here would be used in a program as we are iterating over a string.
# The while loop is not desgined for this iterative task. A great example for a while loop is where you create a 
# menu and you do not know how many times a user will want to itterate through the menu selecting options.
  
i = 0
var = input('Enter a string value ie your name:')
while i < len(var):
    letter = var[i]
    print ('The letter is', letter)
    i += 1

for i in var:
    print(f'The letter is {letter}')

# ===============================================================
# Infinite loops
# ===============================================================
# Example:

counter = 0
while counter <= 10:
    print(counter)
    # without the below expression 'counter += 1' evaluating a value to increase the integer value of varible counter from 0 to 10 on each iteration 
    # it would be an infinite loop and would only print 0 indefinitily as there is no escape condition. 
    counter += 1

# ===============================================================
# #Intentional Infinite Loops with exit conditions
# The break statement will exit a loop and the continue statement will go back to the beginning of the while loop while the 
# condition is elevated to True. 
# Break and continue statements should be used sparingly. Using these statements make it harder to understand the flow of a loop.
# As best practice it is good to not use these statements. Any loop can be written with out them.  
# ===============================================================
# Example:

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

# ===============================================================
# Sentry variables
# Often, while loops are controlled by a sentry variable, a variable used in the condition and compared to some other value
# or values. You will need to initilize the sentry variable. 
# ===============================================================
# Example:

response = ''
guessCount = 1
while response != 'batman':
    response = input('Guess what my name is:')
    if guessCount == 5:
        print('HINT: nananananana batman!')
    guessCount += 1 # Here you could use continue statment instead of useing the guessCount variable
print('nananananana batman!')

# ===============================================================
# Checking the sentry variable is possible for the while loop to evaluate to True, otherwise the while statement will not run. 
# The below will never run as the variable response is equal to name.
# ===============================================================
# Example:

response = 'name'
while response != 'name':
    response = input('Enter a name:')

# ===============================================================
# This while loop will not exit until username is evaluated to True. Ie a value has been entered and assigned to the username variable.
# ===============================================================
# Example:

print('--------------------------------')
username = ''
while not username:
    username = input('Enter your username:')

password = ''
while not password:
    password = input('Enter your password:')

# ===============================================================
# This while loop will not exit until start == ''
# ===============================================================
# Example:

start = None
while start != '':
    start = input('\nstart:')
    if start:
        print('some code')
    else:
        print('fin')

# ===============================================================
# This loop will not exit until the user enters nothing. Because word is True it enters the block. 
# The while will not exit unti the condition is false.
# ===============================================================
# Example:
  
word = 'anything'
while word:
	word = input('>')

# ===============================================================
# This loop does the exact same thing.
# ===============================================================
# Example:
 
word = None
while word != '':
	word = input('>')

# ===============================================================
