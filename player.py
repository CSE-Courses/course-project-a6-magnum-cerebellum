from character import Character
from items import Item
import config

class Player():
    def __init__(self, character):
        self.pos = (0,0)
        self.health = 10
        self.character = character
        self.actions = self.character.actions
        self.items = self.character.items
        self.hp = 10
    
    # return False if decrease kills player, true otherwise. Update player hp with decreased ammount
    def decrease_hp(self, n):
        if (self.hp - n) <= 0:
            self.hp = 0
            return False
        else:
            self.hp = self.hp - n
            return True

    def add_item(self, item):
        new_item = Item(item)
        self.items.append(new_item)

    # set character's location #
    # changes self.pos attribute to new position. If position is out of range self.pos is not updated #
    # returns players position self.pos #
    def set_location(self, x, y):
        if not (x < 0 or x > config.display_width or y < 0 or y > config.display_height):
            self.pos = (x, y)
        return self.pos
    def draw(self):
        pass
    def __str__(self):
        return "player of " + self.character.type
    
