class Attraction:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.visitors = 0


    @property
    def name(self):
        return self.__name
    
    @property
    def height(self):
        return self.__height
    
    @property
    def visitors(self):
        return self.__visitors
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @height.setter
    def height(self, value):
        if value is None or value < 0: 
            raise ValueError("u tiny")
        else:
            print("you can go!")
        self.__height = value

    @visitors.setter
    def visitors(self, value):
        self.__visitors = value

    def visit(self, height):
        if height >= self.__height:
            self.visitors += 1
            print("enjoy!")
        else:
            with open('log.txt', 'a') as f:
                f.write(f'Visitor with height {height} is too small, so the person cannot visit {self.__name}')


# Attractions
de_pagode = Attraction("De Pagode", 0)
max_moritz = Attraction("Max & Moritz", 100)
de_baron = Attraction("De Baron", 132)

max_moritz.visit(150)
max_moritz.visit(150)
max_moritz.visit(50)