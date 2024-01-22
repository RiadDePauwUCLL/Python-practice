# Make sure you have all the names correct
# this includes function, class, method, and parameters


def csom(n):
    num = sum(int(digit) for digit in str(n))
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

# other possible solutions

# def csom(n):
#     while n >= 10:
#         total = 0
#         for digit in str(n):
#             total += int(digit)
#         n = total
#     print(n)
#     return n

# def csom(n):
#     sum_of_digits = 0
#     while n > 0:
#         sum_of_digits += n % 10
#         n //= 10

#     if (sum_of_digits >= 10):
#         return csom(sum_of_digits)
#     else:
#         return sum_of_digits

print(csom(8))
print(csom(302))
print(csom(129))
print(csom(377096267))

def isPalindrome(t):
    return t[::1] == t[::-1]





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
        # else:
        #     print("you can go!")
        self.__height = value

    @visitors.setter
    def visitors(self, value):
        self.__visitors = value

    def visit(self, height):
        if height >= self.__height:
            self.visitors += 1
            # print("enjoy!")
        else:
            with open('log.txt', 'a') as f:
                f.write(f'Visitor with height {height} is too small, so the person cannot visit {self.__name}')


# Attractions
de_pagode = Attraction("De Pagode", 0)
max_moritz = Attraction("Max & Moritz", 100)
de_baron = Attraction("De Baron", 132)
de_baron2 = Attraction("", 132)
max_moritz.visit(150)
max_moritz.visit(150)
de_baron2.visit(150)
# max_moritz.visit(50)






class ThemePark:

    def __init__(self, name):
        self.name = name
        self.attractions = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value or not value[0].isupper():
            raise ValueError("Name must start with a capital letter & cannot be empty")
        self.__name = value

    def addAttraction(self, attraction):
        if not any(a.name.lower().replace(' ', '') == attraction.name.lower().replace(' ', '') for a in self.attractions):
            self.attractions.append(attraction)

    def printOverview(self):
        total_visits = sum(a.visitors for a in self.attractions)
        print(f'{self.name} is an amusement park with {len(self.attractions)} attractions visited a total of {total_visits} times.')

    def securityupdate(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                new_height, attractions = line.split(':')
                new_height = int(new_height.strip().split(' ')[0])
                attractions = [a.strip() for a in attractions.split(',')]
                for attraction in attractions:
                    for a in self.attractions:  
                        if a.name.lower().replace(' ', '') == attraction.lower().replace(' ', ''):
                            a.height = new_height
                            break
                    else:
                        with open('log.txt', 'a') as log:
                            log.write(f"Attraction {attraction} does not exist in the amusement park.\n")

        print("Overview of the attractions after security update:")
        for a in self.attractions:
            print(f"- {a.name}: {a.height} cm")


# create theme park
efteling = ThemePark("The Efteling")

efteling.printOverview()

efteling.addAttraction(de_pagode)
efteling.printOverview()

efteling.addAttraction(max_moritz)
efteling.addAttraction(de_baron)
efteling.printOverview()

efteling.securityupdate('update.txt')