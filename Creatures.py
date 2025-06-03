# Imports random to use for random selection of the cretures type
import random

# Creating the Creatures class to create the various creatures and hold their type, stats, and aggression_level
class Creatures:

    # Dictionary containing the different creature types
    types = {'Minotar', 'Basolisk', 'Undead', 'Troll'}

    # Constructor for Creatures class that will choose the creature's type randomly and base it's stats on the type
    def __init__(self):

        self.type = type = random.choice(Creatures.types)
        self.stats = {'health': 10, 'attack': 10, 'defense': 10, 'speed': 10}

        if type == 'Minotar':
            self.stats['attack'] += 10

        if type == 'Basolisk':
            self.stats['speed'] += 10

        if type == 'Undead':
            self.stats['health'] += 10

        if type == 'Troll':
            self.stats['health'] += 3
            self.stats['defense'] += 5
            self.stats['attack'] += 2
