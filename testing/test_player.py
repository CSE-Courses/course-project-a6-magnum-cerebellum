import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from player import Player
from character import Character
import config
class TestPlayer(unittest.TestCase):

    # test that player inherits characters actions and items #
    def test_player_inherit(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for character in characters:
            char = Character(type_=character)
            player = Player(char)
            self.assertEqual(char.actions, player.actions)
            self.assertEqual(char.items, player.items)
            
    def test_player_set_location(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for character in characters:
            char = Character(type_=character)
            player = Player(char)
            prev_pos = player.pos

            # invalid moves #
            self.assertEqual(player.set_location(-1, 0), prev_pos)
            self.assertEqual(player.set_location(0, -1), prev_pos)
            self.assertEqual(player.set_location(config.display_width + 1, 0), prev_pos)
            self.assertEqual(player.set_location(0, config.display_height + 1), prev_pos)
            # valid moves #
            self.assertEqual(player.set_location(100, 100), player.pos)
            self.assertEqual(player.set_location(0, config.display_height), player.pos)
            self.assertEqual(player.set_location(config.display_width, 0), player.pos)

if __name__ == '__main__':
    unittest.main()