# Imports everything from the Items file for the Player class to use
from Items import *

# Creating the Player class  to store the players name, race, stats, location, and items
class Player:

    races = ['Elf', 'Ork', 'Human', 'Wizard']

    # Contructor for the Player class where the player can choose a name and race and have their stats, location, and items stored in their bag
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.stats = {'health': 10, 'attack': 10, 'defense': 10, 'speed': 10, 'intelligence': 10}
        self.backpack = []
        self.equipped_item = Items()
        self.location = [0, 0]