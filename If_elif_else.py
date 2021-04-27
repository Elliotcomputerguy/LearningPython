#!/usr/bin/env python

# The conditional if, elif, else statements are boolean expressions that evalute to either True or False. 
# An if statement can be read as "if condition is True, execute the code in the following block. Otherwise if it is False, skip the block"
# An elif statement comes after the if statement and will check if the first condition did not evaluate to true. You can use as many
# elif statements. Each time it will evaluate if it is true if it is then it will execute the block of code. 
# else is the last statement known as the catch all statement and will execute if none of the if or elif statements evaluate to True. 
# ===============================================================
# Example:

numberOfCars = input('How many cars do you own:')
numberOfCars = int(numberOfCars)
if numberOfCars < 2:
    print('You dont have many cars.')
elif numberOfCars < 6:
    print('You have quite a collection.')
elif numberOfCars < 12:
    print('You got a lot of cars!.')
else:
    print('You earn to much money!')

# ===============================================================
# Comparison operators are used to evaluate conditions to either a boolean True or False value. 
# They are used in if,elif and while conditionals.  

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

# Interpreting any value as True or False not using a comparison operator but the value itself is being treated as the condition.  
# When it comes to evaluating a number as a condition. 0 is False and everything else is True.
# There are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
# the number 0, and the value None. And of course the value False evaluates to False.
# ===============================================================
# Example:

condition = input('\nEnter a value to mark condition as True or hit enter to skip to mark as False:')
if condition:
    print('True: #%s' % (condition))
else: 
    print(f'False: {condition}')

# ===============================================================