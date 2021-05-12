
# Boolean comparators are used to compare two values. True and False. Boolean became known as the term Boolean coined by 
# the mathematician George Boole. Conditonals are sometimes expressed as Boolean expressions and conditional logic refered 
# to as Boolian logic. Boolean can only evaluate a conditonal to two Boolean values. Either True or False. 
# True and False both start with a capital letters. 
# ===============================================================

###################################################
# Operator	       Name	               Example    #
################################################### 
#  ==	           Equal	            x == y	  #
#  !=	         Not equal	            x != y	  #
#  >	        Greater than	        x > y	  #
#  <	         Less than	            x < y	  #
#  >=	    Greater than or equal to	x >= y	  #
#  <=	    Less than or equal to	    x <= y    #
#                                                 #
###################################################

# ===============================================================
# Conditional expressions evaluate not only integers but also strings. 
# ===============================================================
# Example

'string' == 'string' # = True
'string1' == 'string2' # = False
'a' > 'b' # = False 
'b' > 'a' # = True
'Space' > 'Mars' # = True
'Boolean' > 'Basketball' # = True
True > False # = True
True < False # = False

# ===============================================================
# Strings are ordered lexicographically. A comes before b and c after b. Therefore a is not greater than b. But is less than b. 
# Every character has a unicode code point which python uses to compare characters with. 
# ===============================================================