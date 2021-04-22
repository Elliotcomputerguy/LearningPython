#!/usr/bin/python

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

# My times table program. I convert input() into integer to allow the end user to choose what times table to do.

i = 1
timestable = input('Enter your times table of choice:')
timestable = int(timestable)
while i <=10:
    print(timestable, 'x', i, '=', i * timestable )
    i += 1

# A for loop statement would work much better here as it is designed to iterate through strings and lists.
print('--------------------------------------')
i = 0
var = input('Enter a string value ie your name:')
while i < len(var):
    letter = var[i]
    print ('The letter is', letter)
    i += 1

# Infinite loops

counter = 0
while counter <= 10:
    print(counter)
    # without the below expression evaluating a value to increase the integer value of varible counter from 0 to 10 on each iteration 
    # it would be an infinite loop and would only print 0 indefinitily as there is no escape condition. 
    counter += 1

# Intentional Infinite Loops with exit conditions
# The break statement will exit a loop and the continue statement will go back to the beginning of the while loop while the 
# condition is elevated to True. 
# Break and continue statements should be used sparingly. Using these statements make it harder to understand the flow of a loop.
# As best practice it is good to not use these statements. Any loop can be wrote with out them.  

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

# Sentry variables
# Often, while loops are controlled by a sentry variable, a variable used in the condition and compared to some other value
# or values. You will need to initilize the sentry variable. 

# The below will never run as the variable response is equal to because. 
response = 'because'
while response != 'because':
    response = input('why')


# This while loop will not exit until username is evaluated to True. Ie a value has been entered and assigned to the username variable.
print('--------------------------------')
username = ''
while not username:
    username = input('Enter your username:')

password = ''
while not password:
    password = input('Enter your password:')
