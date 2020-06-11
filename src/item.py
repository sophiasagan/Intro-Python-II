class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        pass

    def __str__(self):
        return (f"Item: {self.name}")

    def on_drop(self, player):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        self.picked_up = False
        super().__init__(name, description)

    def on_take(self, player):
        super().on_take(player)

        if not self.picked_up:
            player.score += self.value
            print(f"You get {self.value} points!")
            self.picked_up = True

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.lightsource = True

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def on_drop(self, player):
        super().on_drop(player)
        print("Damn to the depths, me thinks yer daft walkin' around 'ere blind mate!\n")