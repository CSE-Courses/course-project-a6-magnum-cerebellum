import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from character import Character
import config
class TestCharacter(unittest.TestCase):
    def test_character_actions(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for char in characters: 
            new_char = Character(char)
            actions = new_char.actions
            self.assertEqual(data[char]["actions"], actions)
    
    def test_character_items(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for char in characters: 
            new_char = Character(char)
            items = new_char.items
            self.assertEqual(data[char]["items"], items)

if __name__ == '__main__':
    unittest.main()