from player import Player

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, *items):
        self.name = name
        self.description = description
        self.is_light = False
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

        if len(items) > 0:
            for item in items:
                self.items.append(item)

    def __str__(self):
        return (f"{self.name}")

    def remove_item(self, item):
        self.items.remove(item)


    def add_item(self, item):
        self.items.append(item)

    
    def does_item_exist(self, item):
        for existing_item in self.items:
            if item.lower() == existing_item.name.lower():
                return existing_item
            else:
                print("That item does not exist in this room.")