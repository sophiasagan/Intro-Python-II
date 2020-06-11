import textwrap

from room import Room
from player import Player
from item import Item, Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of ye, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before Ye, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """Ye've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# room['outside'].is_light = True
# room['foyer'].is_light = True

# Add some items

t = Treasure("coins", "Shiny coins\n" "It's something but it ain't no treasure...", 20)
room['overlook'].items.append(t)

t = Treasure("silver", "Tarnished silver\n" "Now that's some spending money, maybe enough for a nipperkin of ale or rum...", 200)
room['narrow'].items.append(t)

t = Treasure("gold", "Glinting gold\n" "Looks like ye found what's left of the gold. Ye best be going now....", 1000)
room['treasure'].items.append(t)

l = LightSource("lamp", "Old Dusty lamp\n" "Well, it beats being completely in the dark...")
room['foyer'].items.append(l)

l = LightSource("torch", "bright torch\n Ye can see ....")
room['overlook'].items.append(l)

i = Item("stick", "Wooden walking staff\n" "I can use this to poke around and keep balance...")
room['outside'].items.append(i)


#
# Main
#
name = input("Tell me yer name and I'll tell ye a tale....: \n")
# Make a new player object that is currently in the 'outside' room.
player = Player(name, room['outside'])

#print(player.name)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


moves = ['n', 's', 'e', 'w']
actions = ['i', 'inventory']
points = ['score', 'booty', 'loot']


print(f"\n\nWelcome, {player.name}. Will ye find treasure or DEATH?!")
print("-" * 100)
print("CONTROLS:")
print(
    "Move using [n] north, [s] south, [e] east, and [w] west.")
print(
    "Pickup items using [get ItemName], drop items using [drop ItemName], get score using [score] or quit [q]")
print("-" * 100)


while True:
    # light sources:
    # light_sources = [item for item in player.items + player.current_room.items
    #                  if isinstance(item, LightSource) and item.lightsource]

    # is_light = player.current_room.is_light or len(light_sources) > 0

    # if is_light:
    #     # Print the room name
    #     print("\n{}\n".format(player.current_room.name))

    #     # Print the room description
    #     for line in textwrap.wrap(player.current_room.description):
    #         print(line)

    #     # Print any items found in the room
    #     # if len(player.current_room.items) > 0:
    #     #     print("\nYe see:\n")
    #     #     for i in player.current_room.items:
    #     #         print("     " + str(i))
    # else:
    #     print("\nIt's very dark!\n")

    print(f"\n{player.name}, ye entered:  " + player.current_room.name)
    for line in textwrap.wrap(player.current_room.description):
        print(line)

    # if there are any available items in the room, display them to the player
    for item in player.current_room.items:
        print(f"\n\nLook here las, ye found a(n) {item.name}.\n\nBlimey, don'tcha just stare at it... pick it up!")

    print("\n\n"'Which direction will ye travel?\n')
    player_input = input("> ")

    if player_input == 'q':  # quit the game if the user inputs q
        exit()
    elif player_input in moves:  # if the user selects a direction to move, use our move method
        player.move(f'{player_input}_to')
    elif player_input in actions:  # if the user opens their inventory, use our display inventory method
        player.display_inventory()
    elif player_input in points:
        print(f'Yer booty is currently worth {player.score} shillings.') # if user wants to see accumulated score
    elif "get" in player_input or "take" in player_input:
        # if user inputs "get" or "take", determine if they've entered in
        # a valid item that exists in the room, and use our pickup method
        print("Putting item in purse...")
        item.on_take(player)
        words = player_input.split()
        

        if len(words) > 1:
            selection = words[1]
            found_item = player.current_room.does_item_exist(selection)

            print(found_item)
            if found_item:
                player.pickup_item(found_item)
                player.current_room.remove_item(found_item)
        else:
            print("What are ye trying t' pickup?") # the user did not input an item, or it didn't exist

    elif "drop" in player_input:
        # if the user inputs "drop", determine if they've entered in a
        # valid item that exists in their inventory, and use our drop method
        print("Digging through purse...")
        item.on_drop(player)
        words = player_input.split()

        if len(words) > 1:
            selection = words[1]
            found_item = player.find_item(selection)

            if found_item:
                player.current_room.add_item(found_item)
                player.drop_item(found_item)
        else:
            print("What do ye want t' leggo?") # the user did not input an item, or it didn't exist