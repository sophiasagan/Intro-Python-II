# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        new_room = getattr(self.current_room, direction)
        if new_room is not None:
            self.current_room = new_room
        else:
            print('That move leads to nowhere.')
