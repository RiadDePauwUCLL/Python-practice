# A fairly classic way to set colours in a computer program consists of 
# splitting the colour in three components: red, green and blue. 
# Each of these components is an integer and takes a value betwee 0 and 255 (boundaries included). 
# Within this system, the greyscales correspond to the colours in which the three components have the same value.

# If a photo must be printed as a greyscale picture, every colour must be converted to a specific greyscale. 
# You could use the mean value, for example, but this gives a wrong image, since the human eye is not equally sensitive to every colour. This is why the following conversion is often used:

# greyscale = 30% of red + 59% of green + 11% of blue
# If a picture should be made unrecognizable, one sometimes inverts parts of the picture. 
# Here, every colour is replaced by its inverse colour. In order to obtain this colour, 
# you should replace every component by 255 minus that component. 

# Assignment
# Your assignment consists of making a class Colour with the following methods:

# The initializing method __init__ gets the three colour components as parameters, 
# where each component gets the value 0 as a standard. 
# Make sure that only components between 0 and 255 are used: values smaller than 0 are replaced with 0, 
# values larger than 255 are replaced with 255.

# The method __str__ represents this colour as a string in the format (R, G, B), where R, G and B indicate the different components.

# The method inverse prints a new Colour that represents the inverse colour.

# The method greyscale prints a new Colour that represents the greyscale of this colour according to the calculation above. 
from math import floor

class Colour():
    def __init__(self, r, g, b):
        self.r = min(255, max(0, r))
        self.g = min(255, max(0, g))
        self.b = min(255, max(0, b))

    def greyscale(self):
        grey = floor((self.r * .3) + (self.g * .59) + (self.b * .11))
        return Colour(grey, grey, grey)

    def inverse(self):
        inversed_r = 255 - self.r
        inversed_g = 255 - self.g
        inversed_b = 255 - self.b
        return Colour(inversed_r, inversed_g, inversed_b)

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

c = Colour(128, 62, 350)
g = c.greyscale()
print(isinstance(g, Colour))
print(g)

XD = Colour(25, 50, 305)
Gigachad = Colour(-4, 20, 69)
print(XD)
print(Gigachad)
bruh = XD.greyscale()
moment = Gigachad.greyscale()
print(bruh)
print(moment)
big = XD.inverse()
exdee = Gigachad.inverse()
print(big)
print(exdee)