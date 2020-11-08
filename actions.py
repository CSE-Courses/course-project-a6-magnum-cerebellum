import json
import os

class Action():
    def __init__(self, type_):
        f = open(os.path.join("data/action_data.json"))
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no action availible") 
        self.action = data[type_]
        self.action_name = type_
        self.damage = self.action["damage_level"]

    def __str__(self):
        return self.action_name
        