import random

# Generating Random Numbers
# Python generates random numbers based on a formula, so they are not truely random. 
# The random generation is called pseudorandom. You have to import the random module in order to use it in your program.

# random.seed()

# The pseudorandom number generator starts with an initial number called a seed. All of the numbers numbers produced from a seed are 
# predictable. Our Python programs only seem to generate unpredictable random numbers becasue the seed is set to the computers current
# clock time (specifically, set to the number of seconds since jan 1st, 1970) when the random module is imported.
# Do not count on this to provide true random numbers. 

# random.seed(42) 
for i in range(5):
    print(random.randint(1, 100,),end='') # See what i did to get the value in a straight line. Rather than down the screen.
print('')

# Random.randint() function
# The random module contains a function called randint(), which produces a random integer. The program does not directly call the randint()
# function but accesses it via the random module. This access is known as dot notation. The randint() function requires to integer arguments
# and returns a random integer between those two values. 

var = random.randint(1, 10)
print(var)
# randrange() function
# The randrange() function. There are multiple ways to call randrange() but the easiest method is to use a single, positive, integer
# argument. The return value will be anything from 0 - 9 using the below example. If i + 1 it will be 0 - 10.
var = random.randrange(10) + 1
print(var)

