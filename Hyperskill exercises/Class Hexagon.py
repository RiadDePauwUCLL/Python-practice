# Hexagon

# The class Hexagon represents the regular hexagons (all sides are equal in length and all angles equal 120°). 
# The only parameter needed to create a regular hexagon is the length of its side t.

# Create a method get_areathat calculates the area of the hexagon according to the formula: S = (3(sqrt)3*t²) / 2

# The name of the method has to be get_area! The method doesn't receive any parameters and it doesn't print anything, 
# it just returns the calculated area (rounded to 3 decimals). You do NOT need to call the method in your program!

# To calculate the square root use the math.sqrt(x) method (the math module has already been imported).

# There is no input to read, so you do NOT need to work with it, and nothing else is required.

# Write code here:

import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return round((3 * math.sqrt(3) * self.side_length ** 2) / 2, 3)