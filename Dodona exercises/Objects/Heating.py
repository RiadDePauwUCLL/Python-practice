# Heating

# An architect must fit multiple heaters in a large building. 
# In order to make a computer simulation of the heat control of the building, he must be able to represent a series of heaters. 
# Every heater is described by the following information fields: a name of the heater, the current setting of the temperature, 
# the minimum temperature allowed and the maximum temperature allowed. 
# In the simulation, the temperature of a certain heater must be increased or decreased, 
# and one must be able at all times to ask the current temperature of every heater.

# Assignment
# Make a class Heater that supports the following methods:

# An initialisation method __init__ that takes the name of the heater (str). 
# In addition, the method also has three optional parameters that take the following information: i) 
# the current setting of the temperature (int or float; default value: 10.0), ii) 
# the minimum temperature allowed (int or float; default value: 0.0) and iii) 
# the maximum temperature allowed (int or float; default value: 100.0).

# A method __str__ that returns a string representation of the heater (str). 
# The exact formatting of the string representation can be derived from the example below. 
# All numbers must be represented with one decimal digit (using rounding).

# A method __repr__ that returns a string representation of the heater (str). 
# Where the method __str__ is used to obtain a human readable string representation of the object, 
# the method __repr__ must return a string representation that makes sense 
# to the Python interpreter: a syntactically correct Python expression, 
# that — when evaluated — makes an object that is equal to the object that is passed to the method __repr__. 
# All numbers must be represented with one decimal digit (using rounding).

# A method change_temperature that can be used to modify the current setting of the temperature. 
# The method takes the increase in temperature (int or float; which actually is a decrease in temperature if a negative number is passed). 
# The method must make sure that the current setting of the temperature always remains within the interval of allowed temperatures. 
# If the new setting of the temperature would be lower than the minimum temperature allowed 
# (resp. higher than the maximum temperature allowed), the new setting of the temperature is 
# equated to the minimum (resp. maximum) temperature allowed.

# A method temperature that returns the current setting of the temperature (float).

# Example
# >>> machine1 = Heater('radiator kitchen', temperature=20)
# >>> machine2 = Heater('radiator living', minimum=15, temperature=18)    
# >>> machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
# >>> print(machine1)
# radiator kitchen: current temperature: 20.0; allowed min: 0.0; allowed max: 100.0
# >>> machine2
# Heater('radiator living', 18.0, 15.0, 100.0)
# >>> machine2.change_temperature(8)
# >>> machine2.temperature()
# 26.0
# >>> machine3.change_temperature(-5)
# >>> machine3
# Heater('radiator bathroom', 18.0, 18.0, 28.0)


class Heater:
    def __init__(self, name, temperature=10.0, minimum=0.0, maximum=100.0):
        self.name = name
        self.current_temp = float(temperature)
        self.min_temp = float(minimum)
        self.max_temp = float(maximum)


    def __str__(self):
        return f'{self.name}: current temperature: {self.current_temp:.1f}; allowed min: {self.min_temp:.1f}; allowed max: {self.max_temp:.1f}'


    def __repr__(self):
        return f"Heater('{self.name}', {self.current_temp:.1f}, {self.min_temp:.1f}, {self.max_temp:.1f})"
    

    def change_temperature(self, n):
        new_temp = self.current_temp + n
        if new_temp < self.min_temp:
            self.current_temp = self.min_temp
        elif new_temp > self.max_temp:
            self.current_temp = self.max_temp
        else:
            self.current_temp = new_temp


    def temperature(self):
        return self.current_temp