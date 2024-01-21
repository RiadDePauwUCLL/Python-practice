import random

class Player:
    def __init__(self, name, weapon, kills=0):
        self.__name = name
        self.weapons = [weapon]
        self.kills = kills
        self.is_alive = True        # you don't necessarily always have to have a variable as a parameter.

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, other):
        if self.__name == other:
            raise AssertionError("Same name, same player!")

    def kill(self, other):
        if not self.is_alive:
            raise AssertionError("Player is dead, cannot kill")
        if not other.is_alive:
            raise AssertionError("Cannot kill a player who is already dead")
        if self.name == other.name:
            raise AssertionError("Cannot kill oneself")
        
        self.kills += 1
        for weapon in other.weapons:
            if weapon not in self.weapons:
                self.weapons.append(weapon)
        other.is_alive = False
        
    def __str__(self):
        status = 'is dead' if not self.is_alive else 'is alive'
        return f'{self.__name} {status}\nnumber of murders: {self.kills}\nWeapons: {self.weapons}'
    


class Combat:
    def __init__(self, player1, player2):
        if player1.name == player2.name:
            raise AssertionError("Players must be different")
        if not player1.is_alive or not player2.is_alive:
            raise AssertionError("Both players have to be alive to fight")
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        if random.choice([True, False]):
            self.player1.kill(self.player2)
        else:
            self.player2.kill(self.player1)


# Create two players
player1 = Player("Tom", 'Gun', 5)
player2 = Player("Jerry", "Cheese")
gamer = Player("Tom", 'Gun', 2)
loser = Player("Yorick", "Hammer", 1)

# Create a combat
combat = Combat(player1, player2)

# Start the fight
combat.fight()

# Print the players
print(player1)
print(player2)
gamer.kill(loser)
print(loser)
print(gamer)
