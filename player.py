from character import Character
from items import Item
from config import * 
import math


class Player():
    def __init__(self, character):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.health = 10
        self.hp = 10
        self.character = character
   # def add_item(self, item):
   #     new_item = Item(item)
    #    self.items.append(new_item)

    @property
    def pos(self):
        return (self.x, self.y)

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

    # set character's location #
    # changes self.pos attribute to new position. If position is out of range self.pos is not updated #
    # returns players position self.pos #
    def set_location(self, x, y):
        if not (x < 0 or x > render_display_width or y < 0 or y > render_display_height):
            self.pos = (x, y)
        return self.pos

    def draw(self):
        pass

  #  def __str__(self):
   #     return "player of " + self.character.type

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
    


