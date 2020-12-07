import json
import os
from actions import Action
import pygame
import config
import random
import encounter

# must set for items class to work (sprites)
screen = pygame.display.set_mode((800, 600))
class Enemy():
    def __init__(self, type_):
        f = open(os.path.join("data/enemy_data.json"), "r")
        data = json.load(f)
        if type_ not in data.keys():
            raise Exception("Sorry, no enemies availible")
        self.enemy = data[type_]
        self.type = type_
        self.actions = []
        #Damage list of two ints, damage will RANGE from the first & second. EX. CSE220 dmg ranges from 5 to 12
        self.damage = self.enemy["damage"]
        self.hp = 100
        for action in self.enemy["actions"]:
            self.actions.append(Action(action))

    # return False if decrease kills enemy, true otherwise. Update enemy hp with decreased ammount
    def decrease_hp(self, n):
        if (self.hp - n) <= 0:
            self.hp = 0
            return False
        else:
            self.hp = self.hp - n
            return True

    def random_attack(self):
        i = random.randint(0, len(self.actions)-1)
        config.text1.append(self.actions[i])
        return self.actions[i]

    def __str__(self):
        return self.type

def random_enemy() :  
    f = open(("data/enemy_data.json"),"r")
    data = json.load(f)
    f.close()
    enemies = data.keys()
    enemies_list = list(enemies)
    if encounter.boss_flag:
        enemy = Enemy("Ethan")
        print("in random enemy chose " + enemy.type)
        return enemy
    flag = False
    while not flag and not encounter.boss_flag:
        choice = random.choice(enemies_list)
        if choice != "Ethan":
            flag = True
    print(choice + "\n")
    for enemy in enemies:
        if enemy == choice:
            chosen_enemy = Enemy(choice)
            return chosen_enemy


# Returns Ethan as the enemy
def boss_enemy():
    print("Entering boss battle")
    f = open(("data/enemy_data.json"),"r")
    data = json.load(f)
    f.close()
    enemies = data.keys()
    enemies_list = list(enemies)
    if encounter.boss_flag:
        for enemy in enemies_list:
            if enemy == "Ethan":
                chosen_enemy = Enemy(enemy)
                return chosen_enemy
