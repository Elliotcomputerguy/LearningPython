#!/usr/bin/env python

# and, or, not are logical operators that are used to combine Boolean expressions. 
# When combined with simple conditions such as a Boolean comparators they become compound conditions.
# ===============================================================

# ===
# and
# ===

# ===============================================================
# The logical operator 'and' evaluates two Boolean expressions in which both simple conditionals either side of 
# the logical operator have to be True for the compound condition to evaluate to True. Any other evaluation will result as False. 
# ===============================================================
# Example

100 < 5 and 11 < 50 # = False

# ===============================================================
# The following evaluated compound condition evaluates to False because the first simple conditonal evaluates to False. 
# A 100 is not less than 5 and evaluates to False. 11 is less than 50 and evaluates to True. 
# The 'and' logical operator uses the below rules when evalauting simple conditions.
# ===============================================================

# ===============================================================
#                        and Operator Rules
# ===============================================================
#     True and True                                  True
#     True and False                                 False
#     False and True                                 False
#     False and False                                False
# ===============================================================

# ===
# or
# ===

# Saying the phrase it can be either be True or False is the same logic applied in the 'or' operator. If one of the simple conditions 
# on either side of the 'or' logical operator evaluates to True the compound condition evaluates to True. 
# If both simple conditions evalaute to False the compund condition evaluates to False. 
# ===============================================================
# Example

1 > 2 or 1 < 2 # = True 

# ===============================================================
# the first simple condition evalautes to False as 1 is not greater than 2. While the second conditional evalutes to True as 1 is less
# than 2. Therefore this compound condition evaluates to True as one of the simple conditions evaluates to True.
# ===============================================================

# ===============================================================
#                        or Operator rules
# ===============================================================
#     True or True                                   True
#     True or False                                  True
#     False or True                                  True
#     False or False                                 False
# ===============================================================

# ===
# not
# ===

# ===============================================================
# The not logical operator reverses True from False. If something is not True then it is False. If something is not False then it is True.
# There is an order of operator precedence. When you attempt to evaluate False == not True you will receive an error 
# as the == operator precedes the logical not operator and attempts to evaluate the == operator first. 
# You have to use parentheses to tell python to evaluate which conditions first in the compound condition.
# ===============================================================

# ===============================================================
#                        not Operator rules
# ===============================================================
#     not True                                       False
#     not False                                      True
# ===============================================================

# ===============================================================
# Example

not True == False # = True: False is equal to False so therfore is True.

False == (not True) # = True: False is equal to False so therfore the evaluation is evaluated as True.

# ===============================================================

# ===============================================================
#                  Operator Order of Precedence
# ===============================================================
#                       <, <=, == , =>, >
#                              not
#                              and
#                              or     
# ===============================================================

# ===============================================================
# Example

not (5 > 6) == (not True) or (5 == 2) and (7 <= 8) # This complex compound condition evaluates to False. 

# ===============================================================
# Breaking it down.
# not (5 > 6) = not True. 5 is not greater than 6 so therfore it is not True. So is evaluated as False. not False.
# not False == not True evaluates to False. 
# (5 == 2) is not True so this is False. 
# (7 <= 8) is True as 7 is less than 8. 
# The or logical operator evaluates its compound conditional as False as both conditions either side of 'or' evaluate to False. 
# The and operator evaluates its compound conditonal as False because the conditions on both side are not True so therfore is 
# evaluated as False
# ===============================================================
# Example 

True and not (5 == 3) # = True

# ===============================================================
# Breaking it down. 
# 5 does not eqaual to 3 so there for it is not True and evaluates to False.  
# True and not False evaluates to True. As not False evaluates to True. As both conditions are True the 'and' logical operator 
# evaluates the compound condition as True.
# ===============================================================
# Example

('b' != 'b') or not (5 >= 6) # = True           

# ===============================================================
# Breaking it down.
# b is equal to b so evalutes to False. 
# 5 is not greater than 6 so is also evaluated to False. 
# False or not False evalutes to True as not False evaluates to True and the 'or' logical operator has a rule that either one condition 
# to be True or False to evaluate as True.

