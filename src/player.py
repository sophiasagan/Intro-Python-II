from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.items = []
        self.score = 0

    # player method to move the user in a direction
    # if there is no room in the direction moved, alert the user to try a different way
    def move(self, direction):
        new_room = getattr(self.current_room, direction)
        if new_room is not None:
            self.current_room = new_room
        else:
            print("You shall not pass!!" "\n There's no room in that direction. Try a different way.")

    # player method to pickup items from a room and add them to player's inventory
    def pickup_item(self, item):
        self.inventory.append(item)
        print(f"You have picked up a(n) {item.name}.")
        print(item.description)

    # player method to drop items from the player's inventory
    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You have dropped a(n) {item.name}.")

    # find item in player inventory to determine if it exists
    def find_item(self, item):
        for existing_item in self.inventory:
            if item.lower() == existing_item.name.lower():
                return existing_item

    # display the items in a player's inventory
    def display_inventory(self):
        if len(self.inventory) == 0:  # if the player's inventory is empty, let them know
            print("You do not have any items in your inventory.")
        else:
            print("Current Inventory:")
            for item in self.inventory:
                print(f"Name: {item.name}\t Description: {item.description}")

    # def display_score(self, score):
    #     if s[0] == "score":
    #         print(f"Your score is currently {item.score}.")