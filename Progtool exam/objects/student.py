class Pair:

    def __init__(self):
        self.first = None
        self.second = None


class Position:

    def __init__(self, x , y):
        self.x = x
        self.y = y


class Interval:

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        if self.lower > self.upper:
            return True
        else:
            return False

    def contains(self, value):
        if self.lower <= value <= self.upper:
            return True
        else:
            return False
        
    def overlaps_with(self, other):
        if self.is_empty() or other.is_empty():
            return False
        else:
            return self.upper >= other.lower and self.lower <= other.upper
        

class Password:

    def __init__(self, password):
        self.__password = password

    def verify(self, password):
        if self.__password == password:
            return True
        else:
            return False
        
# we basically make it a private field thanks to the "__".
# don't rely on the explanation within the exercises, it's terrible..
        

class Averager:

    def __init__(self, list=None):
        if list is None:
            self.__list = []
        else:
            self.__list = list

# alternative option:
#   def __init__(self):
#       self.reset()

    def add(self, value):
        self.__list.append(value)

    def average(self):
        if len(self.__list) == 0:
            return 0
        else:
            total = sum(self.__list)
            count = len(self.__list)
            return total / count

    def reset(self):
        self.__list = []

# Here we compute the average of values within a list.
# we append the values within the empty list and proceed with checking the average of that list.
# if we have to reset, we use the reset function by replacing it with an empty list.
        

class Counter:

    def __init__(self):
        self.reset()

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        self.__count = value

    def increment(self):
        self.__count += 1

    def reset(self):
        self.__count = 0

# The self.reset() here is quite self-explanatory now.
        

class Unit:

    def __init__(self, health, firepower, armor):
        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError()
        
        self.health = health
        self.firepower = firepower
        self.armor = armor

    @property
    def health(self):
        return self.__health
    
    @property
    def firepower(self):
        return self.__firepower
    
    @property
    def armor(self):
        return self.__armor
    
    @health.setter
    def health(self, value):
        self.__health = value

    @firepower.setter
    def firepower(self, value):
        self.__firepower = value

    @armor.setter
    def armor(self, value):
        self.__armor = value

    def shot_by(self, other):
        damage = other.firepower - self.armor
        if damage < 0:
            damage = 0
        self.__health -= damage
        if self.health < 0:
            self.health = 0



class Tweet:

    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError()
        self._max_length = max_length
        self._message = message[:self._max_length]

    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, value):
        self._message = value[:self._max_length]

    @property
    def max_length(self):
        return self._max_length
    
    @max_length.setter
    def max_length(self, value):
        if value < 1:
            raise ValueError()
        self._max_length = value
        self._message = self._message[:value]

# here we check the max_length of the tweet. The code is pretty self-explanatory:
# we check the length of the tweet & we can redefine the length with the setter.
# if the max_length is invalid it's going to cause a ValueError.