import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from player import Player
from character import Character
from items import Item
import config
class TestPlayer(unittest.TestCase):

    # test that player inherits characters actions and items #
    def test_player_inherit(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data = json.load(f)
        f.close()
        characters = data.keys()
        for character in characters:
            char = Character(character)
            player = Player(char)
            self.assertEqual(char.actions, player.actions)
            self.assertEqual(char.items, player.items)

    def test_player_add_item(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        char_data = json.load(f)
        f.close()
        characters = char_data.keys()
        for character in characters:
            char = Character(character)
            player = Player(char)
            f = open(os.path.join("data/item_data.json"))
            item_data = json.load(f)
            item_names = item_data.keys()
            player_item_list = []
            for i in item_names:
                player.add_item(i)
                for player_item in player.items:
                    player_item_list.append(player_item.item_name)
                self.assertIn(i, player_item_list)


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