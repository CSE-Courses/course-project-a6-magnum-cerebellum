import json
import os

class Enemy():
    def __init__(self, type_):
        f = open(os.path.join("data/enemy_data.json"))
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no enemies availible") 
        self.enemy = data[type_]
        self.type = type_
        self.actions = self.enemy["actions"]
      
    
    def __str__(self):
        return self.type