import json
import os
from actions import Action
class Enemy():
    def __init__(self, type_):
        self.health = type_
        f = open(os.path.join("data/enemy_data.json"))
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no enemies availible") 
        self.enemy = data[type_]
        self.type = type_
        self.actions = []
        for action in self.enemy["actions"]:
            self.actions.append(Action(action))
        self.difficulty = {} #dictionary of difficulty levels to damage multiplier
        self.damage = self.base(None, None)
      
    
    def __str__(self):
        return self.type


    def base(self, red_zone, base_damage):
        if red_zone >= self.health / 100:
            self.damage = self.damage * 1.5
        else:
            if self.difficulty[0] == 1:
                self.damage = base_damage * self.difficulty[1]
            elif self.difficulty[0] == 2:
                self.damage = base_damage * self.difficulty[2]
            elif self.difficulty[0] == 3:
                self.damage = base_damage * self.difficulty[3]
