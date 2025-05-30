# Creating the Item class which will hold the items and their attributes
class Items:
    
    # Item variables with their attributed stored in dictionaries
    no_item = {'name': 'Nothing', 'stats': {'attack': 0}}

    sword_of_avalon = {'name': 'Sword of Avalon', 'stats': {'attack': 11, 'speed': 2}}

    merlins_staff = {'name': 'Merlin\'s Staff', 'stats': {'intelligence': 5, 'attack': 7}}

    stone_skin_armor = {'name': 'Stone Skin Armor', 'stats': {'defense': 15}}

    skeleton_key = {'name': 'Skeleton Key'}

    health_potion = {'name': 'Health Potion', 'stats': {'health': 10}}

    # A function to udate the player's stats based on the equipped item.
    def updateStats(player, is_being_unequipped):

        if not is_being_unequipped:

            for key in player.equipped_item['stats']:

                player.stats[key] += player.equipped_item['stats'][key]

        else:

            for key in player.equipped_item['stats']:

                player.stats[key] -= player.equipped_item['stats'][key]