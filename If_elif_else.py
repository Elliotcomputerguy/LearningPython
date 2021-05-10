#!/usr/bin/env python

# The conditional if, elif, else statements are boolean expressions that evalute to either True or False. 
# An if statement can be read as "if condition is True, execute the code in the following block. Otherwise if it is False, skip the block"
# An elif statement comes after the if statement and will check if the first condition did not evaluate to true. You can use as many
# elif statements. Each time it will evaluate if the condition is true if the condition evaluates to True it will execute the block of code. 
# else is the last statement known as the catch all statement and will execute if none of the if or elif statements evaluate to True. 
# ===============================================================
# Example:

numberOfCars = input('How many cars do you own:')
numberOfCars = int(numberOfCars)
if numberOfCars < 1:
    print('You dont have many cars.')
elif numberOfCars < 5:
    print('You have quite a collection.')
elif numberOfCars < 10:
    print('You got a lot of cars!.')
else:
    print('You earn to much money!')

# ===============================================================
# Boolean comparators are used to evaluate conditionals to either a boolean True or False value. 
# ===============================================================

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

# ===============================================================
# Just like the while and for loops, an if statements can be nested in side one another to create complex conditional executions.
# ===============================================================
# Example

if True:
    print('do something')
    if True:
        print('This is a nested if statement')
        if True:
            print('This is a nested if statement in a nested branch')
        elif True:
            print('This is a nested elif statement in a nested branch')
        else:
            print('This is a nested else statement in a nested branch')
    elif True:
        print('This is a nested elif statement')
    else:
        print('This is a nested else statement')
elif True:
    print('do something')
else:
    print('do something else')
    
# ===============================================================
