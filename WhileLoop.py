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
timestable = input()
timestable = int(timestable)
while i <=10:
    print('10 x', i, '=', i * timestable )
    i = i + 1
