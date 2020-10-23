import json
import os
from actions import Action
from items import Item


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
        for action in self.character["actions"]:
            self.actions.append(Action(action))
        for item in self.character["items"]:
            self.items.append(Item(item))

    def __str__(self):
        return self.type

def create_all_characters():
    return_list = []
    f = open(os.path.join("data/character_data.json"))
    data = json.load(f)
    character_data = data.keys()
    for char in character_data:
        c = Character(char)
        return_list.append(c)
    return return_list