# Creating the Item class which will hold the items and their attributes
class Items:
    
    # Item variables with their attributed stored in dictionaries
    sword_of_avalon = {'name': 'Sword of Avalon', 'stats': {'attack': 11, 'speed': 2}}

    merlins_staff = {'name': 'Merlin\'s Staff', 'stats': {'intelligence': 5, 'attack': 7}}

    stone_skin_armor = {'name': 'Stone Skin Armor', 'stats': {'defense': 15}}

    skeleton_key = {'name': 'Skeleton Key'}

    health_potion = {'name': 'Health Potion', 'stats': {'health': 10}}

    # A function to udate the player's stats based on the equipped item.
    def updateStats(player, item, is_being_unequipped):

        if not is_being_unequipped:

            for key in item['stats']:

                player.stats[key] += item['stats'][key]

        else:

            for key in item['stats']:

                player.stats[key] -= item['stats'][key]