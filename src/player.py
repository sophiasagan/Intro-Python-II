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

    # player move method
    def move(self, direction):
        new_room = getattr(self.current_room, direction)
        if new_room is not None:
            self.current_room = new_room
        else:
            print("Ye shall not pass!!" "\n There's no room in that direction. Try a different way.")

    # player method to pickup items 
    def pickup_item(self, item):
        self.inventory.append(item)
        print(f"Ye have picked up a(n) {item.name}.")
        print(item.description)

    # player method to drop items 
    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"Ye have dropped a(n) {item.name}.")

    # find item in player inventory 
    def find_item(self, item):
        for existing_item in self.inventory:
            if item.lower() == existing_item.name.lower():
                return existing_item

    # display inventory
    def display_inventory(self):
        if len(self.inventory) == 0:  
            print("Ye do not have any items in yer purse.")
        else:
            print("Current Inventory:")
            for item in self.inventory:
                print(f"Name: {item.name}\t Description: {item.description}")
