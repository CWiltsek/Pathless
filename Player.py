# Imports everything from the Items and Map files for the Player class to use
from Items import *
from Map import *

# Creating the Player class  to store the players name, race, stats, location, and items
class Player:

    races = ['Elf', 'Ork', 'Human', 'Wizard']

    # Contructor for the Player class where the player can choose a name and race and have their stats, location, items stored in their bag, and if the pllayer is busy in an action
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.stats = {'health': 10, 'attack': 10, 'defense': 10, 'speed': 10, 'intelligence': 10}
        self.backpack = []
        self.equipped_item = Items.no_item
        self.x = 1
        self.y = 1
        self.is_busy = False

        # Changes player stats based on chosen race
        if race.title == 'Elf':
            self.stats['speed'] += 5

        if race.title == 'Ork':
            self.stats['attack'] += 5

        if race.title == 'Human':
            for key in self.stats.keys():
                self.stats[key] += 1

        if race.title == 'Wizard':
            self.stats['intelligence'] += 5

    # The move function to handle player movement given input and checking if a wall is reached
    def move(self, direction, distance):

        if not direction in ['north', 'south', 'east', 'west']:

            print('Please choose on of the four cardinal directions (North, South, East, or West) ')
            new_direction = input('Please specify a direction. ')
        
            if int(distance) < 0:

                print('Please choose a positve numbered distance to travel. ')
                new_distance = input('Please specify the distance you wish to travel. ')

                self.move(new_direction, new_distance)

            self.move(new_direction, distance)

        distance_remaining = int(distance)

        while distance_remaining > 0 and not self.is_busy:

            if direction.lower() == 'north':

                if self.y == 1:

                    print('You have reached a wall. Please choose another direction and distance.')
                    new_direction = input('Please specify a direction. ')

                    if not type(new_direction) == str or not new_direction.lower() in ['north', 'south', 'east', 'west']:

                        print('Invalid directions choice. Please choose between north, south, east, or west. ')
                        new_direction = input('Specify a direction. ')

                    new_distance = input('Now specify a distance. ')

                    if not type(new_distance) == int or not new_distance < 29:

                        print('Invalid distance. Please choose a distance between 1 and 28. ')
                        new_distance = input('Specify a distance. ')

                    self.move(new_direction, new_distance)

                    break

                self.y -= 1
                distance_remaining -= 1
                Map.check_collision(self)

            elif direction.lower() == 'south':

                if self.y == 28:

                    print('You have reached a wall. Please choose another direction and distance.')
                    new_direction = input('Please specify a direction. ')

                    if not type(new_direction) == str or not new_direction.lower() in ['north', 'south', 'east', 'west']:

                        print('Invalid directions choice. Please choose between north, south, east, or west. ')
                        new_direction = input('Specify a direction. ')

                    new_distance = input('Now specify a distance. ')

                    if not type(new_distance) == int or not new_distance < 29:

                        print('Invalid distance. Please choose a distance between 1 and 28. ')
                        new_distance = input('Specify a distance. ')

                    self.move(new_direction, new_distance)

                    break

                self.y += 1
                distance_remaining -= 1
                Map.check_collision(self)

            elif direction.lower() == 'east':

                if self.x == 28:

                    print('You have reached a wall. Please choose another direction and distance.')
                    new_direction = input('Please specify a direction. ')

                    if not type(new_direction) == str or not new_direction.lower() in ['north', 'south', 'east', 'west']:

                        print('Invalid directions choice. Please choose between north, south, east, or west. ')
                        new_direction = input('Specify a direction. ')

                    new_distance = input('Now specify a distance. ')

                    if not type(new_distance) == int or not new_distance < 29:

                        print('Invalid distance. Please choose a distance between 1 and 28. ')
                        new_distance = input('Specify a distance. ')

                    self.move(new_direction, new_distance)

                    break

                self.x += 1
                distance_remaining -= 1
                Map.check_collision(self)

            elif direction.lower() == 'west':

                if self.x == 1:

                    print('You have reached a wall. Please choose another direction and distance.')
                    new_direction = input('Please specify a direction. ')

                    if not type(new_direction) == str or not new_direction.lower() in ['north', 'south', 'east', 'west']:

                        print('Invalid directions choice. Please choose between north, south, east, or west. ')
                        new_direction = input('Specify a direction. ')

                    new_distance = input('Now specify a distance. ')

                    if not type(new_distance) == int or not new_distance < 29:

                        print('Invalid distance. Please choose a distance between 1 and 28. ')
                        new_distance = input('Specify a distance. ')

                    self.move(new_direction, new_distance)

                    break

                self.x -= 1
                distance_remaining -= 1
                Map.check_collision(self)
