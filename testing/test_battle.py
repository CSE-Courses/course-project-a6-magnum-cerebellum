import unittest
import json

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from player import Player
from character import Character
from enemies import Enemy

from battle import Battle

class TestBattle(unittest.TestCase):
    def test_damage_on_player(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data_character = json.load(f)
        f.close()
        f = open(os.path.join(parentdir,"data/enemy_data.json"),"r")
        data_enemy = json.load(f)
        f.close()
        characters = data_character.keys()
        enemies = data_enemy.keys()
        for character in characters:
            char = Character(character)
            player = Player(char)
            for enemy_ in enemies:
                enemy = Enemy(enemy_)
                battle = Battle(player, enemy)
                items = player.items
                
                while battle.attack_player(items[0]):
                    self.assertTrue(player.hp != 0)
                self.assertTrue(player.hp == 0)

    def test_damage_on_enemy(self):
        f = open(os.path.join(parentdir,"data/character_data.json"),"r")
        data_character = json.load(f)
        f.close()
        f = open(os.path.join(parentdir,"data/enemy_data.json"),"r")
        data_enemy = json.load(f)
        f.close()
        characters = data_character.keys()
        enemies = data_enemy.keys()
        for character in characters:
            char = Character(character)
            player = Player(char)
            for enemy_ in enemies:
                enemy = Enemy(enemy_)
                battle = Battle(player, enemy)
                items = player.items
                
                while battle.attack_enemy(items[0]):
                    self.assertTrue(enemy.hp != 0)
                self.assertTrue(enemy.hp == 0)       

if __name__ == '__main__':
    unittest.main()