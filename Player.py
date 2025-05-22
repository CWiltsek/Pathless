# Creating the Player class  to store the players name, race, stats, and items
class Player:
    
    races = ['Elf', 'Ork', 'Human', 'Wizard']

    # Contructor for the Player class where the player can choose a name and rae and have their stats and items stored
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.stats = {'health': 10, 'attack': 10, 'defense': 10, 'speed': 10, 'intelligence': 10}
        self.items = []