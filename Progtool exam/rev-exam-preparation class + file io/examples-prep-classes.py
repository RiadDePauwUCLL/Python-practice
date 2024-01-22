class Animal:
    def __init__(self, name, list_likes, age):
        self.name = name
        self.list_likes = list_likes
        self.age = age

@property  #property is a getter, it gets the value of the name.
def name(self):
    return self._name
# gets the name, it is a private value. It gives the name.

@name.setter
def name(self, value):
    if not isinstance(value, str):
        raise TypeError('name must be a string')
    self._name = value
# update the value of name, it is a private value. It sets the name.
# It ensures that the name is a string, otherwise it will raise an error.

@property
def list_likes(self):
    return self._list_likes

@list_likes.setter
def list_likes(self, value):
    if not isinstance(value, list):
        raise ValueError('list_likes must be a list')
    for item in value:
        if item not in ('vegetables', 'meat', 'fruit', 'other'):
            raise ValueError('list_likes must contain only be vegetables, meat, fruit or other')
    
    self._list_likes = value

def add_likes(self, item):
    if item in ('vegetables', 'meat', 'fruit', 'other'):
        if item not in self.list_likes:
            self.list_likes.append(item)
        else:
            raise ValueError('item already in list_likes')
    else:
        raise ValueError('item must be vegetables, meat, fruit or other')
    
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    if not isinstance(value, int) or value < 0:
        raise TypeError('age cannot be negative')
    self._age = value


# In regards to the getter and setter, the name is a private value, it is not accessible from outside the class.
# Below you will find more information about the getter:
    
# In Python, the underscore prefix _ before a variable name is a convention that indicates 
# the variable is intended for internal use within the class, module, or function it's defined in. 
    
# It's a hint to the programmer that the variable or method should not be accessed directly outside of its defined context.

# However, it's important to note that this is just a convention and Python does not enforce it strictly. 
# You can still access these variables directly, but it's generally considered bad practice.
    
# In the context of your code, self._name is a private instance variable of a class. 
# The method name(self) is a getter method used to access the value of self._name from outside the class. 
# This is a way to encapsulate (hide) the internal state of an object and control how it's accessed and modified.