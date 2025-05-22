# Creating the Creatures class to create the various creatures and hold their type, stats, and aggression_level
class Creatures:

    # Dictionary containing the different creature types
    types = {}

    # Constructor for Creatures class that will choose the creature's type and base it's stats and aggression_level based on the type
    def __init__(self, type):
        self.type = type
