

# Intoducing None

# Python uses the keyword None to define null objects and variables. While None does serve some of the same purposes as null in other languages, 
# it’s another beast entirely. As the null in Python, None is not defined to be 0 or any other value. In Python, None is an object.

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

x = None
if x:
  print("\n\nDo you think None is True?")
elif x is False:
  print ("\n\nDo you think None is False?")
else:
  print("\n\nNone is not True, or False, None is just None...")

# The inside print function returns a None.
print(print('hi'))

def func():
    pass
print(func())
