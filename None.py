

# Intoducing None

# None is python's way of presenting nothing? But i cannot get it to evaluate to False ? Explanation....

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

x = None
if x:
  print("\n\nDo you think None is True?")
elif x is False:
  print ("\n\nDo you think None is False?")
else:
  print("\n\nNone is not True, or False, None is just None...")
