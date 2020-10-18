import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from character import Character
from actions import Action
from items import Item
import config
import pygame

# must set for items class to work (sprites)
screen = pygame.display.set_mode((800, 600))

class TestCharacter(unittest.TestCase):
    def test_character_name(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for char in characters: 
            new_char = Character(char)
           

    def test_character_actions(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for char in characters: 
            new_char = Character(char)
            actions = new_char.actions
            actions_from_data = []
            for i in data[char]["actions"]:
                actions_from_data.append(i)
            for entry in actions:
                self.assertIn(entry.action_name, actions_from_data)
    
    def test_character_items(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for char in characters: 
            new_char = Character(char)
            items = new_char.items
            items_from_data = []
            for i in data[char]["items"]:
                items_from_data.append(i)
            for entry in items:
                self.assertIn(entry.item_name, items_from_data)
     

if __name__ == '__main__':
    unittest.main()