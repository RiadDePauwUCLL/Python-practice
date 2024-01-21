import random

# not gonna lie, I used AI for help on this one. I didn't want to get stuck for hours,
# This is definitely a more advanced type of class,
# Personally, it would be highly unlikely something like this comes on the exam.
# Was fun though.


class Mines:
    def __init__(self, x, y, hit=False):
        self.x = x
        self.y = y
        self._hit = hit

    def hit(self):
        self._hit = True

    def is_hit(self):
        if self._hit is True:
            return f'The mine has been hit! oh nooo scaryyyyy'


class Field:
    def __init__(self, height, Mines):
        if not 3 <= height <= 5:
            raise AssertionError('Height must be between 3 & 5')
        
        self.height = height
            
        seen = set()
        for mine in Mines:
            if not (1 <= mine.x <= height and 1 <= mine.y <= height):
                raise AssertionError("Mine coordinates must be within the field")
            if (mine.x, mine.y) in seen:
                raise AssertionError("Duplicate mine coordinates")

        self.mines = Mines

    def __repr__(self):
        field_repr = ""
        for y in range(1, self.height + 1):
            for x in range(1, self.height + 1):
                if any(mine.x == x and mine.y == y and mine._hit for mine in self.mines):
                    field_repr += "X "
                else:
                    field_repr += ". "
            field_repr += "\n"
        return field_repr
    

    def hit_mine(self, x, y):
        for mine in self.mines:
            if mine.x == x and mine.y == y:
                mine.hit()
                return True
        return False
    

height = int(input("Enter the size of the scary field: "))
x = random.randint(1, height)
y = random.randint(1, height)
field = Field(height, [Mines(x, y)])

while True:
    print(field)
    choice = int(input("0. Quit the game.\n1. Enter a coordinate.\n"))
    if choice == 0:
        break
    elif choice == 1:
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        field.hit_mine(x, y)


# xd = Mines(5, 6)

# xd.hit()
# xd.is_hit()
# print(xd)