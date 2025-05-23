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
        self.equipped_item = Items.no_item
        self.x = 1
        self.y = 1

    def move(self, direction, distance):
        distance_remaining = distance
        if direction.lower() == 'north':
            if self.y == 1 and distance_remaining > 0:
                print('You have reached a wall. Please choose another direction and distance.')
                new_direction = input('Please specify a direction. ')
                new_distance = input('Now specify a distance. ')
                if not type(new_direction) == str or not new_direction.lower() in ['north', 'east', 'south', 'west']:
                    print('Invalid directions choice. Please choose between north, south, east, or west. ')
                    new_direction = input('Please specify a direction. ')
                if not type(new_distance) == int or not new_distance < 29:
                    print('Invalid distance. Please choose a distance between 1 and 28. ')
                    new_distance = input('Now specify a distance. ')