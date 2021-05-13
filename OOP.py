
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

class PetRabbit:
    ''' Virtual Pet Rabbit''' #<-- DocString 
    pass

# ===============================================================
# The first thing you would usually do inside of a class is define a constructor method also called a initialization method. 
# The constructor method is automatically called when an object from the class is instantiated. The constructor method 
# definines the attributes of the object. The built-in __init__() is a specific method name understood by Python. 
# Python has a collection of built-in special methods that begin with two underscores and end with two underscores. 

# You can give the __init__() any number of parameters, but the first parameter will always be called self. When a new class
# object is created, the object is automatically passed to the self parameter in __init__() so the new attributes can be defined on an
# object. The constructor method initalizes an object attribute called name and links the value to the name parameter. 
# ===============================================================
# Example:

class PetRabbit:
    ''' Virtual Pet Rabbit ''' #<-- DocString 

    def __init__(self, name):
        self.name = name

# ===============================================================
# Attributes created in a __init__() method are called instance attributes. An instance attribute's value is specific to a particular
# instance of the class. Each instantiated object from a class does not have to have the same values. 
# Below we have instantiated an object from the class PetRabbit and passing an argument to the name attribute. 
# ===============================================================
# Example:

print('''

    (\ (\\
    ( -.-)     
    O_('')('') 

''')
rabbit = PetRabbit('Danny the Hungry Rabbit')
print(f'Hi my name is {rabbit.name}\n')

# ===============================================================
# Object methods are exactly the same as functions but associated with an object defined within a class and only invoked
# from an object of that class. Just as with the constructor method all object methods must have the self parameter called self by convention
# The special self parameter allows the method to reference the object. If you create a method without any parameters it will error when
# called.
# ===============================================================
# Example:

class PetRabbit:
    ''' Virtual Pet Rabbit''' #<-- DocString 

    def __init__(self, name): #<-- Constructor method
        self.name = name

    def enunciate(self, voice): #<-- Object method
        return f'{voice}'

print('''

    (\ (\\
    ( -.-)     
    O_('')('') 

''')

rabbit = PetRabbit('Danny the Hungry Rabbit') #<-- Instantiating an object from the class PetRabbit
print(f'Hi my name is {rabbit.name}\n') #<-- calling the attribute on the constructor method to initialize the name parameter.
print(rabbit.enunciate('I am hungry and looking for some carrots! \n\nWill you help me find some carrots\n')) #<-- Invoking method enunciate

# =======================================================
# When you print the object print(rabbit) you receive a memory location. <__main__.PetRabbit object at 0x000001A1CF0A4FD0>
# It does not return any useful information on the object. 
# Using the special method __str__() in a class definition to make a string representation for the object that will be displayed
# when invoked. It is considered good practice to create a __str__() method to help see an objects attributes.
# ===============================================================
# Example:

class PetRabbit:
    ''' Virtual Pet Rabbit''' #<-- DocString 

    def __init__(self, name): #<-- Constructor method
        self.name = name

    def enunciate(self, voice): #<-- Object method
        return f'{voice}'

    def __str__(self):          #<-- String method to return name attribute 
        classObject = 'PetRabbit Object\n'
        classObject += f'Name: {self.name}'
        return classObject


rabbit = PetRabbit('Danny the Hungry Rabbit') #<-- Instantiating an object from the class PetRabbit
print(rabbit) #<-- making a call to the __str__() method

# ===============================================================
# Class attributes are attributes that have the same value for all class instances. So if we wanted any class object created to only be 
# alive for 30 days we would create that as a class attribute.  
# ===============================================================
# Example:

class PetRabbit:
    ''' Virtual Pet Rabbit''' #<-- DocString 

    classObjectLife = 0 #<-- Class attribute

    def __init__(self, name): #<-- Constructor method
        self.name = name
        # when object is instantiated get date and time and write it to a json file
        # once 30 days have been reached the pet rabbit goes to bunny heaven 

    def enunciate(self, voice): #<-- Object method
        return f'{voice}'

    def __str__(self):          #<-- String method to return name attribute 
        classObject = 'PetRabbit Object\n'
        classObject += f'Name: {self.name}'
        return classObject


rabbit = PetRabbit('Jack the Hungry Rabbit') #<-- Instantiating an object from the class PetRabbit
print(rabbit.classObjectLife)

# ===============================================================
# Example:


