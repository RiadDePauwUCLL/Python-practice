#               Point & Rectangle

# Define a class Point that can be used to represent points in the two-dimensional Euclidean plane. 
# Two arguments must be passed when creating a new point (x & y) (Point): 
# 1) the x-coordinate (int) of the point.
# 2) the y-coordinate (int) of the point.



# Define a class Rectangle that can be used to represent rectangles in
# the two-dimensional Euclidean plane. 

# Three arguments must be passed when creating a new rectangle (Rectangle): 
# 1) the point 'p' (Point) in the top left corner of the rectangle.
# 2) the width 'w' (int) of the rectangle.
# 3) the height 'h' (int) of the rectangle. 

# If it does not hold that (w, h) > 0, an AssertionError must be raised with the message invalid rectangle. 
# Rectangles (Rectangle) must at least support the following methods:


# A method surface_area that returns the surface area (int, w * h) of the rectangle.

# A method circumference that returns the circumference (int, 2*(w + h)) of the rectangle.

# A method bottom_right that returns the point (Point) in the bottom right corner of the rectangle.

# A method overlap that takes a rectangle (Rectangle). 
# If both rectangles (the rectangle on which the method was called and the rectangle passed 
# as an argument to the method) overlap, 
# the method must return a rectangle (Rectangle) that represents the overlapping region 
# of the two rectangles. Otherwise, the value None must be returned.

# If a point (Point) or a rectangle (Rectangle) is passed to the builtin functions repr or str, 
# a string representation (str) of the point or the rectangle must be returned that reads as 
# a Python expression that creates a point or a rectangle at the same location.

# Use the convention that the y-axis is pointed downward, that is: Point(1, 1) is above Point(1, 2).

# Example
# >>> p = Point(3, 4)
# >>> p
# Point(3, 4)
# >>> print(p)
# Point(3, 4)

# >>> r1 = Rectangle(Point(1, 1), 8, 5)
# >>> r2 = Rectangle(Point(2, 3), 9, 2)
# >>> r1
# Rectangle(Point(1, 1), 8, 5)
# >>> print(r2)
# Rectangle(Point(2, 3), 9, 2)
# >>> r1.surface_area()
# 40
# >>> r1.circumference()
# 26
# >>> r1.bottom_right()
# Point(9, 6)
# >>> r1.overlap(r2)
# Rectangle(Point(2, 3), 7, 2)
# >>> r2.overlap(Rectangle(Point(0, 0), 2, 2))

# >>> Rectangle(Point(3, 4), -2, 7)
# Traceback (most recent call last):
# AssertionError: invalid rectangle



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return self.__repr__()


class Rectangle:
    def __init__(self, top_left, width, height):
        if not (width > 0 and height > 0):
            raise AssertionError("invalid rectangle")
        self.top_left = top_left
        self.width = width
        self.height = height

    
    def surface_area(self):
        return self.width * self.height
    

    def circumference(self):
        return 2 * (self.width + self.height)
    

    def bottom_right(self):
        return Point(self.top_left.x + self.width, self.top_left.y + self.height)

    
    def overlap(self, other):
        x1 = max(self.top_left.x, other.top_left.x)
        y1 = max(self.top_left.y, other.top_left.y)
        x2 = min(self.top_left.x + self.width, other.top_left.x + other.width)
        y2 = min(self.top_left.y + self.height, other.top_left.y + other.height)
        if x1 < x2 and y1 < y2:
            return Rectangle(Point(x1, y1), x2 - x1, y2 - y1)
        return None
        
    
    def __str__(self):
        return f"Rectangle({self.top_left}, {self.width}, {self.height})"

    
    def __repr__(self):
        return self.__str__()



xd = Point(2, 5)
print(xd)

r1 = Rectangle(xd, 5, 9)
r2 = Rectangle(Point(6, 3), 3, 6)
# r3 = Rectangle(Point(2, 3), 0, 7)

print(r1.bottom_right())
print(r1.surface_area())
# print(r3.circumference())
print(r2.overlap(Rectangle(Point(6, 3), 3, 6)))