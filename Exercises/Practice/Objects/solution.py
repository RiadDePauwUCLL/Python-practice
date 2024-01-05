import random

# Classic Hello World
# You are given a method called main, make it print the line Hello World!, 
# (yes, that includes a new line character at the end) and don't return anything

# Note that for some languages, the function main is the entry point of the program.

# Here's how it will be tested:

#     Solution.main("parameter1", "parameter2","parametern")
# Hints:

# Check your references
# Think about the scope of your method
# For prolog you can use write but there are better ways
# If you still don't get it probably you can define main as an attribute 
# of the Solution class that accepts a single argument, 
# and that only prints "Hello World!" without any return.
# Write ur code here:

class Solution:
    def main(self):
        print('Hello World!')


# It's a pretty basic object. Nothing special.
        






# Color Ghost
# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

# ghost = Ghost()
# ghost.color  => "white" or "yellow" or "purple" or "red"
# Write ur code here:

class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)


# Here it's plain simple, __init__ does the trick.
        






# Name your Python!
# For those of us who are not very familiar with Python, 
# let's handle the very basic challenge of creating a class named Python. 
# We want to give our Pythons a name, 
# so it should take a name argument that we can retrieve later.

# For example:

# bubba = Python('Bubba')
# bubba.name # should return 'Bubba'
# Write ur code here:
        
def Python():
    def __init__(self, name):
        self.name = name







# Basic subclasses - Adam & Eve
# According to the creation myths of the Abrahamic religions, 
# Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. 
# The creation method must return an array of length 2 containing objects 
# (representing Adam and Eve). 
# The first object in the array should be an instance of the class Man. 
        
# The second should be an instance of the class Woman. 
# Both objects have to be subclasses of Human. 
# Your job is to implement the Human, Man and Woman classes.
# Write ur code here:
        
def God():
    return [(Man), (Woman)]

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass










#Make them bark

# You have been hired by a dogbreeder to write a program to keep record of his dogs.

# You've already made a constructor Dog, so no one has to hardcode every puppy.

# The work seems to be done. It's high time to collect the payment.

# ..hold on! The dogbreeder says he wont pay you, until he can make every dog object .bark(). 
# Even the ones already done with your constructor. "Every dog barks" he says. 
# e also refuses to rewrite them, lazy as he is.

# You can't even count how much objects that bastard client of yours already made. 
# He has a lot of dogs, and none of them can .bark().

# Can you solve this problem, or will you let this client outsmart you for good?

# Practical info:
# The .bark() method of a dog should return the string 'Woof!'.

# The contructor you made (it is preloaded) looks like this:

# class Dog(object):
#     def __init__(self, name, breed, sex, age):
#         self.name  = name
#         self.breed = breed
#         self.sex   = sex
#         self.age   = age
# Hint: A friend of yours just told you about how javascript 
# handles classes differently from other programming languages. 
# He couldn't stop ranting about "prototypes", or something like that. 
# Maybe that could help you...
# Write ur code here:

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age

    def bark(self):
        return 'Woof!'
    
    # Dog.bark = bark
    # WTF????????????????????
    
    #The line Dog.bark = bark in this "code" is unnecessary and doesn't make sense in this context.

    # In Python, when you define a method within a class, like bark in your Dog class, 
    # it's automatically associated with instances of that class. 
    # You don't need to manually assign the method to the class outside of the class definition.
    # terrible design for an exercise lol