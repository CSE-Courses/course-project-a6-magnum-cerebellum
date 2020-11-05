import json
import os
from actions import Action
import pygame
import random

class Enemy():
    def __init__(self, type_):
        f = open(os.path.join("data/enemy_data.json"), "r")
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no enemies availible")
        self.enemy = data[type_]
        self.type = type_
        self.actions = []
        self.hp = 100
        for action in self.enemy["actions"]:
            self.actions.append(Action(action))

    # return False if decrease kills enemy, true otherwise. Update player hp with decreased ammount
    def decrease_hp(self, n):
        if (self.hp - n) <= 0:
            self.hp = 0
            return False
        else:
            self.hp = self.hp - n
            return True

    def random_attack(self):
        i = random.randint(0, len(self.actions)-1)
        return self.actions[i]

    def __str__(self):
        return self.type

def random_enemy() :  
    f = open(("data/enemy_data.json"),"r")
    data = json.load(f)
    f.close()
    enemies = data.keys()
    for enemy in enemies: 
        
        return enemy

