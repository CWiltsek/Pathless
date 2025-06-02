# Imports everything contained in the Creatures, Player, Map, and Item files
from Map import *
from Items import *
from Creatures import *
from Player import *

# The main class where the game start will be called from
class main:

    # Resets the game to a base state
    def reset():

        Map.dungeon = Map.reset_dungeon

    # Function to initialize the game
    def start():

        # Creates an instance of the Player class with input
        print("""
                    W   W    EEEEE    L         CCCC     OOO     M   M    EEEEE        TTTTT     OOO         TTTTT    H   H    EEEEE
                    W   W    E        L        C        O   O    MM MM    E              T      O   O          T      H   H    E 
                    W   W    E        L        C        O   O    MM MM    E              T      O   O          T      H   H    E 
                    W W W    EEEEE    L        C        O   O    M M M    EEE            T      O   O          T      HHHHH    EEEEE
                    WW WW    E        L        C        O   O    M   M    E              T      O   O          T      H   H    E 
                    WW WW    E        L        C        O   O    M   M    E              T      O   O          T      H   H    E 
                    W   W    EEEEE    LLLLL     CCCC     OOO     M   M    EEEEE          T       OOO           T      H   H    EEEEE
              
                                                DDDD     U   U    N   N     GGG     EEEEE     OOO     N   N
                                                D   D    U   U    NN  N    G   G    E        O   O    NN  N 
                                                D   D    U   U    N N N    G        E        O   O    N N N 
                                                D   D    U   U    N  NN    G  GG    EEEEE    O   O    N  NN
                                                D   D    U   U    N   N    G   G    E        O   O    N   N
                                                D   D    U   U    N   N    G   G    E        O   O    N   N 
                                                DDDD      UUU     N   N     GGG     EEEEE     OOO     N   N 
                  """)
        name = input('Please choose your character\'s name. ')
        if not type(name) == str:
            print('Invalid name choice. Must be a valid string. ')
            name = input('Please choose your character\'s name. ')
        race = input('Now choose a race between Elf, Ork, Human, or Wizard. ')
        if not race.title() in Player.races:
            print('Invalid race choice. ')
            race = input('Please choose a race between Elf, Ork, Human, or Wizard. ')
        player = Player(name, race)

        print('After choosing your name and race please choose a direction and distance to travel.')
        new_direction = input('Please choose a cardinal direction you wish to travel in. ')
        new_distance = input('Please choose a whole number distancce you wish to travel. ')
        player.move(new_direction, new_distance)

    start()
