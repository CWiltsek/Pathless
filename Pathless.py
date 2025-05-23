# Imports everything contained in the Creatures, Player, Map, and Item files
from Map import *
from Items import *
from Creatures import *
from Player import *

# The main class where the game start will be called from
class main:

    # Function to initialize the game
    def start():

        # Creates an instance of the Player class with input
        print('Welcome to the dungeon!')
        name = input('Please choose your character\'s name. ')
        if not type(name) == str:
            print('Invalid name choice. Must be a valid string. ')
            name = input('Please choose your character\'s name. ')
        race = input('Now choose a race between Elf, Ork, Human, or Wizard. ')
        if not race.title() in Player.races:
            print('Invalid race choice. ')
            race = input('Please choose a race between Elf, Ork, Human, or Wizard. ')
        player = Player(name, race)

    start()
