

# Object-oriented programming basic building blocks consist of objects. Classes define the data structure which identify
# behaviours that an object can perform with its defined data. They are the blue prints that design the object. 
# OOP allows you to represent real life objects as software objects. Software objects combine attributes and methods. 
# An attribute could be referenced as a name or an age; where a method would describe a behaviour. 
# If an aircraft is our object. The aircrafts name would be an attribute, where a method would be how it can fly and move. 
# When you build an object it is instantiated from a class. You can instantiate as many objects also called instances from a class. 
# The objects do not all have to have the same attributes from the same class. Taking our aircraft object. 
# You could instantiate one with a different name to another aircraft object. 

# When building an object, a class is the first thing you build. Just as you would a house. You would have
# schematics representing the attributes and methods of the house before it can become an object.

# Defining the class starts of with the definition of the class header. Using the keyword class followed by the class name and a colon. 
# All classes are written in captials. You can use the keyword pass as a placeholder to stop errors and represent where code will go. 
# Classes are written in capatilized word notation. It is the standard convention but not a rule in Python. 
# ===============================================================
# Example:

class VirtualPet:
    ''' Virtual Pet ''' #<-- DocString 
    pass

# ===============================================================
# The first thing you do inside of a class is define a constructor method also called a initialization method. 
# The constructor method is automatically called when an object from the class is instantiated. The constructor method 
# definines the attributes of the object. The built-in __init__() is a specific method name understood by Python. 
# Python has a collection of built-in special methods that begin with two underscores and end with two underscores. 

# You can give the __init__() any number of parameters, but the first parameter will always be called self. When a new class
# object is created, the object is automatically passed to the self parameter in __init__() so the new attributes can be defined on an
# object. The constructor method initalizes an object attribute called name and links the value to the name parameter. 
# ===============================================================
# Example:

class VirtualPet:
    ''' Virtual Pet ''' #<-- DocString 

    def __init__(self, name):
        self.name = name

# ===============================================================
# Attributes created in a __init__() method are called instance attributes. An instance attribute's value is specific to a particular
# instance of the class. Each instantiated object from the class VirtualPet does not have to have the same name. 
# Below we have instantiated an object from the class VirtualPet and passing an argument to the name attribute. 
# ===============================================================
# Example:

print('''

    (\ (\\
    ( -.-)     
    O_('')('') 

''')
pet = VirtualPet('Jack the Hungry Rabbit')
print(f'Hi my name is {pet.name}\n')

# ===============================================================
# Object methods are exactly the same as functions but associated with an object defined within a class and only invoked
# from an object of that class. Just as with the constructor method all object methods must have the self parameter called self by convention
# The special self parameter allows the method to reference the object. If you create a method without any parameters it will error when
# called. 
# ===============================================================
# Example:

class VirtualPet:
    ''' Virtual Pet ''' #<-- DocString 

    def __init__(self, name):
        self.name = name

    def enunciate(self, voice): #<-- Object method
        return f'{voice}'

print('''

    (\ (\\
    ( -.-)     
    O_('')('') 

''')

pet = VirtualPet('Jack the Hungry Rabbit')
print(f'Hi my name is {pet.name}\n')
print(pet.enunciate('i am hungry and looking for some carrots! \n\nWill you help me find some carrots\n'))

# =======================================================



# Class attributes are attributes that have the same value for all class instances. 
# 







#You can define a class attribute by assigning 
# a value to a variable name outsode of __init__(). 

# Class attributes are defined directly beneath the first line of the class name. Class attributes are automatically created and assigne
# their initial values. 

# Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for 
# properties that vary from one to another. 

# Creating a new object from a class is called instantiating an object. You can instantiate a new object by typing the name of the 
# class followed by opening and closing parentheses.

# You need to provide arguments for the parameters in the __init__ method. A TypeError will be raised if not assigned. The first parameter
# 'self' is removed when a new instance is created. 



# After you create the instance from your class. You can access the instance attributes using dot notation.



# You can access the class attributes the same way. 



# Classes will always have the attributes you expect. There values can also be modified dynamically. Custom objects are mutable. 


# Instance methods are defined inside a class and can onlt be called from an instance of that class. Just like __init__(),
# An instance method is always self.
