import json
import os
from actions import Action
from items import Item
from assets import character_images
from os import listdir
from os.path import isfile, join
import pygame 
class Character():
    def __init__(self, type_):
        f = open(os.path.join("data/character_data.json"))
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no character availible")
        self.character = data[type_]
        self.type = type_
        self.actions = []
        self.items = []
        self.sprite = self.get_sprite()

        for action in self.character["actions"]:
            self.actions.append(Action(action))
        for item in self.character["items"]:
            self.items.append(Item(item))

    def __str__(self):
        return self.type
    
    # return character sprite in size x by y pixels 
    def sprite_size(self,w,h):
        return pygame.transform.scale(self.sprite, (w, h))

    def get_sprite(self):
        sprite = None
        path = 'assets/character_images/'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for file in onlyfiles:
            if file.split('.')[0] == self.type:
                sprite = pygame.image.load(path + file)
        return sprite

def create_all_characters():
    return_list = []
    f = open(os.path.join("data/character_data.json"))
    data = json.load(f)
    character_data = data.keys()
    for char in character_data:
        c = Character(char)
        return_list.append(c)
    return return_list