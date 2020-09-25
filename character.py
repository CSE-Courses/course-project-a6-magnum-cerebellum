import json
import os

class Character():
    def __init__(self, type_):
        f = open(os.path.join("data/character_data.json"))
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no character availible") 
        self.character = data[type_]
        self.type = type_
        self.actions = self.character["actions"]
        self.items = self.character["items"]
    
    def __str__(self):
        return self.type