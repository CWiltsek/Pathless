# Imports Items for the map to give to the player once found and Creautres to populate rooms in the dungeon
from Items import *
from Creatures import *

# Creating the Map class which will hold the map data for the game
class Map:
    
    # Maps stored as nested lists where the position is based on map_name[y][x] in a 30x30 grid
    # S = sword, A = armor, M = staff, H = health potion, K = key, E = exit, C = creature ' ' = empty
    dungeon = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
               ['.', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'], 
               ['.', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    
    reset_dungeon = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
                     ['.', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'], 
                     ['.', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.'],
                     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    
    # Function used to check if the player collides with an Item or Creature and call Player.move() after the collision action is taken
    def check_collision(player):

        # Empty room collision handling
        if Map.dungeon[player.y][player.x] == ' ':

            print('You have reached an empty room. [{x}, {y}]'.format(x = player.x, y = player.y))

        # Exit collision handling
        if Map.dungeon[player.y][player.x] == 'E':

            if Items.skeleton_key in player.backpack:

                print("""
                      Y   Y    OOO     U   U            W   W    IIIII   N   N
                       Y Y    O   O    U   U            W   W      I     NN  N
                        Y     O   O    U   U            W   W      I     N N N
                        Y     O   O    U   U            W W W      I     N  NN
                        Y     O   O    U   U            WW WW      I     N   N
                        Y     O   O    U   U            WW WW      I     N   N
                        Y      OOO      UUU             W   W    IIIII   N   N
                    """)
            
            else:

                print('You must first find the Skeleton Key! You mark down the location of the exit at {x}, {y}.'.format(x = player.x, y = player.y))
                print('After findind the exit without having they key you must choose a direction and distance.')
                new_direction = input('Please choose a cardinal direction you wish to travel in. ')
                new_distance = input('Please choose a whole number distancce you wish to travel. ')
                player.move(new_direction, new_distance)

        # Sword of Avalon collision handling
        if Map.dungeon[player.y][player.x] == 'S':

            print('You found the Sword of Avalon!')
            will_equip = input('The sword will be stored in your backpack unless you equip it. Would you like to equip? Y/N? ')

            if not will_equip.lower() in ['y', 'n']:

                print('Please choose Y or N')
                will_equip = input('Equip the sword? Y/N? ')

            if will_equip.lower() == 'y':

                if not Items.merlins_staff in player.equipped_items:

                    print('You have equipped {equipped}!'.format(equipped = Items.sword_of_avalon['name']))

                    player.equipped_items.append(Items.sword_of_avalon)
                    Items.updateStats(player, Items.sword_of_avalon, False)

                else:

                    print('You have unequipped {unequipped} and have equipped {equipped} instead!'.format(unequipped = Items.merlins_staff['name'], equipped = Items.sword_of_avalon['name']))

                    player.backpack.append(Items.merlins_staff)
                    Items.updateStats(player, Items.merlins_staff, True)
                    player.equipped_items.append(Items.sword_of_avalon)
                    Items.updateStats(player, Items.sword_of_avalon, False)

            else:

                player.backpack.append(Items.sword_of_avalon)

            Map.dungeon[player.y][player.x] = ' '

            print('After findind the Sword of Avalon you must choose a direction and distance.')
            new_direction = input('Please choose a cardinal direction you wish to travel in. ')
            new_distance = input('Please choose a whole number distancce you wish to travel. ')
            player.move(new_direction, new_distance)

        # Merlin's Staff collision handling
        if Map.dungeon[player.y][player.x] == 'M':

            print('You found Merlin\'s Staff!')
            will_equip = input('The staff will be stored in your backpack unless you equip it. Would you like to equip? Y/N? ')

            if not will_equip.lower() in ['y', 'n']:

                print('Please choose Y or N')
                will_equip = input('Equip the sword? Y/N? ')

            if will_equip.lower() == 'y':

                if not Items.sword_of_avalon in player.equipped_items:

                    print('You have equipped {equipped}!'.format(equipped = Items.merlins_staff['name']))

                    player.equipped_items.append(Items.merlins_staff)
                    Items.updateStats(player, Items.merlins_staff, False)

                else:

                    print('You have unequipped {unequipped} and have equipped {equipped} instead!'.format(unequipped = Items.sword_of_avalon['name'], equipped = Items.merlins_staff['name']))

                    player.backpack.append(Items.sword_of_avalon)
                    Items.updateStats(player, Items.sword_of_avalon, True)
                    player.equipped_items.append(Items.merlins_staff)
                    Items.updateStats(player, Items.merlins_staff, False)

            else:

                player.backpack.append(Items.merlins_staff)

            Map.dungeon[player.y][player.x] = ' '

            print('After findind Merlin\'s Staff you must choose a direction and distance.')
            new_direction = input('Please choose a cardinal direction you wish to travel in. ')
            new_distance = input('Please choose a whole number distancce you wish to travel. ')
            player.move(new_direction, new_distance)

        # Stone Skin Armor collision handling
        if Map.dungeon[player.y][player.x] == 'A':

            print('You found the Stone Skin Armor!')
            will_equip = input('The armor will be stored in your backpack unless you equip it. Would you like to equip? Y/N? '.format(item = Items.stone_skin_armor))

            if not will_equip.lower() in ['y', 'n']:

                print('Please choose Y or N')
                will_equip = input('Equip the armor? Y/N? ')

            if will_equip.lower() == 'y':

                print('You have equipped {equipped}!'.format(equipped = Items.stone_skin_armor['name']))

                player.equipped_items.append(Items.stone_skin_armor)
                Items.updateStats(player, Items.stone_skin_armor, False)


            else:

                player.backpack.append(Items.stone_skin_armor)

            Map.dungeon[player.y][player.x] = ' '

            print('After findind the Stone Skin Armor you must choose a direction and distance.')
            new_direction = input('Please choose a cardinal direction you wish to travel in. ')
            new_distance = input('Please choose a whole number distancce you wish to travel. ')
            player.move(new_direction, new_distance)

        # Health potion collision handling
        if Map.dungeon[player.y][player.x] == 'H':

            print('You found a health potion!')
            will_equip = input('The health will be stored in your backpack unless you drink it. Would you like to drink it and gain 10 health points? Y/N? ')

            if not will_equip.lower() in ['y', 'n']:

                print('Please choose Y or N')
                will_equip = input('Use the health potion? Y/N? ')

            if will_equip.lower() == 'y':

                print('You have drank the health potion!')

                Items.updateStats(player, Items.health_potion, False)

            else:

                player.backpack.append(Items.health_potion)

            Map.dungeon[player.y][player.x] = ' '

            print('After findind the health potion you must choose a direction and distance.')
            new_direction = input('Please choose a cardinal direction you wish to travel in. ')
            new_distance = input('Please choose a whole number distancce you wish to travel. ')
            player.move(new_direction, new_distance)

        # Skeleton Key collision handling
        if Map.dungeon[player.y][player.x] == 'K':

            print('You found the Skeleton Key! Time to find the exit.')

            player.backpack.append(Items.skeleton_key)

            Map.dungeon[player.y][player.x] = ' '

            print('After findind the Skeleton Key you must choose a direction and distance.')
            new_direction = input('Please choose a cardinal direction you wish to travel in. ')
            new_distance = input('Please choose a whole number distancce you wish to travel. ')
            player.move(new_direction, new_distance)

        # Creature collision handling
        if Map.dungeon[player.y][player.x] == 'C':

            creature = Creatures()
            
            player.fight(creature)

            Map.dungeon[player.y][player.x] = ' '

            if player.stats['health'] > 0:

                print('After defeating the {creature} you must choose a direction and distance.'.format(crature = creature.type))
                new_direction = input('Please choose a cardinal direction you wish to travel in. ')
                new_distance = input('Please choose a whole number distancce you wish to travel. ')
                player.move(new_direction, new_distance)
