class Apple:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    


emp_1 = Apple('John', 'Cena')

emp_1.first = 'Ben'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


# without private properties, we are able to change the variables.


# While with private ones on the other hand, this is the result:
# The main difference is that we can change what's in the setter,
# but not what is in the __init__ file.

class Microsoft:
    def __init__(self, first, last):
        self._first = first
        self._last = last

    @property
    def email2(self):
        return f'{self._first}.{self._last}@email.com'
    
    @property
    def fullname2(self):
        return f'{self._first} {self._last}'
    
    @fullname2.setter
    def fullname2(self, name):
        first, last = name.split(' ')
        self._first = first
        self._last = last
    


emp_2 = Microsoft('Timmy', 'Turner')

emp_2.fullname2 = 'John Kramer'

print(emp_2._first)
print(emp_2.email2)
print(emp_2.fullname2)